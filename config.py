"""
Brewer Lawn Designs - Lead Generation System Configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

# === Company Info ===
COMPANY_NAME = "Brewer Lawn Designs"
COMPANY_EMAIL = os.getenv("COMPANY_EMAIL", "info@brewerlawndesigns.com")
COMPANY_PHONE = os.getenv("COMPANY_PHONE", "")
SERVICE_AREA_ZIP = os.getenv("SERVICE_AREA_ZIP", "")  # Your primary zip code
SERVICE_RADIUS_MILES = int(os.getenv("SERVICE_RADIUS_MILES", "25"))

# === Google Places API ===
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# === Email / SendGrid ===
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")
FROM_EMAIL = os.getenv("FROM_EMAIL", COMPANY_EMAIL)

# === Database ===
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "data", "leads.db")

# === Landing Page ===
LANDING_PAGE_HOST = os.getenv("LANDING_PAGE_HOST", "0.0.0.0")
LANDING_PAGE_PORT = int(os.getenv("LANDING_PAGE_PORT", "8080"))

# === Lead Scoring Weights ===
LEAD_SCORE_WEIGHTS = {
    "has_email": 20,
    "has_phone": 15,
    "has_address": 10,
    "from_landing_page": 30,   # Inbound leads score higher
    "new_homeowner": 25,
    "from_directory": 10,
}

# === Search Keywords for Scraper ===
SCRAPER_KEYWORDS = [
    "new home construction",
    "real estate listings",
    "home builders",
    "property management companies",
    "HOA communities",
    "commercial property managers",
]

# === Services Offered (for landing page & outreach) ===
SERVICES = [
    "Landscaping",
    "Hardscaping",
    "Landscape Maintenance",
    "Sod",
    "Artificial Turf",
    "Fall and Spring Cleanup",
    "Concrete & Masonry",
    "Garden Design",
]

# === Company Details (for landing page) ===
COMPANY_TAGLINE = "Expertise. Reliability. Value."
COMPANY_LOCATION = "New Braunfels"
COMPANY_STORY = (
    "Brewer Lawn Designs is known for its outstanding work, quality landscaping "
    "that our clients in New Braunfels and surrounding areas appreciate and trust. "
    "From small, neighborhood gardens to sprawling lawns and commercial spaces, "
    "we approach every project with care and meticulous detail. We believe in "
    "building lasting relationships with our clients, getting to know them and "
    "their personal style so that we can best bring their vision to life."
)
