"""
CRM Database - SQLite-based lead management for Brewer Lawn Designs.

Handles lead storage, deduplication, scoring, and status tracking.
"""
import sqlite3
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import DATABASE_PATH, LEAD_SCORE_WEIGHTS


def get_connection() -> sqlite3.Connection:
    """Get a database connection, creating the DB if needed."""
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    """Create database tables if they don't exist."""
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT DEFAULT '',
            phone TEXT DEFAULT '',
            address TEXT DEFAULT '',
            source TEXT DEFAULT '',
            status TEXT DEFAULT 'new',
            score INTEGER DEFAULT 0,
            notes TEXT DEFAULT '',
            services_interested TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now')),
            updated_at TEXT DEFAULT (datetime('now')),
            last_contacted TEXT DEFAULT '',
            follow_up_date TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            details TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (lead_id) REFERENCES leads(id)
        );

        CREATE TABLE IF NOT EXISTS email_campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            body_template TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS email_sends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id INTEGER,
            lead_id INTEGER NOT NULL,
            status TEXT DEFAULT 'sent',
            sent_at TEXT DEFAULT (datetime('now')),
            opened_at TEXT DEFAULT '',
            FOREIGN KEY (campaign_id) REFERENCES email_campaigns(id),
            FOREIGN KEY (lead_id) REFERENCES leads(id)
        );
    """)
    conn.commit()
    conn.close()


def calculate_score(email: str, phone: str, address: str, source: str) -> int:
    """Calculate a lead quality score based on available info."""
    score = 0
    if email:
        score += LEAD_SCORE_WEIGHTS.get("has_email", 0)
    if phone:
        score += LEAD_SCORE_WEIGHTS.get("has_phone", 0)
    if address:
        score += LEAD_SCORE_WEIGHTS.get("has_address", 0)
    if source == "landing_page":
        score += LEAD_SCORE_WEIGHTS.get("from_landing_page", 0)
    if source == "google_places":
        score += LEAD_SCORE_WEIGHTS.get("from_directory", 0)
    return score


def add_lead(name: str, email: str = "", phone: str = "", address: str = "",
             source: str = "", notes: str = "", services: str = ""):
    """
    Add a new lead to the database. Returns the lead ID, or None if duplicate.
    Deduplication is based on name + address, or email if provided.
    """
    conn = get_connection()
    init_db()

    # Check for duplicates
    if email:
        existing = conn.execute(
            "SELECT id FROM leads WHERE email = ? AND email != ''", (email,)
        ).fetchone()
        if existing:
            conn.close()
            return None

    if name and address:
        existing = conn.execute(
            "SELECT id FROM leads WHERE name = ? AND address = ? AND address != ''",
            (name, address)
        ).fetchone()
        if existing:
            conn.close()
            return None

    score = calculate_score(email, phone, address, source)

    cursor = conn.execute(
        """INSERT INTO leads (name, email, phone, address, source, score, notes, services_interested)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (name, email, phone, address, source, score, notes, services)
    )
    lead_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return lead_id


def update_lead(lead_id: int, **kwargs):
    """Update fields on an existing lead."""
    conn = get_connection()
    allowed_fields = {
        "name", "email", "phone", "address", "status", "notes",
        "services_interested", "follow_up_date", "last_contacted"
    }
    updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
    if not updates:
        conn.close()
        return

    updates["updated_at"] = datetime.now().isoformat()
    set_clause = ", ".join(f"{k} = ?" for k in updates)
    values = list(updates.values()) + [lead_id]

    conn.execute(f"UPDATE leads SET {set_clause} WHERE id = ?", values)
    conn.commit()
    conn.close()


def get_leads(status: str = None, min_score: int = 0, limit: int = 100) -> list:
    """Retrieve leads, optionally filtered by status and minimum score."""
    conn = get_connection()
    init_db()

    query = "SELECT * FROM leads WHERE score >= ?"
    params = [min_score]

    if status:
        query += " AND status = ?"
        params.append(status)

    query += " ORDER BY score DESC, created_at DESC LIMIT ?"
    params.append(limit)

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_lead(lead_id: int):
    """Get a single lead by ID."""
    conn = get_connection()
    init_db()
    row = conn.execute("SELECT * FROM leads WHERE id = ?", (lead_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def add_interaction(lead_id: int, interaction_type: str, details: str = ""):
    """Log an interaction with a lead (call, email, meeting, etc.)."""
    conn = get_connection()
    conn.execute(
        "INSERT INTO interactions (lead_id, type, details) VALUES (?, ?, ?)",
        (lead_id, interaction_type, details)
    )
    conn.execute(
        "UPDATE leads SET last_contacted = datetime('now'), updated_at = datetime('now') WHERE id = ?",
        (lead_id,)
    )
    conn.commit()
    conn.close()


def get_interactions(lead_id: int) -> list:
    """Get all interactions for a lead."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM interactions WHERE lead_id = ? ORDER BY created_at DESC",
        (lead_id,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_stats() -> dict:
    """Get summary statistics about leads."""
    conn = get_connection()
    init_db()
    stats = {}
    stats["total"] = conn.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
    stats["new"] = conn.execute("SELECT COUNT(*) FROM leads WHERE status = 'new'").fetchone()[0]
    stats["contacted"] = conn.execute("SELECT COUNT(*) FROM leads WHERE status = 'contacted'").fetchone()[0]
    stats["qualified"] = conn.execute("SELECT COUNT(*) FROM leads WHERE status = 'qualified'").fetchone()[0]
    stats["won"] = conn.execute("SELECT COUNT(*) FROM leads WHERE status = 'won'").fetchone()[0]
    stats["lost"] = conn.execute("SELECT COUNT(*) FROM leads WHERE status = 'lost'").fetchone()[0]
    stats["avg_score"] = conn.execute("SELECT COALESCE(AVG(score), 0) FROM leads").fetchone()[0]
    conn.close()
    return stats


def export_csv(filepath: str):
    """Export all leads to a CSV file."""
    import csv
    leads = get_leads(limit=10000)
    if not leads:
        print("No leads to export.")
        return

    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=leads[0].keys())
        writer.writeheader()
        writer.writerows(leads)
    print(f"Exported {len(leads)} leads to {filepath}")
