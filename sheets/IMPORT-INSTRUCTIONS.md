# Google Sheets Import Instructions

## Quick Import Steps

### Sheet 1: Social Media Content Queue

1. Go to [sheets.google.com](https://sheets.google.com)
2. Create new blank spreadsheet
3. Name it: `Epyc Courier - Social Media Content Queue`
4. File → Import → Upload → Select `social-media-content-queue.csv`
5. Import location: "Replace spreadsheet"
6. Click "Import data"

**Sheet ID needed for n8n:** Copy from URL after `/d/` and before `/edit`

---

### Sheet 2: Lead Tracker

1. Create new blank spreadsheet
2. Name it: `Epyc Courier - Lead Tracker`
3. File → Import → Upload → Select `lead-tracker.csv`
4. Import location: "Replace spreadsheet"

**Sheet ID needed for n8n:** `EPYC_LEAD_LOG_SHEET_ID`

---

### Sheet 3: Financial Tracker

1. Create new blank spreadsheet
2. Name it: `Epyc Courier - Financial Tracker`
3. **Tab 1:** File → Import → Select `financial-tracker-payout-log.csv` → Replace spreadsheet
4. Rename the tab to "Payout Log"
5. **Tab 2:** Click + to add new tab, name it "Daily Revenue"
   - File → Import → Select `financial-tracker-daily-revenue.csv` → Import to current sheet
6. **Tab 3:** Click + to add new tab, name it "Monthly Summary"
   - File → Import → Select `financial-tracker-monthly-summary.csv` → Import to current sheet

**Sheet ID needed for n8n:** `EPYC_FINANCIAL_TRACKER_SHEET_ID`

---

### Sheet 4: Operations Tracker

1. Create new blank spreadsheet
2. Name it: `Epyc Courier - Operations Tracker`
3. **Tab 1:** File → Import → Select `operations-deliveries.csv` → Replace spreadsheet
4. Rename the tab to "Deliveries"
5. **Tab 2:** Click + to add new tab, name it "Daily Reports"
   - File → Import → Select `operations-daily-reports.csv` → Import to current sheet
6. **Tab 3:** Click + to add new tab, name it "Weekly KPIs"
   - File → Import → Select `operations-weekly-kpis.csv` → Import to current sheet

**Sheet IDs needed for n8n:**
- `EPYC_DISPATCH_LOG_SHEET_ID`
- `EPYC_KPI_DASHBOARD_SHEET_ID`
(Can be same sheet, different tabs)

---

## After Import: Record Your Sheet IDs

| Sheet Name | Sheet ID |
|------------|----------|
| Social Media Content Queue | _______________ |
| Lead Tracker | _______________ |
| Financial Tracker | _______________ |
| Operations Tracker | _______________ |

---

## Files Created

```
/sheets/
├── social-media-content-queue.csv     (9 posts pre-loaded)
├── lead-tracker.csv                   (headers only)
├── financial-tracker-payout-log.csv   (headers only)
├── financial-tracker-daily-revenue.csv (headers only)
├── financial-tracker-monthly-summary.csv (headers only)
├── operations-deliveries.csv          (headers only)
├── operations-daily-reports.csv       (headers only)
├── operations-weekly-kpis.csv         (headers only)
└── IMPORT-INSTRUCTIONS.md             (this file)
```

---

## Data Validation (Optional but Recommended)

After import, add these dropdown validations:

### Social Media Content Queue
- Column B (platform): `linkedin`, `facebook`, `instagram`
- Column I (status): `pending`, `posted`, `failed`

### Lead Tracker
- Column P (Qualification): `Hot`, `Warm`, `Cold`
- Column Q (Status): `New`, `Contacted`, `Qualified`, `Proposal`, `Won`, `Lost`

### Operations - Deliveries
- Column I (Status): `Pending`, `Dispatched`, `In Transit`, `Delivered`, `Failed`, `Cancelled`
- Column M (On-Time): `Yes`, `No`

### Operations - Daily Reports
- Column B (Status): `GREEN`, `YELLOW`, `RED`
