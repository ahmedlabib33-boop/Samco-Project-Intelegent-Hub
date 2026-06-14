# Weekly Data Update Guide

**Designed and Developed by:** Eng Ahmed Labib | **Department:** Planning Department

## Overview

The SAMCO Egypt Construction Dashboard now loads all data from CSV files, making weekly updates simple and straightforward.

---

## How It Works

### Data Flow
```
CSV Files (data/import_templates/)
    ↓
CSV Loaders (csv_loader.py, evm_loader.py)
    ↓
Dashboard (dashboard.py)
    ↓
User Interface
```

### Key Features
- ✅ All data from CSV files (no hardcoded data)
- ✅ Automatic caching for performance
- ✅ Easy weekly updates
- ✅ Handles missing data gracefully
- ✅ Real-time data refresh

---

## CSV Files to Update Weekly

### 1. **activities.csv** (Most Important)
**Purpose**: Project activities, progress, and costs

**Required Columns**:
- `activity_id` - Unique activity identifier
- `activity_name` - Activity description
- `wbs_code` - Work Breakdown Structure code
- `planned_start` - Planned start date
- `planned_end` - Planned end date
- `actual_start` - Actual start date
- `actual_end` - Actual end date
- `planned_duration` - Planned duration (days)
- `actual_duration` - Actual duration (days)
- `percent_complete` - Progress percentage (0-100)
- `planned_cost` - Planned cost (BAC)
- `actual_cost` - Actual cost (AC)
- `earned_value` - Earned value (EV)
- `status` - Activity status (Not Started, In Progress, Completed, On Hold)
- `responsible_party` - Who is responsible
- `critical_flag` - Is critical path (Yes/No)

**Update Frequency**: Weekly

**Example**:
```csv
activity_id,activity_name,wbs_code,planned_start,planned_end,actual_start,actual_end,planned_duration,actual_duration,percent_complete,planned_cost,actual_cost,earned_value,status,responsible_party,critical_flag
A001,Mobilization,1.1,2025-04-30,2025-05-15,2025-04-30,2025-05-20,15,20,100,500000,550000,500000,Completed,SAMCO,Yes
A002,Site Preparation,1.2,2025-05-16,2025-06-15,2025-05-21,2025-06-20,30,30,75,1000000,750000,750000,In Progress,SAMCO,Yes
```

### 2. **evm.csv** (Critical for EVM Tab)
**Purpose**: Earned Value Management data

**Required Columns**:
- `activity_id` - Activity identifier
- `period` - Reporting period (Month/Week)
- `BAC` - Budget at Completion
- `AC` - Actual Cost
- `EV` - Earned Value
- `PV` - Planned Value
- `CPI` - Cost Performance Index (calculated)
- `SPI` - Schedule Performance Index (calculated)
- `CV` - Cost Variance (calculated)
- `SV` - Schedule Variance (calculated)

**Update Frequency**: Weekly

**Example**:
```csv
activity_id,period,BAC,AC,EV,PV,CPI,SPI,CV,SV
A001,May-2025,500000,550000,500000,500000,0.91,1.00,-50000,0
A002,May-2025,1000000,750000,750000,800000,1.00,0.94,-0,50000
```

### 3. **progress_updates.csv**
**Purpose**: Weekly progress updates

**Required Columns**:
- `update_id` - Update identifier
- `activity_id` - Activity identifier
- `update_date` - Date of update
- `percent_complete` - Current progress
- `notes` - Update notes
- `issues` - Any issues encountered

**Update Frequency**: Weekly

### 4. **delay_events.csv**
**Purpose**: Delay events and impacts

**Required Columns**:
- `delay_id` - Delay identifier
- `activity_id` - Affected activity
- `delay_date` - Date delay occurred
- `delay_days` - Number of days delayed
- `root_cause` - Cause of delay
- `impact` - Impact on project
- `status` - Delay status (Open, Closed, Pending)

**Update Frequency**: As needed

### 5. **risks.csv**
**Purpose**: Project risks and mitigation

**Required Columns**:
- `risk_id` - Risk identifier
- `risk_description` - Risk description
- `category` - Risk category (Technical, Schedule, Financial, etc.)
- `probability` - Probability (1-5)
- `impact` - Impact (1-5)
- `severity` - Severity (Low, Medium, High)
- `mitigation` - Mitigation strategy
- `status` - Risk status (Open, Mitigated, Closed)

**Update Frequency**: Weekly

### 6. **payments.csv**
**Purpose**: Payment and invoicing data

**Required Columns**:
- `payment_id` - Payment identifier
- `invoice_date` - Invoice date
- `invoice_amount` - Invoice amount
- `payment_date` - Payment date
- `payment_amount` - Payment amount
- `status` - Payment status (Invoiced, Paid, Pending)

**Update Frequency**: Weekly

### 7. **contracts.csv**
**Purpose**: Contract information

**Required Columns**:
- `contract_id` - Contract identifier
- `contract_name` - Contract name
- `contractor` - Contractor name
- `employer` - Employer name
- `contract_value` - Contract value
- `start_date` - Start date
- `end_date` - End date
- `status` - Contract status

**Update Frequency**: As needed

### 8. **milestones.csv**
**Purpose**: Project milestones

**Required Columns**:
- `milestone_id` - Milestone identifier
- `milestone_name` - Milestone name
- `planned_date` - Planned date
- `actual_date` - Actual date
- `status` - Milestone status (Not Started, In Progress, Completed)

**Update Frequency**: Weekly

### 9. **change_orders.csv**
**Purpose**: Change orders and variations

**Required Columns**:
- `change_id` - Change order identifier
- `change_date` - Date of change
- `description` - Change description
- `cost_impact` - Cost impact
- `schedule_impact` - Schedule impact (days)
- `status` - Change status (Proposed, Approved, Implemented)

**Update Frequency**: As needed

### 10. **cost_items.csv**
**Purpose**: Detailed cost breakdown

**Required Columns**:
- `cost_id` - Cost item identifier
- `activity_id` - Associated activity
- `cost_code` - Cost code
- `description` - Cost description
- `planned_cost` - Planned cost
- `actual_cost` - Actual cost
- `status` - Cost status

**Update Frequency**: Weekly

---

## Weekly Update Process

### Step 1: Prepare Data
1. Open your data source (Excel, database, etc.)
2. Export latest data for each CSV file
3. Ensure all required columns are present
4. Validate data (no missing critical values)

### Step 2: Update CSV Files
1. Navigate to: `data/import_templates/`
2. Replace each CSV file with updated data
3. Keep file names exactly the same
4. Ensure CSV format (comma-separated)

### Step 3: Refresh Dashboard
1. Stop the dashboard (Ctrl+C)
2. Run: `streamlit run dashboard.py`
3. Dashboard automatically loads new data
4. All tabs update with latest information

### Step 4: Verify Data
1. Check Overview tab for updated metrics
2. Verify EVM calculations
3. Check for any missing data warnings
4. Review all tabs for accuracy

---

## Data Validation

### Required Data Checks
- ✅ All CSV files present in `data/import_templates/`
- ✅ All required columns present
- ✅ No empty critical fields
- ✅ Dates in correct format (YYYY-MM-DD)
- ✅ Numbers without currency symbols
- ✅ Percentages as decimals (0-100)

### Common Issues

**Issue**: "File not found" error
- **Solution**: Ensure CSV file is in `data/import_templates/` with correct name

**Issue**: "Column not found" error
- **Solution**: Check CSV has all required columns with exact names

**Issue**: Missing data in dashboard
- **Solution**: Verify CSV file has data rows (not just headers)

**Issue**: Incorrect calculations
- **Solution**: Verify numeric columns don't have text or symbols

---

## Data Format Examples

### Dates
```
Correct: 2025-05-15
Incorrect: 5/15/2025 or 15-May-2025
```

### Numbers
```
Correct: 1000000
Incorrect: 1,000,000 or $1,000,000
```

### Percentages
```
Correct: 75 (for 75%)
Incorrect: 0.75 or 75%
```

### Status Values
```
Correct: "In Progress", "Completed", "On Hold"
Incorrect: "in progress", "complete", "hold"
```

---

## Automated Data Refresh

### Option 1: Manual Refresh
1. Update CSV files
2. Restart dashboard
3. Data automatically loads

### Option 2: Scheduled Refresh (Advanced)
Add to your system:
```bash
# Update every Monday at 8 AM
0 8 * * 1 /path/to/update_data.sh
```

### Option 3: Real-time Monitoring
Dashboard checks for file updates every 60 seconds (configurable)

---

## Troubleshooting

### Dashboard Won't Load New Data
1. Check CSV file is saved correctly
2. Verify file is in correct directory
3. Restart dashboard
4. Check browser cache (Ctrl+Shift+Delete)

### Missing Data in Tabs
1. Verify CSV file has data
2. Check column names match exactly
3. Look for error messages in console
4. Check data format (dates, numbers)

### Calculations Incorrect
1. Verify numeric columns have no text
2. Check for missing values
3. Verify formula dependencies
4. Review EVM calculations

---

## Best Practices

### ✅ Do
- Update all files weekly
- Keep consistent column names
- Use standard date format (YYYY-MM-DD)
- Validate data before uploading
- Keep backup of previous week's data
- Document any data changes

### ❌ Don't
- Change column names
- Add extra columns
- Use different date formats
- Include currency symbols
- Leave critical fields empty
- Delete old CSV files

---

## Quick Reference

### File Locations
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

### Update Frequency
- **Weekly**: activities, evm, progress_updates, risks, payments, milestones, cost_items
- **As Needed**: delay_events, contracts, change_orders, claims, wbs

### Dashboard Tabs
1. 📊 Overview - Uses: activities, contracts, payments
2. 📈 EVM Analysis - Uses: evm, activities
3. 📋 Contracts - Uses: contracts, payments
4. ⚠️ Delays - Uses: delay_events, activities
5. 🎯 Risks - Uses: risks
6. 🎪 Milestones - Uses: milestones, change_orders
7. ⏳ Time Impact - Uses: delay_events, activities
8. 📉 S-Curve - Uses: evm, payments
9. ⚖️ Contract Clauses - Uses: delay_events, contracts

---

## Support

### Questions?
1. Check this guide
2. Review CSV file examples
3. Check dashboard error messages
4. Review data validation section

### Need Help?
- Verify CSV format
- Check column names
- Review data types
- Check file locations
