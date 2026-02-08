# Brewer Lawn Designs - Lead Generation System

A local lead generation system with four components: web scraping, a landing page with lead capture forms, a CRM database, and automated email outreach.

## Quick Start

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Copy and fill in your config
cp .env.example .env
# Edit .env with your API keys and company info

# 3. Start the landing page + dashboard
python main.py server
# Visit http://localhost:5000 for the landing page
# Visit http://localhost:5000/dashboard for the lead dashboard
```

## Commands

| Command | Description |
|---------|-------------|
| `python main.py scrape` | Scrape Google Places for potential leads |
| `python main.py server` | Start the landing page web server |
| `python main.py leads` | View all leads in the terminal |
| `python main.py leads --status new` | Filter leads by status |
| `python main.py stats` | Show lead statistics |
| `python main.py email welcome` | Send welcome emails to new inbound leads |
| `python main.py email follow_up` | Send follow-ups to contacted leads |
| `python main.py export` | Export all leads to CSV |

## Setup Details

### Google Places API (for scraping)
1. Go to https://console.cloud.google.com
2. Create a project and enable the Places API and Geocoding API
3. Create an API key and add it to your `.env` file

### SendGrid (for email outreach)
1. Sign up at https://sendgrid.com (free tier: 100 emails/day)
2. Create an API key and add it to your `.env` file
3. Verify your sender email address in SendGrid

### Without API keys
The system works without API keys for local lead management:
- The landing page captures leads without any API keys
- The CRM database stores and scores leads locally
- Email campaigns run in "dry run" mode (prints what would be sent)

## Project Structure

```
brewer-lawn-leads/
├── main.py                  # CLI entry point
├── config.py                # Configuration
├── .env.example             # Environment variable template
├── requirements.txt         # Python dependencies
├── scraper/
│   └── google_places.py     # Google Places API lead scraper
├── landing_page/
│   ├── app.py               # Flask web server
│   ├── templates/           # HTML templates
│   └── static/css/          # Stylesheets
├── crm/
│   └── database.py          # SQLite lead database & management
├── outreach/
│   └── email_campaigns.py   # SendGrid email campaigns
└── data/
    └── leads.db             # SQLite database (auto-created)
```

## Lead Scoring

Leads are automatically scored based on available information:

| Criteria | Points |
|----------|--------|
| From landing page (inbound) | +30 |
| New homeowner | +25 |
| Has email | +20 |
| Has phone | +15 |
| Has address | +10 |
| From directory | +10 |

## Lead Statuses

- **new** - Just added, not yet contacted
- **contacted** - Initial outreach sent
- **qualified** - Confirmed interest, good fit
- **won** - Became a customer
- **lost** - Not interested or unresponsive
