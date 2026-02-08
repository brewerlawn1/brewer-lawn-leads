"""
Email outreach module for Brewer Lawn Designs.

Sends follow-up emails to leads using SendGrid.
IMPORTANT: Only send emails to leads who have opted in (e.g., submitted a form).
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY, FROM_EMAIL, COMPANY_NAME, SERVICES
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


def run_campaign(campaign_type: str = "welcome"):
    """Run an email campaign by type."""
    print(f"Running '{campaign_type}' email campaign for {COMPANY_NAME}")
    print("=" * 50)

    if campaign_type == "welcome":
        send_welcome_emails()
    elif campaign_type == "follow_up":
        send_follow_ups()
    else:
        print(f"Unknown campaign type: {campaign_type}")
        print("Available: welcome, follow_up")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run email campaigns")
    parser.add_argument("campaign", nargs="?", default="welcome",
                        choices=["welcome", "follow_up"],
                        help="Campaign type to run")
    args = parser.parse_args()
    run_campaign(args.campaign)
