"""
Flask Landing Page for Brewer Lawn Designs.

Captures inbound leads via a contact/quote request form.
"""
import sys
import os
import json
import threading
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from config import (LANDING_PAGE_HOST, LANDING_PAGE_PORT, SERVICES, COMPANY_NAME,
                     COMPANY_TAGLINE, COMPANY_LOCATION, COMPANY_STORY)
from crm.database import add_lead

app = Flask(__name__)

# Web3Forms API key (free HTTPS email forwarding)
WEB3FORMS_KEY = os.environ.get("WEB3FORMS_KEY", "ccf95b96-b6bd-416f-904a-f796ba981034")


def send_lead_email(name, email, phone, address, service, message):
    """Send email notification for new lead via Web3Forms API."""
    sys.stderr.write(f"[EMAIL] Sending lead email for {name} via Web3Forms...\n")
    try:
        data = json.dumps({
            "access_key": WEB3FORMS_KEY,
            "subject": f"New Lead: {name}",
            "from_name": "Brewer Lawn Designs Website",
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "service": service,
            "message": message,
        }).encode("utf-8")

        req = urllib.request.Request(
            "https://api.web3forms.com/submit",
            data=data,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode())
            sys.stderr.write(f"[EMAIL] Web3Forms response: {result}\n")
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
