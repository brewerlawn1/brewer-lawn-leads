"""
Flask Landing Page for Brewer Lawn Designs.

Captures inbound leads via a contact/quote request form.
"""
import sys
import os
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from functools import wraps

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
from config import (LANDING_PAGE_HOST, LANDING_PAGE_PORT, SERVICES, COMPANY_NAME,
                     COMPANY_TAGLINE, COMPANY_LOCATION, COMPANY_STORY)
from crm.database import add_lead, get_leads, get_stats, add_interaction

app = Flask(__name__)

# Email config
NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", "brewerlawndesigns@icloud.com")
SMTP_USER = os.environ.get("SMTP_USER", "brewerlawndesigns@icloud.com")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.mail.me.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))

# Dashboard password
DASHBOARD_PASSWORD = os.environ.get("DASHBOARD_PASSWORD", "brewer2026")


def send_lead_email(name, email, phone, address, service, message):
    """Send email notification for new lead in background thread."""
    if not SMTP_PASSWORD:
        return
    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = NOTIFY_EMAIL
        msg["Subject"] = f"New Lead: {name}"

        body = f"""New lead from brewerlawndesigns.org!

Name: {name}
Email: {email}
Phone: {phone}
Address: {address}
Service: {service}
Message: {message}

View all leads: https://brewerlawndesigns.org/dashboard
"""
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Email send failed: {e}")


def check_dashboard_auth(f):
    """Simple password protection for dashboard."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.password != DASHBOARD_PASSWORD:
            return Response(
                "Login required to view the dashboard.",
                401,
                {"WWW-Authenticate": 'Basic realm="Dashboard"'},
            )
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def home():
    return render_template("index.html",
                           company_name=COMPANY_NAME,
                           services=SERVICES,
                           tagline=COMPANY_TAGLINE,
                           location=COMPANY_LOCATION,
                           story=COMPANY_STORY)


@app.route("/submit-lead", methods=["POST"])
def submit_lead():
    """Handle form submission from the landing page."""
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    address = request.form.get("address", "").strip()
    services = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    if not name:
        return render_template("index.html",
                               company_name=COMPANY_NAME,
                               services=SERVICES,
                               error="Please provide your name.")

    lead_id = add_lead(
        name=name,
        email=email,
        phone=phone,
        address=address,
        source="landing_page",
        notes=message,
        services=services,
    )

    # Send email notification in background thread
    threading.Thread(
        target=send_lead_email,
        args=(name, email, phone, address, services, message),
        daemon=True,
    ).start()

    return render_template("thank_you.html",
                           company_name=COMPANY_NAME,
                           name=name)


@app.route("/api/leads", methods=["GET"])
@check_dashboard_auth
def api_leads():
    """Simple API endpoint to view leads (for internal use)."""
    status = request.args.get("status")
    min_score = int(request.args.get("min_score", 0))
    leads = get_leads(status=status, min_score=min_score)
    return jsonify(leads)


@app.route("/api/stats", methods=["GET"])
@check_dashboard_auth
def api_stats():
    """API endpoint for lead statistics."""
    return jsonify(get_stats())


@app.route("/dashboard")
@check_dashboard_auth
def dashboard():
    """Simple internal dashboard to view leads."""
    leads = get_leads()
    stats = get_stats()
    return render_template("dashboard.html",
                           company_name=COMPANY_NAME,
                           leads=leads,
                           stats=stats)


if __name__ == "__main__":
    app.run(host=LANDING_PAGE_HOST, port=LANDING_PAGE_PORT, debug=True)
