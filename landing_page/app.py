"""
Flask Landing Page for Brewer Lawn Designs.

Captures inbound leads via a contact/quote request form.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from config import (LANDING_PAGE_HOST, LANDING_PAGE_PORT, SERVICES, COMPANY_NAME,
                     COMPANY_TAGLINE, COMPANY_LOCATION, COMPANY_STORY)
from crm.database import add_lead

app = Flask(__name__)


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

    return render_template("thank_you.html",
                           company_name=COMPANY_NAME,
                           name=name)


if __name__ == "__main__":
    app.run(host=LANDING_PAGE_HOST, port=LANDING_PAGE_PORT, debug=True)
