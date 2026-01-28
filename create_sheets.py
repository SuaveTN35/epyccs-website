#!/usr/bin/env python3
"""
Epyc Courier Service — Google Sheets Automation Script
Creates 4 Google Sheets with correct tabs, imports CSV data, formats headers.
Outputs Sheet IDs for n8n environment variable configuration.

Prerequisites:
  1. Google Cloud project with Sheets API + Drive API enabled
  2. OAuth Desktop credentials downloaded as credentials.json in this directory
  3. pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

Usage:
  python3 create_sheets.py
"""

import csv
import json
import os
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# --- Configuration -----------------------------------------------------------

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(SCRIPT_DIR, "credentials.json")
TOKEN_FILE = os.path.join(SCRIPT_DIR, "token.json")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "sheet-ids.json")
SHEETS_DIR = os.path.join(SCRIPT_DIR, "sheets")

# Sheet definitions: name, tabs (with CSV mapping), n8n env var key
SHEET_DEFINITIONS = [
    {
        "name": "Epyc Courier - Social Media Content Queue",
        "env_key": "EPYC_CONTENT_QUEUE_SHEET_ID",
        "tabs": [
            {
                "title": "Content Queue",
                "csv": "social-media-content-queue.csv",
            }
        ],
    },
    {
        "name": "Epyc Courier - Lead Tracker",
        "env_key": "EPYC_LEAD_LOG_SHEET_ID",
        "tabs": [
            {
                "title": "Leads",
                "csv": "lead-tracker.csv",
            }
        ],
    },
    {
        "name": "Epyc Courier - Financial Tracker",
        "env_key": "EPYC_FINANCIAL_TRACKER_SHEET_ID",
        "tabs": [
            {
                "title": "Payout Log",
                "csv": "financial-tracker-payout-log.csv",
            },
            {
                "title": "Daily Revenue",
                "csv": "financial-tracker-daily-revenue.csv",
            },
            {
                "title": "Monthly Summary",
                "csv": "financial-tracker-monthly-summary.csv",
            },
        ],
    },
    {
        "name": "Epyc Courier - Operations Tracker",
        "env_key": "EPYC_DISPATCH_LOG_SHEET_ID",
        "tabs": [
            {
                "title": "Deliveries",
                "csv": "operations-deliveries.csv",
            },
            {
                "title": "Daily Reports",
                "csv": "operations-daily-reports.csv",
            },
            {
                "title": "Weekly KPIs",
                "csv": "operations-weekly-kpis.csv",
            },
        ],
    },
]


# --- Authentication ----------------------------------------------------------

def authenticate():
    """Authenticate via OAuth2. Opens browser on first run, caches token."""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired token...")
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"ERROR: {CREDENTIALS_FILE} not found.")
                print("Download OAuth credentials from Google Cloud Console")
                print("and save as credentials.json in this directory.")
                sys.exit(1)
            print("Opening browser for authentication...")
            print("Sign in as admin@epyccs.com and authorize the application.")
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
        print("Token saved for future runs.")

    return creds


# --- CSV Loading -------------------------------------------------------------

def load_csv(filename):
    """Load CSV file and return (headers, rows) where rows is list of lists."""
    filepath = os.path.join(SHEETS_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  WARNING: CSV not found: {filepath}")
        return [], []

    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return [], []

    headers = rows[0]
    data = rows[1:]
    return headers, data


# --- Sheet Creation ----------------------------------------------------------

def create_spreadsheet(sheets_service, name, tab_definitions):
    """
    Create a spreadsheet with the specified tabs.
    Returns the spreadsheet ID and a dict mapping tab titles to sheet IDs.
    """
    sheet_properties = []
    for i, tab in enumerate(tab_definitions):
        sheet_properties.append({
            "properties": {
                "title": tab["title"],
                "index": i,
            }
        })

    body = {
        "properties": {"title": name},
        "sheets": sheet_properties,
    }

    spreadsheet = (
        sheets_service.spreadsheets()
        .create(body=body, fields="spreadsheetId,sheets.properties")
        .execute()
    )

    spreadsheet_id = spreadsheet["spreadsheetId"]
    tab_ids = {}
    for sheet in spreadsheet["sheets"]:
        props = sheet["properties"]
        tab_ids[props["title"]] = props["sheetId"]

    return spreadsheet_id, tab_ids


def populate_tab(sheets_service, spreadsheet_id, tab_title, headers, data):
    """Write headers + data rows into a specific tab."""
    all_rows = [headers] + data if data else [headers]
    range_name = f"'{tab_title}'!A1"

    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body={"values": all_rows},
    ).execute()

    return len(all_rows)


def format_headers(sheets_service, spreadsheet_id, tab_sheet_id, num_columns):
    """Bold the header row and freeze it."""
    requests = [
        # Bold header row
        {
            "repeatCell": {
                "range": {
                    "sheetId": tab_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": num_columns,
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {"bold": True},
                        "backgroundColor": {
                            "red": 0.9,
                            "green": 0.9,
                            "blue": 0.9,
                        },
                    }
                },
                "fields": "userEnteredFormat(textFormat,backgroundColor)",
            }
        },
        # Freeze header row
        {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": tab_sheet_id,
                    "gridProperties": {"frozenRowCount": 1},
                },
                "fields": "gridProperties.frozenRowCount",
            }
        },
        # Auto-resize columns
        {
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": tab_sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": 0,
                    "endIndex": num_columns,
                }
            }
        },
    ]

    sheets_service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={"requests": requests},
    ).execute()


# --- Main --------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  Epyc Courier Service — Google Sheets Automation")
    print("=" * 60)
    print()

    # Authenticate
    creds = authenticate()
    sheets_service = build("sheets", "v4", credentials=creds)
    print()

    # Process each sheet definition
    results = {}

    for defn in SHEET_DEFINITIONS:
        name = defn["name"]
        env_key = defn["env_key"]
        tabs = defn["tabs"]

        print(f"Creating: {name}")
        print(f"  Tabs: {', '.join(t['title'] for t in tabs)}")

        # Create spreadsheet with all tabs
        spreadsheet_id, tab_ids = create_spreadsheet(
            sheets_service, name, tabs
        )
        url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
        print(f"  ID: {spreadsheet_id}")

        # Populate each tab
        for tab in tabs:
            title = tab["title"]
            csv_file = tab["csv"]
            tab_sheet_id = tab_ids[title]

            headers, data = load_csv(csv_file)
            if not headers:
                print(f"  Tab '{title}': No data (CSV missing or empty)")
                continue

            row_count = populate_tab(
                sheets_service, spreadsheet_id, title, headers, data
            )
            data_count = row_count - 1  # subtract header
            print(f"  Tab '{title}': {len(headers)} columns, {data_count} data rows")

            # Format headers
            format_headers(
                sheets_service, spreadsheet_id, tab_sheet_id, len(headers)
            )

        print(f"  URL: {url}")
        print()

        results[env_key] = {
            "spreadsheet_id": spreadsheet_id,
            "url": url,
        }

    # Save results
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Sheet IDs saved to: {OUTPUT_FILE}")
    print()

    # Print summary for n8n
    print("=" * 60)
    print("  n8n Environment Variables")
    print("=" * 60)
    for env_key, info in results.items():
        print(f"  {env_key}={info['spreadsheet_id']}")
    print()
    print("=" * 60)
    print("  Sheet URLs")
    print("=" * 60)
    for env_key, info in results.items():
        print(f"  {info['url']}")
    print()
    print("Done. Open the URLs above to verify your sheets.")


if __name__ == "__main__":
    main()
