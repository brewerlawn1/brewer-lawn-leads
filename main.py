#!/usr/bin/env python3
"""
Brewer Lawn Designs - Lead Generation System
Main CLI entry point.

Usage:
    python main.py scrape         - Scrape Google Places for leads
    python main.py server         - Start the landing page web server
    python main.py dashboard      - Open the lead dashboard (starts server)
    python main.py leads          - View all leads in the terminal
    python main.py stats          - Show lead statistics
    python main.py email welcome  - Send welcome emails to new leads
    python main.py email follow_up - Send follow-up emails
    python main.py export         - Export leads to CSV
"""
import argparse
import sys
from crm.database import get_leads, get_stats, export_csv, init_db


def cmd_scrape(args):
    from scraper.google_places import scrape_leads
    scrape_leads()


def cmd_server(args):
    from landing_page.app import app
    from config import LANDING_PAGE_HOST, LANDING_PAGE_PORT
    print(f"Starting landing page at http://{LANDING_PAGE_HOST}:{LANDING_PAGE_PORT}")
    print(f"Dashboard at http://{LANDING_PAGE_HOST}:{LANDING_PAGE_PORT}/dashboard")
    app.run(host=LANDING_PAGE_HOST, port=LANDING_PAGE_PORT, debug=True)


def cmd_leads(args):
    init_db()
    status = args.status if hasattr(args, 'status') else None
    leads = get_leads(status=status)

    if not leads:
        print("No leads found.")
        return

    print(f"\n{'Score':>5}  {'Name':<25} {'Email':<30} {'Phone':<15} {'Source':<15} {'Status':<10}")
    print("-" * 105)

    for lead in leads:
        print(f"{lead['score']:>5}  {lead['name']:<25} {lead['email'] or '-':<30} "
              f"{lead['phone'] or '-':<15} {lead['source']:<15} {lead['status']:<10}")

    print(f"\nTotal: {len(leads)} leads")


def cmd_stats(args):
    init_db()
    stats = get_stats()
    print(f"\n{'Brewer Lawn Designs - Lead Stats':^40}")
    print("=" * 40)
    print(f"  Total Leads:    {stats['total']}")
    print(f"  New:            {stats['new']}")
    print(f"  Contacted:      {stats['contacted']}")
    print(f"  Qualified:      {stats['qualified']}")
    print(f"  Won:            {stats['won']}")
    print(f"  Lost:           {stats['lost']}")
    print(f"  Avg Score:      {stats['avg_score']:.0f}")
    print()


def cmd_email(args):
    from outreach.email_campaigns import run_campaign
    run_campaign(args.campaign_type)


def cmd_export(args):
    init_db()
    filepath = args.output or "data/leads_export.csv"
    export_csv(filepath)


def main():
    parser = argparse.ArgumentParser(
        description="Brewer Lawn Designs - Lead Generation System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # scrape
    sub = subparsers.add_parser("scrape", help="Scrape Google Places for leads")
    sub.set_defaults(func=cmd_scrape)

    # server
    sub = subparsers.add_parser("server", help="Start the landing page web server")
    sub.set_defaults(func=cmd_server)

    # leads
    sub = subparsers.add_parser("leads", help="View leads in the terminal")
    sub.add_argument("--status", choices=["new", "contacted", "qualified", "won", "lost"],
                     help="Filter by status")
    sub.set_defaults(func=cmd_leads)

    # stats
    sub = subparsers.add_parser("stats", help="Show lead statistics")
    sub.set_defaults(func=cmd_stats)

    # email
    sub = subparsers.add_parser("email", help="Run email campaigns")
    sub.add_argument("campaign_type", choices=["welcome", "follow_up"],
                     help="Type of email campaign")
    sub.set_defaults(func=cmd_email)

    # export
    sub = subparsers.add_parser("export", help="Export leads to CSV")
    sub.add_argument("-o", "--output", help="Output file path (default: data/leads_export.csv)")
    sub.set_defaults(func=cmd_export)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()
