# CSV Data System - Complete Guide

## Overview

The SAMCO Egypt Construction Dashboard now uses a **CSV-based data system** that allows you to update all dashboard data weekly without touching any code. Simply update the CSV files and the dashboard automatically loads the new data.

---

## Quick Start

### 1. Update CSV Files
- Navigate to: `data/import_templates/`
- Update each CSV file with your latest data
- Keep file names exactly the same
- Use comma-separated format

### 2. Restart Dashboard
```bash
streamlit run dashboard.py
```

### 3. Dashboard Loads New Data
- All tabs automatically refresh
- Charts and metrics update
- No code changes needed

---

## CSV Files Reference

### 1. **activities.csv** ⭐ MOST IMPORTANT
**Purpose**: Project activities, progress, and costs

**Required Columns**:
```
activity_id          - Unique activity identifier (e.g., A001)
activity_name        - Activity description
wbs_code            - Work Breakdown Structure code
planned_start       - Planned start date (YYYY-MM-DD)
planned_end         - Planned end date (YYYY-MM-DD)
actual_start        - Actual start date (YYYY-MM-DD)
actual_end          - Actual end date (YYYY-MM-DD)
planned_duration    - Planned duration in days
actual_duration     - Actual duration in days
percent_complete    - Progress percentage (0-100)
planned_cost        - Planned cost / BAC
actual_cost         - Actual cost / AC
earned_value        - Earned value / EV
status              - Activity status (Not Started, In Progress, Completed, On Hold)
responsible_party   - Who is responsible
critical_flag       - Is critical path (Yes/No)
```

**Example**:
```csv
activity_id,activity_name,wbs_code,planned_start,planned_end,actual_start,actual_end,planned_duration,actual_duration,percent_complete,planned_cost,actual_cost,earned_value,status,responsible_party,critical_flag
A001,Mobilization,1.1,2025-04-30,2025-05-15,2025-04-30,2025-05-20,15,20,100,500000,550000,500000,Completed,SAMCO,Yes
A002,Site Preparation,1.2,2025-05-16,2025-06-15,2025-05-21,2025-06-20,30,75,75,1000000,750000,750000,In Progress,SAMCO,Yes
```

**Update Frequency**: Weekly

---

### 2. **evm.csv** ⭐ CRITICAL FOR EVM TAB
**Purpose**: Earned Value Management data by period

**Required Columns**:
```
activity_id    - Activity identifier
activity_name  - Activity name
period         - Reporting period (Month/Week, e.g., May-2025)
BAC            - Budget at Completion
AC             - Actual Cost
EV             - Earned Value
PV             - Planned Value
CPI            - Cost Performance Index (EV/AC)
SPI            - Schedule Performance Index (EV/PV)
CV             - Cost Variance (EV-AC)
SV             - Schedule Variance (EV-PV)
```

**Example**:
```csv
activity_id,activity_name,period,BAC,AC,EV,PV,CPI,SPI,CV,SV
A001,Mobilization,May-2025,500000,550000,500000,500000,0.91,1.00,-50000,0
A002,Site Preparation,May-2025,1000000,750000,750000,800000,1.00,0.94,0,-50000
```

**Update Frequency**: Weekly

---

### 3. **progress_updates.csv**
**Purpose**: Weekly progress updates and notes

**Required Columns**:
```
update_id       - Update identifier
activity_id     - Activity identifier
update_date     - Date of update (YYYY-MM-DD)
percent_complete - Current progress (0-100)
notes           - Update notes
issues          - Any issues encountered
```

**Update Frequency**: Weekly

---

### 4. **delay_events.csv**
**Purpose**: Delay events and impacts

**Required Columns**:
```
delay_id        - Delay identifier
activity_id     - Affected activity
delay_date      - Date delay occurred (YYYY-MM-DD)
delay_days      - Number of days delayed
root_cause      - Cause of delay
impact          - Impact on project
status          - Delay status (Open, Closed, Pending)
```

**Update Frequency**: As needed

---

### 5. **risks.csv**
**Purpose**: Project risks and mitigation

**Required Columns**:
```
risk_id         - Risk identifier
risk_title      - Risk title
category        - Risk category (Technical, Schedule, Financial, etc.)
probability     - Probability (1-5)
time_impact_days - Time impact in days
cost_impact     - Cost impact
severity_band   - Severity (Low, Medium, High)
response_strategy - Mitigation strategy
mitigation_status - Status (Open, Mitigated, Closed)
```

**Update Frequency**: Weekly

---

### 6. **payments.csv**
**Purpose**: Payment and invoicing data

**Required Columns**:
```
payment_id      - Payment identifier
invoice_date    - Invoice date (YYYY-MM-DD)
invoice_amount  - Invoice amount
payment_date    - Payment date (YYYY-MM-DD)
payment_amount  - Payment amount
status          - Payment status (Invoiced, Paid, Pending)
```

**Update Frequency**: Weekly

---

### 7. **contracts.csv**
**Purpose**: Contract information

**Required Columns**:
```
contract_id     - Contract identifier
contract_name   - Contract name
contractor      - Contractor name
employer        - Employer name
contract_value  - Contract value
start_date      - Start date (YYYY-MM-DD)
end_date        - End date (YYYY-MM-DD)
status          - Contract status
```

**Update Frequency**: As needed

---

### 8. **milestones.csv**
**Purpose**: Project milestones

**Required Columns**:
```
milestone_id    - Milestone identifier
milestone_name  - Milestone name
planned_date    - Planned date (YYYY-MM-DD)
actual_date     - Actual date (YYYY-MM-DD)
status          - Milestone status (Not Started, In Progress, Completed)
```

**Update Frequency**: Weekly

---

### 9. **change_orders.csv**
**Purpose**: Change orders and variations

**Required Columns**:
```
change_id       - Change order identifier
change_date     - Date of change (YYYY-MM-DD)
description     - Change description
cost_impact     - Cost impact
schedule_impact - Schedule impact (days)
status          - Change status (Proposed, Approved, Implemented)
```

**Update Frequency**: As needed

---

### 10. **cost_items.csv**
**Purpose**: Detailed cost breakdown

**Required Columns**:
```
cost_id         - Cost item identifier
activity_id     - Associated activity
cost_code       - Cost code
description     - Cost description
planned_cost    - Planned cost
actual_cost     - Actual cost
status          - Cost status
```

**Update Frequency**: Weekly

---

### 11. **claims.csv**
**Purpose**: Claims and disputes

**Required Columns**:
```
claim_id        - Claim identifier
claim_date      - Claim date (YYYY-MM-DD)
description     - Claim description
amount          - Claim amount
status          - Claim status
```

**Update Frequency**: As needed

---

### 12. **wbs.csv**
**Purpose**: Work Breakdown Structure

**Required Columns**:
```
wbs_code        - WBS code
wbs_name        - WBS name
parent_code     - Parent WBS code
level           - WBS level
description     - Description
```

**Update Frequency**: As needed

---

## Data Format Rules

### Dates
```
✅ Correct:   2025-05-15
❌ Wrong:     5/15/2025 or 15-May-2025
```

### Numbers
```
✅ Correct:   1000000
❌ Wrong:     1,000,000 or $1,000,000
```

### Percentages
```
✅ Correct:   75 (for 75%)
❌ Wrong:     0.75 or 75%
```

### Status Values
```
✅ Correct:   "In Progress", "Completed", "On Hold"
❌ Wrong:     "in progress", "complete", "hold"
```

### Empty Values
```
✅ Correct:   Leave empty or use 0
❌ Wrong:     "N/A", "null", "None"
```

---

## Weekly Update Workflow

### Step 1: Prepare Data (Monday Morning)
1. Export latest data from your source system
2. Verify all required columns are present
3. Check data format (dates, numbers, status values)
4. Validate no critical fields are empty

### Step 2: Update CSV Files (Monday Morning)
1. Navigate to: `data/import_templates/`
2. Replace each CSV file with updated data
3. Keep file names exactly the same
4. Ensure CSV format (comma-separated)

### Step 3: Refresh Dashboard (Monday Morning)
1. Stop the dashboard (Ctrl+C)
2. Run: `streamlit run dashboard.py`
3. Dashboard automatically loads new data
4. All tabs update with latest information

### Step 4: Verify Data (Monday Morning)
1. Check Overview tab for updated metrics
2. Verify EVM calculations
3. Check for any missing data warnings
4. Review all tabs for accuracy

---

## Data Validation Checklist

Before uploading CSV files, verify:

- ✅ All CSV files present in `data/import_templates/`
- ✅ All required columns present
- ✅ No empty critical fields
- ✅ Dates in correct format (YYYY-MM-DD)
- ✅ Numbers without currency symbols
- ✅ Percentages as decimals (0-100)
- ✅ Status values match expected values
- ✅ No extra spaces in column names
- ✅ File names exactly match expected names
- ✅ CSV format (comma-separated, not semicolon)

---

## Common Issues & Solutions

### Issue: "File not found" error
**Solution**: 
- Ensure CSV file is in `data/import_templates/`
- Check file name matches exactly (case-sensitive)
- Verify file extension is `.csv`

### Issue: "Column not found" error
**Solution**:
- Check CSV has all required columns
- Verify column names match exactly (case-sensitive)
- No extra spaces in column names

### Issue: Missing data in dashboard
**Solution**:
- Verify CSV file has data rows (not just headers)
- Check for empty cells in critical columns
- Verify data format (dates, numbers)

### Issue: Incorrect calculations
**Solution**:
- Verify numeric columns don't have text or symbols
- Check for missing values
- Verify formula dependencies

### Issue: Dashboard won't load new data
**Solution**:
- Check CSV file is saved correctly
- Verify file is in correct directory
- Restart dashboard
- Check browser cache (Ctrl+Shift+Delete)

---

## Data Integration Architecture

```
CSV Files (data/import_templates/)
    ↓
CSV Loaders (csv_loader.py, evm_loader.py)
    ↓
CSV Integration (csv_integration.py)
    ↓
Dashboard (dashboard.py)
    ↓
User Interface
```

### Key Components

**csv_loader.py**
- Loads all CSV files
- Caches data for performance
- Handles missing files gracefully

**evm_loader.py**
- Loads EVM-specific data
- Calculates EVM metrics
- Groups data by activity/period

**csv_integration.py**
- Bridges CSV data and dashboard
- Calculates KPIs
- Provides data transformation

**dashboard.py**
- Displays data in tabs
- Creates charts and metrics
- Refreshes on data changes

---

## Advanced Features

### Automatic Data Refresh
Dashboard checks for file updates every 60 seconds (configurable)

### Data Caching
Loaded data is cached for performance. To force reload:
```python
from src.construction_system.csv_loader import reload_data
reload_data()
```

### Data Status Monitoring
Check which files loaded successfully:
```python
from src.construction_system.csv_integration import get_integration
integration = get_integration()
status = integration.get_data_status()
print(status)
```

---

## Best Practices

### ✅ Do
- Update all files weekly
- Keep consistent column names
- Use standard date format (YYYY-MM-DD)
- Validate data before uploading
- Keep backup of previous week's data
- Document any data changes
- Test with sample data first

### ❌ Don't
- Change column names
- Add extra columns
- Use different date formats
- Include currency symbols
- Leave critical fields empty
- Delete old CSV files
- Mix data formats

---

## Support & Troubleshooting

### Questions?
1. Check this guide
2. Review CSV file examples
3. Check dashboard error messages
4. Review data validation section

### Need Help?
1. Verify CSV format
2. Check column names
3. Review data types
4. Check file locations

---

## File Locations

```
data/import_templates/
├── activities.csv          (Update weekly)
├── evm.csv                 (Update weekly)
├── progress_updates.csv    (Update weekly)
├── delay_events.csv        (Update as needed)
├── risks.csv               (Update weekly)
├── payments.csv            (Update weekly)
├── contracts.csv           (Update as needed)
├── milestones.csv          (Update weekly)
├── change_orders.csv       (Update as needed)
├── cost_items.csv          (Update weekly)
├── claims.csv              (Update as needed)
└── wbs.csv                 (Update as needed)
```

---

## Dashboard Tabs & Data Sources

| Tab | Data Sources | Update Frequency |
|-----|--------------|------------------|
| 📊 Overview | activities, contracts, payments | Weekly |
| 📈 EVM Analysis | evm, activities | Weekly |
| 📋 Contracts | contracts, payments | Weekly |
| ⚠️ Delays | delay_events, activities | As needed |
| 🎯 Risks | risks | Weekly |
| 🎪 Milestones | milestones, change_orders | Weekly |
| ⏳ Time Impact | delay_events, activities | As needed |
| 📉 S-Curve | evm, payments | Weekly |
| ⚖️ Contract Clauses | delay_events, contracts | As needed |

---

## Next Steps

1. **Prepare Your Data**: Export from your source system
2. **Format CSV Files**: Follow the format rules above
3. **Upload Files**: Place in `data/import_templates/`
4. **Restart Dashboard**: Run `streamlit run dashboard.py`
5. **Verify Data**: Check all tabs load correctly

---

## Questions?

Refer to the WEEKLY_UPDATE_GUIDE.md for detailed weekly update procedures.
