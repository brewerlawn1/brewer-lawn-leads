"""
Email Finder — Scrapes lead websites to find contact email addresses.

Visits each lead's website, searches the homepage and /contact page
for email addresses, and updates the CRM database.
"""
import re
import sqlite3
import time
import requests
from urllib.parse import urljoin

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import DATABASE_PATH

# Common email patterns to ignore (generic/no-reply/platform)
IGNORE_PATTERNS = [
    r'noreply@', r'no-reply@', r'donotreply@',
    r'support@example', r'info@example', r'test@',
    r'sentry', r'webpack', r'@sentry', r'@wixpress',
    r'@w3\.org', r'@schema\.org', r'@google',
    r'user@domain', r'name@website', r'you@example',
    r'example@', r'john\.doe@', r'jane\.doe@',
    r'@example\.com', r'@example\.org',
    r'@godaddy\.com', r'@agentfire\.com',       # website builder platforms
    r'@mailparser\.io', r'@zapier\.com',         # automation platforms
    r'@indiantypefoundry', r'@windermere\.com',  # unrelated companies
    r'filler@', r'placeholder@', r'demo@',
    r'@testbuilder', r'@localhost',
]

# Pages to check for contact info
CONTACT_PATHS = ['', '/contact', '/contact-us', '/about', '/about-us']

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def extract_emails(html: str) -> set:
    """Extract email addresses from HTML content."""
    # Find all email-like patterns
    pattern = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
    raw = set(re.findall(pattern, html.lower()))

    # Filter out junk
    clean = set()
    for email in raw:
        if any(re.search(p, email) for p in IGNORE_PATTERNS):
            continue
        # Skip image files, CSS, JS, and other non-email extensions
        if email.endswith(('.png', '.jpg', '.gif', '.svg', '.css', '.js', '.webp', '.jpeg', '.woff', '.woff2')):
            continue
        clean.add(email)

    return clean


def find_emails_for_website(website: str) -> set:
    """Visit a website and its contact pages to find email addresses."""
    all_emails = set()

    for path in CONTACT_PATHS:
        url = urljoin(website.rstrip('/') + '/', path.lstrip('/'))
        try:
            resp = requests.get(url, headers=HEADERS, timeout=8, allow_redirects=True)
            if resp.status_code == 200:
                emails = extract_emails(resp.text)
                all_emails.update(emails)
        except Exception:
            pass

    return all_emails


def pick_best_email(emails: set, business_name: str) -> str:
    """Pick the most relevant email from a set of candidates."""
    if not emails:
        return ''

    emails = list(emails)

    # Prefer info@, contact@, sales@, office@ emails
    priority = ['info@', 'contact@', 'sales@', 'office@', 'hello@', 'admin@']
    for prefix in priority:
        for email in emails:
            if email.startswith(prefix):
                return email

    # Otherwise return the first one
    return emails[0]


def run_email_finder():
    """Find emails for all Google Places leads that have websites but no email."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row

    # Get leads with websites but no email
    rows = conn.execute("""
        SELECT id, name, notes FROM leads
        WHERE source='google_places'
        AND (email = '' OR email IS NULL)
        AND notes LIKE '%Website: http%'
    """).fetchall()

    print(f"Found {len(rows)} leads with websites but no email.")
    print(f"Scanning websites for contact emails...\n")

    found_count = 0
    scanned = 0

    for row in rows:
        # Extract website from notes
        match = re.search(r'Website: (https?://\S+)', row['notes'])
        if not match:
            continue

        website = match.group(1)
        scanned += 1

        print(f"  [{scanned}/{len(rows)}] {row['name'][:40]:40s} → {website[:50]}", end='', flush=True)

        emails = find_emails_for_website(website)
        best = pick_best_email(emails, row['name'])

        if best:
            conn.execute("UPDATE leads SET email = ?, updated_at = datetime('now') WHERE id = ?",
                         (best, row['id']))
            conn.commit()
            found_count += 1
            print(f"  ✓ {best}")
        else:
            print(f"  ✗ no email found")

        # Be polite — don't hammer servers
        time.sleep(0.5)

    print(f"\nDone! Found emails for {found_count}/{scanned} leads.")
    conn.close()


if __name__ == '__main__':
    run_email_finder()
