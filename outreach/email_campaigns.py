"""
Email outreach module for Brewer Lawn Designs.

Sends follow-up emails to leads using SendGrid.

Campaign types:
  welcome    - Welcome emails to new landing page leads (opted in)
  follow_up  - Follow-up emails to contacted leads
  cold       - Cold B2B outreach to Google Places leads with emails
"""
import sys
import os
import re
import sqlite3

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY, FROM_EMAIL, COMPANY_NAME, SERVICES, DATABASE_PATH
from crm.database import get_leads, add_interaction, update_lead


# --- Email Templates ---

WELCOME_TEMPLATE = """
Hi {name},

Thank you for your interest in {company}!

We received your request and wanted to follow up personally. We'd love to learn
more about your landscaping needs and provide you with a free estimate.

Our services include:
{services_list}

Would you like to schedule a free on-site consultation? Just reply to this email
or give us a call and we'll find a time that works for you.

Best regards,
{company}
""".strip()

FOLLOW_UP_TEMPLATE = """
Hi {name},

We wanted to check in and see if you're still interested in landscaping services
for your property.

Spring is a great time to get started on lawn care, garden design, or any outdoor
improvements you've been thinking about.

We'd be happy to come out for a free estimate at your convenience. Just reply to
this email or give us a call.

Looking forward to hearing from you!

Best regards,
{company}
""".strip()

SEASONAL_TEMPLATE = """
Hi {name},

{seasonal_message}

As a reminder, {company} offers a full range of landscaping services to keep your
property looking its best year-round.

Would you like to schedule a service? Reply to this email or call us anytime.

Best,
{company}
""".strip()

# --- Cold Outreach Templates (B2B by category) ---

COLD_TEMPLATES = {
    "Property Management": {
        "subject": "Landscaping services for your managed properties",
        "body": """Hi {first_name},

I'm Andrew with Brewer Lawn Designs here in New Braunfels. I came across {business} and wanted to reach out.

We work with property management companies across the area to keep their properties looking sharp — from weekly mowing and seasonal cleanup to full landscape installations.

A few things that set us apart:
  - Reliable weekly/biweekly service with photo documentation
  - Volume pricing for multiple properties
  - Fast turnaround on tenant move-out cleanups

Would it make sense to chat about your current landscaping needs? I'm happy to swing by one of your properties for a free walkthrough and estimate.

Best,
Andrew Brewer
Brewer Lawn Designs
New Braunfels, TX
brewerlawndesigns.org""",
    },
    "HOA / Community": {
        "subject": "Landscape maintenance for {business}",
        "body": """Hi {first_name},

I'm Andrew with Brewer Lawn Designs, a local landscaping company here in New Braunfels.

I wanted to introduce ourselves to {business} — we specialize in HOA and community common area maintenance, including:
  - Weekly mowing of common areas, entrances, and medians
  - Seasonal flower bed rotations and mulching
  - Irrigation monitoring and adjustments
  - Tree and shrub trimming

We currently serve several communities in the area and understand that consistency and communication are what matter most to HOA boards.

Would it be worth a quick conversation about your community's landscaping needs? I'd be happy to put together a proposal.

Best,
Andrew Brewer
Brewer Lawn Designs
New Braunfels, TX
brewerlawndesigns.org""",
    },
    "Real Estate": {
        "subject": "Curb appeal services for your listings",
        "body": """Hi {first_name},

I'm Andrew with Brewer Lawn Designs in New Braunfels. I help realtors make their listings shine with professional landscaping and curb appeal services.

For your listings, we offer:
  - Quick-turnaround lawn cleanup before showings and photos
  - Sod installation and fresh mulch for instant curb appeal
  - Full landscape makeovers for properties that need extra help
  - Ongoing maintenance for investment properties

A well-landscaped yard can add real value to your listings. I'd love to be your go-to landscaper for getting properties show-ready.

Would you be open to a quick call to see how we might work together?

Best,
Andrew Brewer
Brewer Lawn Designs
New Braunfels, TX
brewerlawndesigns.org""",
    },
    "Home Builder": {
        "subject": "Landscaping partner for your new builds",
        "body": """Hi {first_name},

I'm Andrew with Brewer Lawn Designs here in New Braunfels. I wanted to introduce ourselves as a potential landscaping partner for your new construction projects.

We work with builders across the area on:
  - Final grade preparation and sod installation
  - Hardscaping — walkways, patios, retaining walls
  - Irrigation system installation
  - Full landscape design for model homes and completed builds

We're reliable, licensed, and can scale to handle multiple lots. I'd love to discuss how we could support {business} on upcoming projects.

Any interest in connecting for a quick conversation?

Best,
Andrew Brewer
Brewer Lawn Designs
New Braunfels, TX
brewerlawndesigns.org""",
    },
    "Commercial Property": {
        "subject": "Commercial landscaping services in New Braunfels",
        "body": """Hi {first_name},

I'm Andrew with Brewer Lawn Designs. We provide commercial landscaping services throughout New Braunfels and the surrounding area.

For commercial properties, we offer:
  - Weekly grounds maintenance and mowing
  - Seasonal color rotations and bed maintenance
  - Tree and shrub care
  - Irrigation management
  - Snow/ice removal (when needed)

We'd welcome the opportunity to provide a competitive bid on your property's landscaping needs. Happy to do a free walkthrough and put together a proposal.

Would a brief call work to discuss your needs?

Best,
Andrew Brewer
Brewer Lawn Designs
New Braunfels, TX
brewerlawndesigns.org""",
    },
    "Other": {
        "subject": "Landscaping services in New Braunfels — Brewer Lawn Designs",
        "body": """Hi {first_name},

I'm Andrew with Brewer Lawn Designs, a local landscaping company serving New Braunfels and the surrounding area.

I came across {business} and wanted to introduce ourselves. We offer a full range of landscaping services:
  - Lawn mowing and maintenance
  - Landscaping and garden design
  - Hardscaping — patios, walkways, retaining walls
  - Sod and artificial turf installation
  - Seasonal cleanup

We'd love the chance to earn your business. Would you be open to a quick conversation about your landscaping needs? Free estimates, always.

Best,
Andrew Brewer
Brewer Lawn Designs
New Braunfels, TX
brewerlawndesigns.org""",
    },
}


def categorize_lead(notes: str, name: str) -> str:
    """Categorize a lead based on its notes and name."""
    text = ((notes or '') + ' ' + (name or '')).lower()
    if any(w in text for w in ['hoa', 'homeowner', 'owners association', 'community']):
        return 'HOA / Community'
    if any(w in text for w in ['property manag', 'pm ', 'rental']):
        return 'Property Management'
    if any(w in text for w in ['real estate', 'realt', 'broker', 'listing']):
        return 'Real Estate'
    if any(w in text for w in ['builder', 'construction', 'custom home', 'new home']):
        return 'Home Builder'
    if any(w in text for w in ['commercial', 'office', 'retail', 'industrial']):
        return 'Commercial Property'
    return 'Other'


def get_first_name(business_name: str) -> str:
    """Extract a reasonable greeting name from a business name."""
    # If it looks like a person's name (2-3 short words, no business words)
    biz_words = ['llc', 'inc', 'corp', 'group', 'realty', 'homes', 'properties',
                 'management', 'construction', 'builders', 'associates', 'association']
    words = business_name.split()
    if len(words) <= 3 and not any(w.lower().strip('.,') in biz_words for w in words):
        return words[0]
    return 'there'


def send_email(to_email: str, subject: str, body: str) -> bool:
    """Send a single email via SendGrid. Returns True on success."""
    if not SENDGRID_API_KEY:
        print(f"  [DRY RUN] Would send to {to_email}: {subject}")
        return True

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=body,
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code in (200, 201, 202)
    except Exception as e:
        print(f"  Error sending to {to_email}: {e}")
        return False


def send_welcome_emails():
    """
    Send welcome emails to new leads from the landing page
    who have provided an email address.
    """
    leads = get_leads(status="new")
    landing_page_leads = [
        l for l in leads
        if l["source"] == "landing_page" and l["email"]
    ]

    if not landing_page_leads:
        print("No new landing page leads with email addresses to contact.")
        return

    services_list = "\n".join(f"  - {s}" for s in SERVICES)
    sent_count = 0

    for lead in landing_page_leads:
        body = WELCOME_TEMPLATE.format(
            name=lead["name"].split()[0],  # First name only
            company=COMPANY_NAME,
            services_list=services_list,
        )
        subject = f"Thanks for contacting {COMPANY_NAME}!"

        success = send_email(lead["email"], subject, body)
        if success:
            sent_count += 1
            add_interaction(lead["id"], "email", f"Sent welcome email: {subject}")
            update_lead(lead["id"], status="contacted")
            print(f"  Sent welcome email to {lead['name']} ({lead['email']})")

    print(f"\nSent {sent_count} welcome emails.")


def send_follow_ups():
    """
    Send follow-up emails to leads that were contacted but haven't
    been qualified yet.
    """
    leads = get_leads(status="contacted")
    email_leads = [l for l in leads if l["email"]]

    if not email_leads:
        print("No contacted leads to follow up with.")
        return

    sent_count = 0

    for lead in email_leads:
        body = FOLLOW_UP_TEMPLATE.format(
            name=lead["name"].split()[0],
            company=COMPANY_NAME,
        )
        subject = f"Following up - {COMPANY_NAME}"

        success = send_email(lead["email"], subject, body)
        if success:
            sent_count += 1
            add_interaction(lead["id"], "email", f"Sent follow-up email: {subject}")
            print(f"  Sent follow-up to {lead['name']} ({lead['email']})")

    print(f"\nSent {sent_count} follow-up emails.")


def send_cold_outreach(dry_run: bool = True, limit: int = 0, category_filter: str = ""):
    """
    Send cold B2B outreach emails to Google Places leads with emails.

    Args:
        dry_run: If True, only preview — don't actually send or update DB.
        limit: Max emails to send (0 = all).
        category_filter: Only send to this category (e.g., 'HOA / Community').
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row

    # Get Google Places leads with emails that haven't been contacted yet
    rows = conn.execute("""
        SELECT id, name, email, phone, notes, status FROM leads
        WHERE source = 'google_places'
        AND email IS NOT NULL AND email != ''
        AND status = 'new'
        AND last_contacted = ''
        ORDER BY score DESC
    """).fetchall()

    if not rows:
        print("No uncontacted Google Places leads with emails found.")
        conn.close()
        return

    # Categorize and filter
    leads_by_cat = {}
    for row in rows:
        cat = categorize_lead(row['notes'], row['name'])
        if category_filter and cat != category_filter:
            continue
        if cat not in leads_by_cat:
            leads_by_cat[cat] = []
        leads_by_cat[cat].append(dict(row))

    total = sum(len(v) for v in leads_by_cat.values())
    if total == 0:
        print(f"No leads matching filter '{category_filter}'." if category_filter
              else "No uncontacted leads found.")
        conn.close()
        return

    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"\n{'='*60}")
    print(f"  COLD OUTREACH CAMPAIGN — {mode}")
    print(f"  {total} leads across {len(leads_by_cat)} categories")
    if limit:
        print(f"  Limit: {limit} emails")
    print(f"{'='*60}\n")

    # Show breakdown
    for cat, leads in sorted(leads_by_cat.items()):
        print(f"  {cat:<25} {len(leads):>3} leads")
    print()

    sent_count = 0
    skipped = 0

    for cat, leads in sorted(leads_by_cat.items()):
        template = COLD_TEMPLATES.get(cat, COLD_TEMPLATES['Other'])
        print(f"\n--- {cat} ({len(leads)} leads) ---")

        for lead in leads:
            if limit and sent_count >= limit:
                break

            first_name = get_first_name(lead['name'])
            subject = template['subject'].format(
                business=lead['name'],
                first_name=first_name,
            )
            body = template['body'].format(
                business=lead['name'],
                first_name=first_name,
            )

            if dry_run:
                print(f"  [DRY RUN] {lead['name'][:35]:<35} → {lead['email']}")
                sent_count += 1
            else:
                success = send_email(lead['email'], subject, body)
                if success:
                    sent_count += 1
                    add_interaction(lead['id'], "email", f"Cold outreach: {subject}")
                    update_lead(lead['id'], status="contacted")
                    print(f"  ✓ {lead['name'][:35]:<35} → {lead['email']}")
                else:
                    skipped += 1
                    print(f"  ✗ {lead['name'][:35]:<35} → FAILED")

        if limit and sent_count >= limit:
            print(f"\n  Reached limit of {limit} emails.")
            break

    print(f"\n{'='*60}")
    if dry_run:
        print(f"  DRY RUN COMPLETE: {sent_count} emails would be sent")
        print(f"  To send for real: python main.py email cold --send")
    else:
        print(f"  SENT: {sent_count} emails  |  FAILED: {skipped}")
    print(f"{'='*60}\n")

    conn.close()


def preview_cold_email(category: str = "Property Management"):
    """Preview a sample cold email for a given category."""
    template = COLD_TEMPLATES.get(category, COLD_TEMPLATES['Other'])
    print(f"\n--- Preview: {category} ---")
    print(f"Subject: {template['subject'].format(business='[Business Name]', first_name='[Name]')}")
    print(f"\n{template['body'].format(business='[Business Name]', first_name='[Name]')}")
    print()


def run_campaign(campaign_type: str = "welcome", send: bool = False,
                 limit: int = 0, category: str = "", preview: bool = False):
    """Run an email campaign by type."""
    print(f"Running '{campaign_type}' email campaign for {COMPANY_NAME}")
    print("=" * 50)

    if campaign_type == "welcome":
        send_welcome_emails()
    elif campaign_type == "follow_up":
        send_follow_ups()
    elif campaign_type == "cold":
        if preview:
            for cat in COLD_TEMPLATES:
                preview_cold_email(cat)
        else:
            send_cold_outreach(dry_run=not send, limit=limit, category_filter=category)
    else:
        print(f"Unknown campaign type: {campaign_type}")
        print("Available: welcome, follow_up, cold")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run email campaigns")
    parser.add_argument("campaign", nargs="?", default="welcome",
                        choices=["welcome", "follow_up", "cold"],
                        help="Campaign type to run")
    parser.add_argument("--send", action="store_true",
                        help="Actually send emails (cold campaign only, default is dry run)")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max number of emails to send")
    parser.add_argument("--category", type=str, default="",
                        help="Filter by category (e.g., 'HOA / Community')")
    parser.add_argument("--preview", action="store_true",
                        help="Preview email templates")
    args = parser.parse_args()
    run_campaign(args.campaign, send=args.send, limit=args.limit,
                 category=args.category, preview=args.preview)
