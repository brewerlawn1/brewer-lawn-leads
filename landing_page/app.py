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

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from config import (LANDING_PAGE_HOST, LANDING_PAGE_PORT, SERVICES, COMPANY_NAME,
                     COMPANY_TAGLINE, COMPANY_LOCATION, COMPANY_STORY)
from crm.database import add_lead

app = Flask(__name__)

# Email config
NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", "brewerlawndesigns@icloud.com")
SMTP_USER = os.environ.get("SMTP_USER", "brewerlawndesigns@icloud.com")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.mail.me.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "465"))


def send_lead_email(name, email, phone, address, service, message):
    """Send email notification for new lead."""
    sys.stderr.write(f"[EMAIL] Attempting to send lead email for {name}...\n")
    sys.stderr.write(f"[EMAIL] SMTP_PASSWORD set: {bool(SMTP_PASSWORD)}\n")
    sys.stderr.write(f"[EMAIL] SMTP_USER: {SMTP_USER}\n")
    sys.stderr.write(f"[EMAIL] SMTP_HOST: {SMTP_HOST}:{SMTP_PORT}\n")
    if not SMTP_PASSWORD:
        sys.stderr.write("[EMAIL] No SMTP_PASSWORD set, skipping email\n")
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
"""
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=10) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        sys.stderr.write(f"[EMAIL] Successfully sent lead email for {name}\n")
    except Exception as e:
        sys.stderr.write(f"[EMAIL] Send failed: {e}\n")


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

    add_lead(
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
    ).start()

    return render_template("thank_you.html",
                           company_name=COMPANY_NAME,
                           name=name)


if __name__ == "__main__":
    app.run(host=LANDING_PAGE_HOST, port=LANDING_PAGE_PORT, debug=True)
