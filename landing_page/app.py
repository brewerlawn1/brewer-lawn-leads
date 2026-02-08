"""
Flask Landing Page for Brewer Lawn Designs.

Captures inbound leads via a contact/quote request form.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request, jsonify, redirect, url_for
from config import (LANDING_PAGE_HOST, LANDING_PAGE_PORT, SERVICES, COMPANY_NAME,
                     COMPANY_TAGLINE, COMPANY_LOCATION, COMPANY_STORY)
from crm.database import add_lead, get_leads, get_stats, add_interaction

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
    services = ", ".join(request.form.getlist("services"))
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

    return render_template("thank_you.html",
                           company_name=COMPANY_NAME,
                           name=name)


@app.route("/api/leads", methods=["GET"])
def api_leads():
    """Simple API endpoint to view leads (for internal use)."""
    status = request.args.get("status")
    min_score = int(request.args.get("min_score", 0))
    leads = get_leads(status=status, min_score=min_score)
    return jsonify(leads)


@app.route("/api/stats", methods=["GET"])
def api_stats():
    """API endpoint for lead statistics."""
    return jsonify(get_stats())


@app.route("/dashboard")
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
