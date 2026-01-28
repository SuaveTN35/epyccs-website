# EPYC COURIER SERVICE — Google Sheets Setup Guide

**Created:** 2026-01-26
**Status:** Ready for Implementation

---

## OVERVIEW

You need to create **4 Google Sheets** to power the Epyc Courier automation system:

| Sheet | Purpose | n8n Environment Variable |
|-------|---------|--------------------------|
| Social Media Content Queue | Automated social posting | `EPYC_SOCIAL_CONTENT_SHEET_ID` |
| Lead Tracker | Lead capture and CRM | `EPYC_LEAD_LOG_SHEET_ID` |
| Financial Tracker | Stripe payout monitoring | `EPYC_FINANCIAL_TRACKER_SHEET_ID` |
| Operations Tracker | Dispatch + KPI dashboard | `EPYC_DISPATCH_LOG_SHEET_ID` + `EPYC_KPI_DASHBOARD_SHEET_ID` |

---

## SHEET 1: Social Media Content Queue

**Name:** `Epyc Courier - Social Media Content Queue`

### Tab: Sheet1 (or rename to "Content Queue")

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `id` | Number | Unique ID (1, 2, 3...) |
| B | `platform` | Text | `linkedin`, `facebook`, or `instagram` |
| C | `post_date` | Date (YYYY-MM-DD) | Scheduled date |
| D | `post_time` | Text (HH:MM) | Scheduled time in 24hr format |
| E | `content` | Text | The post text |
| F | `image_url` | URL | URL to image (required for Instagram) |
| G | `link_url` | URL | URL to include in post |
| H | `hashtags` | Text | Hashtags to append |
| I | `status` | Text | `pending`, `posted`, or `failed` |
| J | `posted_at` | DateTime | Timestamp when posted (filled by n8n) |
| K | `post_id` | Text | Platform post ID (filled by n8n) |
| L | `notes` | Text | Any notes |

### Initial Data (Copy from CSV)

Your 9 posts are already prepared in: `epyc-social-media-content-queue.csv`

Copy this data into the sheet after creating columns.

### Data Validation Rules

- Column B (platform): Dropdown with values: `linkedin`, `facebook`, `instagram`
- Column I (status): Dropdown with values: `pending`, `posted`, `failed`

---

## SHEET 2: Lead Tracker

**Name:** `Epyc Courier - Lead Tracker`

### Tab: Leads

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `Timestamp` | DateTime | When lead was received |
| B | `Name` | Text | Full name |
| C | `Email` | Email | Email address |
| D | `Phone` | Text | Phone number |
| E | `Company` | Text | Company name |
| F | `Service Interest` | Text | Service type requested |
| G | `Urgency` | Text | STAT, Rush, Same-Day, Scheduled |
| H | `Pickup Address` | Text | Pickup location |
| I | `Pickup City` | Text | Pickup city |
| J | `Delivery Address` | Text | Delivery location |
| K | `Delivery City` | Text | Delivery city |
| L | `Package Type` | Text | Package description |
| M | `Message` | Text | Additional notes |
| N | `Source` | Text | Lead source (Website, Referral, etc.) |
| O | `Lead Score` | Number | Calculated score (0-100) |
| P | `Qualification` | Text | Hot, Warm, or Cold |
| Q | `Status` | Text | New, Contacted, Qualified, Proposal, Won, Lost |
| R | `Assigned To` | Text | Sales rep name |
| S | `Follow-Up Date` | Date | Next action date |
| T | `Notes` | Text | Internal notes |

### Data Validation Rules

- Column P (Qualification): Dropdown: `Hot`, `Warm`, `Cold`
- Column Q (Status): Dropdown: `New`, `Contacted`, `Qualified`, `Proposal`, `Won`, `Lost`

### Conditional Formatting

- Hot leads (Column P = "Hot"): Highlight row in light red/pink
- Won deals (Column Q = "Won"): Highlight row in light green

---

## SHEET 3: Financial Tracker

**Name:** `Epyc Courier - Financial Tracker`

### Tab 1: Payout Log

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `Timestamp` | DateTime | When logged |
| B | `Account` | Text | DispatchIt or Direct Clients |
| C | `Payout ID` | Text | Stripe payout ID |
| D | `Amount` | Currency | Payout amount (e.g., $1,234.56) |
| E | `Status` | Text | pending, in_transit, paid, failed |
| F | `Created` | DateTime | When payout was created |
| G | `Arrival Date` | DateTime | Expected arrival date |
| H | `Method` | Text | standard or instant |
| I | `Failure Code` | Text | If failed, the error code |
| J | `Failure Message` | Text | If failed, the error message |

### Tab 2: Daily Revenue

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `Date` | Date | Revenue date |
| B | `DispatchIt Revenue` | Currency | Revenue from DispatchIt |
| C | `Direct Revenue` | Currency | Revenue from direct clients |
| D | `Total Revenue` | Currency | =B+C |
| E | `Delivery Count` | Number | Number of deliveries |
| F | `Average per Delivery` | Currency | =D/E |
| G | `Notes` | Text | Any notes |

### Tab 3: Monthly Summary

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `Month` | Text | YYYY-MM |
| B | `Total Revenue` | Currency | Monthly total |
| C | `Total Payouts` | Currency | Amount received |
| D | `Pending` | Currency | Still pending |
| E | `Delivery Count` | Number | Total deliveries |
| F | `Average Revenue/Delivery` | Currency | =B/E |
| G | `MoM Growth` | Percentage | Month over month |

---

## SHEET 4: Operations Tracker

**Name:** `Epyc Courier - Operations Tracker`

### Tab 1: Deliveries (Dispatch Log)

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `ID` | Number | Delivery ID |
| B | `Date` | Date | Delivery date |
| C | `Client` | Text | Client name |
| D | `Service Type` | Text | Medical, Legal, Commercial, etc. |
| E | `Pickup Address` | Text | Full pickup address |
| F | `Delivery Address` | Text | Full delivery address |
| G | `Scheduled Date` | Date | Scheduled delivery date |
| H | `Scheduled Time` | Text | Scheduled time window |
| I | `Status` | Text | Pending, In Transit, Delivered, Failed |
| J | `Driver` | Text | Assigned driver |
| K | `Dispatched At` | DateTime | When dispatched |
| L | `Completed At` | DateTime | When delivered |
| M | `On-Time` | Text | Yes/No |
| N | `Revenue` | Currency | Delivery revenue |
| O | `Notes` | Text | Any notes |

### Tab 2: Daily Reports (KPI Dashboard)

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `Date` | Date | Report date |
| B | `Status` | Text | GREEN, YELLOW, or RED |
| C | `Website` | Text | OPERATIONAL or DOWN |
| D | `Stripe Available` | Currency | Available balance |
| E | `Stripe Pending` | Currency | Pending balance |
| F | `Scheduled Deliveries` | Number | Deliveries scheduled today |
| G | `Pending Deliveries` | Number | Deliveries pending |
| H | `Completed Deliveries` | Number | Deliveries completed |
| I | `On-Time Rate` | Percentage | % delivered on time |
| J | `Revenue Today` | Currency | Day's revenue |
| K | `Alerts` | Text | Any alerts (semicolon separated) |

### Tab 3: Weekly KPIs

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | `Week` | Text | YYYY-WW |
| B | `Total Deliveries` | Number | Week's total |
| C | `On-Time Deliveries` | Number | Delivered on time |
| D | `On-Time Rate` | Percentage | =C/B |
| E | `Total Revenue` | Currency | Week's revenue |
| F | `New Leads` | Number | Leads received |
| G | `Leads Converted` | Number | Leads won |
| H | `Conversion Rate` | Percentage | =G/F |

### Data Validation Rules

- Status (Deliveries): Dropdown: `Pending`, `Dispatched`, `In Transit`, `Delivered`, `Failed`, `Cancelled`
- Status (Daily Reports): Dropdown: `GREEN`, `YELLOW`, `RED`
- On-Time: Dropdown: `Yes`, `No`

### Conditional Formatting

- RED status: Highlight row in light red
- YELLOW status: Highlight row in light yellow
- On-Time = "No": Highlight cell in light red

---

## SETUP INSTRUCTIONS

### Step 1: Create the Sheets

1. Go to [sheets.google.com](https://sheets.google.com)
2. Click "+" to create a new blank spreadsheet
3. Name it according to the sheet name above
4. Create the tabs as specified
5. Add the column headers in Row 1
6. Apply data validation rules where specified
7. Apply conditional formatting where specified

### Step 2: Get Sheet IDs

After creating each sheet:
1. Open the sheet
2. Look at the URL: `https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit`
3. Copy the SHEET_ID_HERE portion
4. Save it for n8n configuration

### Step 3: Share with n8n Service Account

If using n8n Cloud with Google OAuth:
1. You'll authenticate directly through n8n
2. No manual sharing needed

If using n8n self-hosted with Service Account:
1. Create a service account in Google Cloud Console
2. Download the JSON key file
3. Share each Google Sheet with the service account email (found in JSON)
4. Give "Editor" permissions

### Step 4: Configure n8n Environment Variables

In your n8n instance, set these environment variables:

```
EPYC_SOCIAL_CONTENT_SHEET_ID=your_sheet_id_here
EPYC_LEAD_LOG_SHEET_ID=your_sheet_id_here
EPYC_FINANCIAL_TRACKER_SHEET_ID=your_sheet_id_here
EPYC_DISPATCH_LOG_SHEET_ID=your_sheet_id_here
EPYC_KPI_DASHBOARD_SHEET_ID=your_sheet_id_here
```

Note: DISPATCH_LOG and KPI_DASHBOARD can be the same sheet (Operations Tracker) with different tabs.

---

## QUICK COPY-PASTE HEADERS

### Social Media Content Queue
```
id	platform	post_date	post_time	content	image_url	link_url	hashtags	status	posted_at	post_id	notes
```

### Lead Tracker
```
Timestamp	Name	Email	Phone	Company	Service Interest	Urgency	Pickup Address	Pickup City	Delivery Address	Delivery City	Package Type	Message	Source	Lead Score	Qualification	Status	Assigned To	Follow-Up Date	Notes
```

### Financial Tracker - Payout Log
```
Timestamp	Account	Payout ID	Amount	Status	Created	Arrival Date	Method	Failure Code	Failure Message
```

### Financial Tracker - Daily Revenue
```
Date	DispatchIt Revenue	Direct Revenue	Total Revenue	Delivery Count	Average per Delivery	Notes
```

### Operations Tracker - Deliveries
```
ID	Date	Client	Service Type	Pickup Address	Delivery Address	Scheduled Date	Scheduled Time	Status	Driver	Dispatched At	Completed At	On-Time	Revenue	Notes
```

### Operations Tracker - Daily Reports
```
Date	Status	Website	Stripe Available	Stripe Pending	Scheduled Deliveries	Pending Deliveries	Completed Deliveries	On-Time Rate	Revenue Today	Alerts
```

---

## VERIFICATION CHECKLIST

After creating all sheets:

- [ ] Social Media Content Queue created with correct columns
- [ ] 9 posts loaded from CSV
- [ ] Lead Tracker created with Leads tab
- [ ] Financial Tracker created with Payout Log, Daily Revenue, Monthly Summary tabs
- [ ] Operations Tracker created with Deliveries, Daily Reports, Weekly KPIs tabs
- [ ] All Sheet IDs recorded
- [ ] Sheets shared with n8n (if using service account)
- [ ] Environment variables configured in n8n

---

*Document Generated: 2026-01-26*
*Agent: EPYC-COURIER (Captain O-3)*
