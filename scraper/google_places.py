"""
Google Places API scraper for finding potential landscape leads.

Searches for businesses and properties that may need landscaping services:
- Property management companies
- HOA communities
- New construction / home builders
- Commercial properties
"""
import requests
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import GOOGLE_API_KEY, SERVICE_AREA_ZIP, SERVICE_RADIUS_MILES
from crm.database import add_lead


PLACES_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
PLACE_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"


def get_coordinates_from_zip(zip_code: str) -> tuple:
    """Convert a zip code to lat/lng coordinates."""
    resp = requests.get(GEOCODE_URL, params={
        "address": zip_code,
        "key": GOOGLE_API_KEY,
    })
    resp.raise_for_status()
    data = resp.json()
    if data["status"] != "OK" or not data["results"]:
        raise ValueError(f"Could not geocode zip code: {zip_code}")
    location = data["results"][0]["geometry"]["location"]
    return location["lat"], location["lng"]


def search_places(query: str, lat: float, lng: float, radius_meters: int) -> list:
    """Search Google Places for businesses matching a query near a location."""
    results = []
    params = {
        "query": query,
        "location": f"{lat},{lng}",
        "radius": radius_meters,
        "key": GOOGLE_API_KEY,
    }
    resp = requests.get(PLACES_SEARCH_URL, params=params)
    resp.raise_for_status()
    data = resp.json()

    if data["status"] != "OK":
        print(f"  Google Places returned status: {data['status']}")
        return results

    results.extend(data.get("results", []))

    # Follow pagination (up to 3 pages max from Google)
    while "next_page_token" in data:
        import time
        time.sleep(2)  # Google requires a short delay before using page tokens
        params = {
            "pagetoken": data["next_page_token"],
            "key": GOOGLE_API_KEY,
        }
        resp = requests.get(PLACES_SEARCH_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        results.extend(data.get("results", []))

    return results


def get_place_details(place_id: str) -> dict:
    """Get detailed info (phone, website, etc.) for a specific place."""
    resp = requests.get(PLACE_DETAILS_URL, params={
        "place_id": place_id,
        "fields": "name,formatted_address,formatted_phone_number,website,type,business_status",
        "key": GOOGLE_API_KEY,
    })
    resp.raise_for_status()
    data = resp.json()
    if data["status"] != "OK":
        return {}
    return data.get("result", {})


def scrape_leads(keywords=None):
    """
    Main entry point: search Google Places for potential leads
    and save them to the CRM database.
    """
    from config import SCRAPER_KEYWORDS

    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY is not set in .env")
        print("Get a key at https://console.cloud.google.com")
        return

    if not SERVICE_AREA_ZIP:
        print("ERROR: SERVICE_AREA_ZIP is not set in .env")
        return

    keywords = keywords or SCRAPER_KEYWORDS
    radius_meters = SERVICE_RADIUS_MILES * 1609  # miles to meters

    print(f"Geocoding zip code {SERVICE_AREA_ZIP}...")
    lat, lng = get_coordinates_from_zip(SERVICE_AREA_ZIP)
    print(f"  Center: ({lat}, {lng})")
    print(f"  Radius: {SERVICE_RADIUS_MILES} miles ({radius_meters} meters)")
    print()

    total_added = 0

    for keyword in keywords:
        print(f"Searching: '{keyword}'...")
        places = search_places(keyword, lat, lng, radius_meters)
        print(f"  Found {len(places)} results")

        for place in places:
            place_id = place.get("place_id")
            if not place_id:
                continue

            details = get_place_details(place_id)
            if not details:
                continue

            name = details.get("name", "")
            address = details.get("formatted_address", "")
            phone = details.get("formatted_phone_number", "")
            website = details.get("website", "")

            lead_id = add_lead(
                name=name,
                email="",  # Google Places doesn't provide emails
                phone=phone,
                address=address,
                source="google_places",
                notes=f"Found via keyword: {keyword}. Website: {website}",
            )
            if lead_id:
                total_added += 1

        print(f"  Added {total_added} new leads so far")
        print()

    print(f"Scraping complete. Total new leads added: {total_added}")


if __name__ == "__main__":
    scrape_leads()
