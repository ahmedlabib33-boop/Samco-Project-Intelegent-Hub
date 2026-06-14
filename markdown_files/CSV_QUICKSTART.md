# CSV System Quick Start

**Designed and Developed by:** Eng Ahmed Labib | **Department:** Planning Department

## 5-Minute Setup

### Step 1: Prepare Your Data
Export your project data into CSV files with these names:
- `activities.csv`
- `evm.csv`
- `progress_updates.csv`
- `delay_events.csv`
- `risks.csv`
- `payments.csv`
- `contracts.csv`
- `milestones.csv`
- `change_orders.csv`
- `cost_items.csv`
- `claims.csv`
- `wbs.csv`

### Step 2: Place Files
Copy all CSV files to:
```
data/import_templates/
```

### Step 3: Start Dashboard
```bash
streamlit run dashboard.py
```

### Step 4: View Data
Dashboard automatically loads all CSV data and displays it in tabs.

---

## Weekly Update (30 minutes)

### Every Monday Morning
1. Export latest data from your system
2. Replace CSV files in `data/import_templates/`
3. Restart dashboard: `streamlit run dashboard.py`
4. Verify data in all tabs

---

## CSV File Templates

### activities.csv
```csv
activity_id,activity_name,wbs_code,planned_start,planned_end,actual_start,actual_end,planned_duration,actual_duration,percent_complete,planned_cost,actual_cost,earned_value,status,responsible_party,critical_flag
A001,Mobilization,1.1,2025-04-30,2025-05-15,2025-04-30,2025-05-20,15,20,100,500000,550000,500000,Completed,SAMCO,Yes
A002,Site Prep,1.2,2025-05-16,2025-06-15,2025-05-21,2025-06-20,30,30,75,1000000,750000,750000,In Progress,SAMCO,Yes
```

### evm.csv
```csv
activity_id,period,BAC,AC,EV,PV,CPI,SPI,CV,SV
A001,May-2025,500000,550000,500000,500000,0.91,1.00,-50000,0
A002,May-2025,1000000,750000,750000,800000,1.00,0.94,0,50000
```

### risks.csv
```csv
risk_id,risk_description,category,probability,impact,severity,mitigation,status
R001,Material Delay,Schedule,4,5,High,Backup supplier,Open
R002,Weather Impact,External,3,4,Medium,Schedule buffer,Open
```

### payments.csv
```csv
payment_id,invoice_date,invoice_amount,payment_date,payment_amount,status
P001,2025-05-01,100000,2025-05-15,100000,Paid
P002,2025-05-15,150000,2025-05-30,150000,Paid
```

### contracts.csv
```csv
contract_id,contract_name,contractor,employer,contract_value,start_date,end_date,status
C001,Main Contract,SAMCO,Roya,367300000,2025-04-30,2026-11-30,Active
```

### milestones.csv
```csv
milestone_id,milestone_name,planned_date,actual_date,status
M001,Mobilization Complete,2025-05-15,2025-05-20,Completed
M002,Foundation Complete,2025-08-15,,In Progress
```

### delay_events.csv
```csv
delay_id,activity_id,delay_date,delay_days,root_cause,impact,status
D001,A001,2025-05-20,5,Material Delay,Schedule Slip,Open
```

### change_orders.csv
```csv
change_id,change_date,description,cost_impact,schedule_impact,status
CO001,2025-05-15,Design Change,50000,5,Approved
```

### cost_items.csv
```csv
cost_id,activity_id,cost_code,description,planned_cost,actual_cost,status
CI001,A001,1.1.1,Labor,300000,320000,In Progress
```

### progress_updates.csv
```csv
update_id,activity_id,update_date,percent_complete,notes,issues
U001,A001,2025-05-20,100,Completed on time,None
U002,A002,2025-05-20,75,On track,Material delay expected
```

### claims.csv
```csv
claim_id,activity_id,claim_date,claim_amount,description,status
CL001,A001,2025-05-20,50000,Delay Claim,Submitted
```

### wbs.csv
```csv
wbs_id,wbs_code,wbs_name,parent_code,level,planned_cost,actual_cost
WBS001,1,Mobilization,,1,500000,550000
WBS002,1.1,Site Setup,1,2,300000,320000
```

---

## Data Format Rules

### Dates
- Format: `YYYY-MM-DD`
- Example: `2025-05-15`

### Numbers
- No commas: `1000000` not `1,000,000`
- No currency: `500000` not `$500,000`
- Decimals: `0.95` for percentages

### Percentages
- Use 0-100: `75` for 75%
- Not decimals: `75` not `0.75`

### Status Values
- Use exact case: `In Progress`, `Completed`, `On Hold`
- Not lowercase: `in progress` won't work

---

## Dashboard Tabs

| Tab | Data Source | Purpose |
|-----|-------------|---------|
| 📊 Overview | activities, contracts, payments | Project summary |
| 📈 EVM Analysis | evm, activities | Earned value metrics |
| 📋 Contracts | contracts, payments | Contract management |
| ⚠️ Delays | delay_events, activities | Delay tracking |
| 🎯 Risks | risks | Risk register |
| 🎪 Milestones | milestones, change_orders | Milestones & changes |
| ⏳ Time Impact | delay_events, activities | Schedule impact |
| 📉 S-Curve | evm, payments | Financial progress |
| ⚖️ Contract Clauses | delay_events, contracts | Clause matching |

---

## Troubleshooting

### "File not found" Error
- Check file is in `data/import_templates/`
- Check file name is exactly correct
- Check file is saved as CSV

### "Column not found" Error
- Check column names match exactly
- Check for extra spaces in names
- Check capitalization

### No Data Showing
- Check CSV file has data rows
- Check file is not empty
- Check file format is correct

### Dashboard Won't Start
- Check Python version: `python --version`
- Check dependencies: `pip install -r requirements.txt`
- Check syntax: `python -m py_compile dashboard.py`

---

## Command Reference

### Start Dashboard
```bash
streamlit run dashboard.py
```

### Check Syntax
```bash
python -m py_compile dashboard.py
```

### Test Loaders
```bash
python -c "from src.construction_system.csv_loader import get_loader; print('OK')"
```

### View CSV Status
```bash
python -c "from src.construction_system.csv_loader import get_loader; loader = get_loader(); loader.reload_all(); print(loader.get_load_status())"
```

---

## Tips & Tricks

### Backup Your Data
Keep previous week's CSV files:
```
data/import_templates/backup/
├── activities_2025-05-14.csv
├── evm_2025-05-14.csv
└── ...
```

### Validate Before Upload
1. Open CSV in Excel
2. Check all columns present
3. Check no empty critical cells
4. Check data types correct
5. Save as CSV

### Monitor Updates
Check load status:
```python
from src.construction_system.csv_loader import get_loader
loader = get_loader()
loader.reload_all()
print(loader.get_load_status())
```

### Clear Cache
Force reload all data:
```python
from src.construction_system.csv_loader import reload_data
reload_data()
```

---

## Common Mistakes

### ❌ Don't
- Change column names
- Add extra columns
- Use different date formats
- Include currency symbols
- Leave critical fields empty
- Use lowercase status values

### ✅ Do
- Keep column names exact
- Use standard formats
- Validate before uploading
- Update weekly
- Keep backups
- Document changes

---

## Support

### Need Help?
1. Check `WEEKLY_UPDATE_GUIDE.md` for detailed info
2. Review CSV file examples above
3. Check dashboard error messages
4. Verify file locations and formats

### Questions?
- How often to update? **Weekly**
- Where to put files? **data/import_templates/**
- What format? **CSV (comma-separated)**
- Can I add columns? **No, use exact columns**
- Can I skip files? **Yes, dashboard handles missing files**

---

## Next Steps

1. ✅ Prepare your CSV files
2. ✅ Place in `data/import_templates/`
3. ✅ Run `streamlit run dashboard.py`
4. ✅ View your data in dashboard
5. ✅ Update weekly with new data

**You're ready to go!** 🚀
