"""
Flask Landing Page for Brewer Lawn Designs.

Captures inbound leads via a contact/quote request form.
Serves SEO-optimized service and location pages.
"""
import sys
import os
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request, abort
from config import (LANDING_PAGE_HOST, LANDING_PAGE_PORT, SERVICES, COMPANY_NAME,
                     COMPANY_TAGLINE, COMPANY_LOCATION, COMPANY_STORY,
                     COMPANY_PHONE, COMPANY_EMAIL, COMPANY_DOMAIN,
                     COMPANY_DESCRIPTION, GA_MEASUREMENT_ID)
from crm.database import add_lead
from landing_page.seo_content import (
    get_service_page, get_location_page,
    get_all_services, get_all_areas,
    SERVICE_PAGES, LOCATION_PAGES,
)

app = Flask(__name__)


# === Common template context ===
def common_ctx():
    """Return context variables shared across all pages."""
    return {
        "company_name": COMPANY_NAME,
        "phone": COMPANY_PHONE,
        "domain": COMPANY_DOMAIN,
        "ga_id": GA_MEASUREMENT_ID,
        "all_services": get_all_services(),
        "service_areas": get_all_areas(),
    }


# === Homepage ===
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


# === Service Pages ===
@app.route("/services/<slug>")
def service_page(slug):
    page = get_service_page(slug)
    if not page:
        abort(404)
    ctx = common_ctx()
    ctx.update(page)
    return render_template("service.html", **ctx)


# === Location Pages ===
@app.route("/areas")
def areas_index():
    ctx = common_ctx()
    return render_template("areas.html", **ctx)


@app.route("/areas/<slug>")
def location_page(slug):
    page = get_location_page(slug)
    if not page:
        abort(404)
    ctx = common_ctx()
    ctx.update(page)
    ctx["city_name"] = page["name"]
    return render_template("location.html", **ctx)


# === Lead Form Submission ===
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


# === SEO Files ===
@app.route("/robots.txt")
def robots():
    return app.response_class(
        response="User-agent: *\nAllow: /\nSitemap: https://brewerlawndesigns.org/sitemap.xml\n",
        status=200,
        mimetype="text/plain"
    )


@app.route("/sitemap.xml")
def sitemap():
    today = date.today().isoformat()
    urls = []

    # Homepage
    urls.append({"loc": "https://brewerlawndesigns.org/", "priority": "1.0", "changefreq": "weekly"})

    # Service pages
    for s in SERVICE_PAGES:
        urls.append({
            "loc": f"https://brewerlawndesigns.org/services/{s['slug']}",
            "priority": "0.9",
            "changefreq": "monthly",
        })

    # Areas index
    urls.append({"loc": "https://brewerlawndesigns.org/areas", "priority": "0.8", "changefreq": "monthly"})

    # Location pages
    for a in LOCATION_PAGES:
        urls.append({
            "loc": f"https://brewerlawndesigns.org/areas/{a['slug']}",
            "priority": "0.8",
            "changefreq": "monthly",
        })

    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_parts.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        xml_parts.append(f"""  <url>
    <loc>{u['loc']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{u['changefreq']}</changefreq>
    <priority>{u['priority']}</priority>
  </url>""")
    xml_parts.append('</urlset>')

    return app.response_class(
        response="\n".join(xml_parts),
        status=200,
        mimetype="application/xml"
    )


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("images/logo.png")


@app.route("/google9748f28534e3948e.html")
def google_verify():
    return "google-site-verification: google9748f28534e3948e.html"


if __name__ == "__main__":
    app.run(host=LANDING_PAGE_HOST, port=LANDING_PAGE_PORT, debug=True)
