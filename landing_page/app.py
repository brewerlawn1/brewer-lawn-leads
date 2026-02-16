"""
Flask Landing Page for Brewer Lawn Designs.

Captures inbound leads via a contact/quote request form.
Serves SEO-optimized service and location pages.
"""
import sys
import os
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import json
from flask import Flask, render_template, request, abort, jsonify
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
from landing_page.blog_content import get_all_posts, get_blog_post, BLOG_POSTS

app = Flask(__name__)


# === 404 Handler ===
@app.errorhandler(404)
def page_not_found(e):
    ctx = common_ctx()
    return render_template("404.html", **ctx), 404


# === Caching & Performance Headers ===
@app.after_request
def add_performance_headers(response):
    # Cache static assets for 1 day, HTML pages for 1 hour
    if response.content_type and "text/html" in response.content_type:
        response.headers["Cache-Control"] = "public, max-age=3600"
    elif response.content_type and any(t in response.content_type for t in ["css", "javascript", "image"]):
        response.headers["Cache-Control"] = "public, max-age=86400"
    # Security headers
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


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
    ctx["service_name"] = page["name"]
    ctx.setdefault("gallery_images", [])
    ctx.setdefault("gallery_alt", [])
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


# === Blog ===
@app.route("/blog")
def blog_index():
    ctx = common_ctx()
    ctx["posts"] = get_all_posts()
    return render_template("blog.html", **ctx)


@app.route("/blog/<slug>")
def blog_post(slug):
    post = get_blog_post(slug)
    if not post:
        abort(404)
    ctx = common_ctx()
    ctx.update(post)
    ctx["recent_posts"] = get_all_posts()[:5]
    return render_template("blog_post.html", **ctx)


# === SEO Files ===
@app.route("/robots.txt")
def robots():
    txt = """User-agent: *
Allow: /
Disallow: /submit-lead
Disallow: /api/

# Sitemap
Sitemap: https://brewerlawndesigns.org/sitemap.xml

# LLM / AI Context
# See /llms.txt for AI-readable business info
"""
    return app.response_class(response=txt, status=200, mimetype="text/plain")


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

    # Blog index
    urls.append({"loc": "https://brewerlawndesigns.org/blog", "priority": "0.7", "changefreq": "weekly"})

    # Blog posts
    for p in BLOG_POSTS:
        urls.append({
            "loc": f"https://brewerlawndesigns.org/blog/{p['slug']}",
            "priority": "0.6",
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


@app.route("/llms.txt")
def llms_txt():
    """LLM-readable business information following the llms.txt standard."""
    services_list = "\n".join(f"- {s['name']}: https://brewerlawndesigns.org/services/{s['slug']}" for s in SERVICE_PAGES)
    areas_list = "\n".join(f"- {a['name']}, TX: https://brewerlawndesigns.org/areas/{a['slug']}" for a in LOCATION_PAGES)

    txt = f"""# Brewer Lawn Designs

> Professional landscaping company serving New Braunfels, TX and surrounding Texas Hill Country communities. 5-star rated on Google with 7 reviews. Family-owned, locally operated.

## Business Information

- Business Name: Brewer Lawn Designs
- Type: Landscaping & Lawn Care Company
- Location: New Braunfels, TX 78130
- Phone: {COMPANY_PHONE}
- Email: brewerlawndesigns@icloud.com
- Website: https://brewerlawndesigns.org
- Google Rating: 5.0 stars (7 reviews)
- Hours: Monday-Saturday 7:00 AM - 6:00 PM
- Price Range: $$

## Services Offered

{services_list}

## Service Areas

{areas_list}

## Why Choose Brewer Lawn Designs

- 5-star Google rating with verified reviews
- On-site consultations available (quote fee is deducted from your final bill when you hire us)
- Locally owned and operated in New Braunfels, TX
- Residential and commercial landscaping
- Full-service: design, installation, and maintenance
- Licensed and insured
- Serving the Texas Hill Country since establishment

## Contact

For a landscaping quote, visit https://brewerlawndesigns.org/#contact or call {COMPANY_PHONE}. We charge a small consultation fee, which is deducted from your final bill when you hire us.

## Social Media

- Instagram: https://www.instagram.com/brewerlawndesigns/
- Facebook: https://www.facebook.com/Brewerlawndesigns/
"""
    return app.response_class(response=txt, status=200, mimetype="text/plain")


@app.route("/llms-full.txt")
def llms_full_txt():
    """Extended LLM context with detailed service descriptions."""
    sections = []
    sections.append("# Brewer Lawn Designs - Complete Business Information\n")
    sections.append("> Full-service landscaping company in New Braunfels, TX. 5.0 Google rating.\n")

    sections.append("## Detailed Service Descriptions\n")
    for s in SERVICE_PAGES:
        sections.append(f"### {s['name']}")
        sections.append(f"URL: https://brewerlawndesigns.org/services/{s['slug']}")
        sections.append(f"{s['meta_description']}")
        if s.get("faqs"):
            for faq in s["faqs"]:
                sections.append(f"Q: {faq['q']}")
                sections.append(f"A: {faq['a']}")
        sections.append("")

    sections.append("## Service Areas in Detail\n")
    for a in LOCATION_PAGES:
        sections.append(f"### {a['name']}, TX")
        sections.append(f"URL: https://brewerlawndesigns.org/areas/{a['slug']}")
        sections.append(f"{a['meta_description']}")
        if a.get("faqs"):
            for faq in a["faqs"]:
                sections.append(f"Q: {faq['q']}")
                sections.append(f"A: {faq['a']}")
        sections.append("")

    sections.append("## Frequently Asked Questions\n")
    sections.append("Q: What areas does Brewer Lawn Designs serve?")
    sections.append("A: We serve New Braunfels, Schertz, Cibolo, San Marcos, Seguin, Garden Ridge, Canyon Lake, and surrounding Texas Hill Country communities.\n")
    sections.append("Q: How does Brewer Lawn Designs handle quotes?")
    sections.append("A: We provide on-site consultations for all landscaping services. We charge a small quote fee, which is deducted from your final bill when you hire us. Contact us at (210) 689-3036 or through our website.\n")
    sections.append("Q: What is Brewer Lawn Designs' Google rating?")
    sections.append("A: Brewer Lawn Designs has a 5.0-star rating on Google with 7 verified reviews.\n")
    sections.append("Q: Does Brewer Lawn Designs do commercial landscaping?")
    sections.append("A: Yes, we provide commercial lawn mowing, landscape maintenance, and full commercial landscaping services.\n")

    return app.response_class(
        response="\n".join(sections),
        status=200,
        mimetype="text/plain"
    )


@app.route("/.well-known/ai-context.json")
def ai_context():
    """Structured AI context for LLM discovery (JSON format)."""
    data = {
        "schema_version": "1.0",
        "business": {
            "name": "Brewer Lawn Designs",
            "type": "Landscaping Company",
            "description": COMPANY_DESCRIPTION,
            "url": "https://brewerlawndesigns.org",
            "phone": COMPANY_PHONE,
            "email": "brewerlawndesigns@icloud.com",
            "location": {
                "city": "New Braunfels",
                "state": "TX",
                "zip": "78130",
                "country": "US"
            },
            "hours": "Monday-Saturday 7:00 AM - 6:00 PM",
            "rating": {"value": 5.0, "count": 7, "source": "Google"},
            "price_range": "$$"
        },
        "services": [
            {"name": s["name"], "url": f"https://brewerlawndesigns.org/services/{s['slug']}", "description": s["meta_description"]}
            for s in SERVICE_PAGES
        ],
        "service_areas": [
            {"name": a["name"], "state": "TX", "url": f"https://brewerlawndesigns.org/areas/{a['slug']}"}
            for a in LOCATION_PAGES
        ],
        "social_media": {
            "instagram": "https://www.instagram.com/brewerlawndesigns/",
            "facebook": "https://www.facebook.com/Brewerlawndesigns/"
        },
        "content_urls": {
            "llms_txt": "https://brewerlawndesigns.org/llms.txt",
            "llms_full": "https://brewerlawndesigns.org/llms-full.txt",
            "sitemap": "https://brewerlawndesigns.org/sitemap.xml"
        }
    }
    return jsonify(data)


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("images/logo.png")


@app.route("/google9748f28534e3948e.html")
def google_verify():
    return "google-site-verification: google9748f28534e3948e.html"


if __name__ == "__main__":
    app.run(host=LANDING_PAGE_HOST, port=LANDING_PAGE_PORT, debug=True)
