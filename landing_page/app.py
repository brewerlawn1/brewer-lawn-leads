"""
Flask Landing Page for Brewer Lawn Designs.

Captures inbound leads via a contact/quote request form.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from config import (LANDING_PAGE_HOST, LANDING_PAGE_PORT, SERVICES, COMPANY_NAME,
                     COMPANY_TAGLINE, COMPANY_LOCATION, COMPANY_STORY,
                     COMPANY_PHONE, COMPANY_EMAIL, COMPANY_DOMAIN,
                     COMPANY_DESCRIPTION, GA_MEASUREMENT_ID)
from crm.database import add_lead

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",
                           company_name=COMPANY_NAME,
                           services=SERVICES,
                           tagline=COMPANY_TAGLINE,
                           location=COMPANY_LOCATION,
                           story=COMPANY_STORY,
                           phone=COMPANY_PHONE,
                           email=COMPANY_EMAIL,
                           domain=COMPANY_DOMAIN,
                           description=COMPANY_DESCRIPTION,
                           ga_id=GA_MEASUREMENT_ID)


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


@app.route("/robots.txt")
def robots():
    return app.response_class(
        response="User-agent: *\nAllow: /\nSitemap: https://brewerlawndesigns.org/sitemap.xml\n",
        status=200,
        mimetype="text/plain"
    )


@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://brewerlawndesigns.org/</loc>
    <lastmod>2026-02-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""
    return app.response_class(response=xml, status=200, mimetype="application/xml")


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("images/logo.png")


@app.route("/google9748f28534e3948e.html")
def google_verify():
    return "google-site-verification: google9748f28534e3948e.html"


if __name__ == "__main__":
    app.run(host=LANDING_PAGE_HOST, port=LANDING_PAGE_PORT, debug=True)
