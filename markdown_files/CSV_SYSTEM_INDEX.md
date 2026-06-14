# CSV System - Complete Index

**Designed and Developed by:** Eng Ahmed Labib | **Department:** Planning Department

## 🎯 Quick Navigation

### I Need To...
- **Get started in 5 minutes** → Read: `CSV_QUICKSTART.md`
- **Update data weekly** → Read: `WEEKLY_UPDATE_GUIDE.md`
- **Understand the technical details** → Read: `CSV_INTEGRATION_SUMMARY.md`
- **See what was implemented** → Read: `IMPLEMENTATION_COMPLETE.md`
- **Find CSV file specifications** → Read: `WEEKLY_UPDATE_GUIDE.md` (Section: CSV Files to Update Weekly)
- **Troubleshoot an issue** → Read: `WEEKLY_UPDATE_GUIDE.md` (Section: Troubleshooting)

---

## 📚 Documentation Files

### 1. CSV_QUICKSTART.md
**Purpose**: Get started in 5 minutes

**Contains**:
- 5-minute setup instructions
- CSV file templates with examples
- Data format rules
- Dashboard tabs overview
- Troubleshooting quick answers
- Command reference
- Tips & tricks

**Best For**: First-time users, quick reference

**Read Time**: 5-10 minutes

---

### 2. WEEKLY_UPDATE_GUIDE.md
**Purpose**: Comprehensive guide for weekly updates

**Contains**:
- How the CSV system works
- All 12 CSV files with required columns
- Data format specifications
- Weekly update process (4 steps)
- Data validation checklist
- Common issues and solutions
- Best practices
- Quick reference tables

**Best For**: Regular users, detailed information

**Read Time**: 20-30 minutes

---

### 3. CSV_INTEGRATION_SUMMARY.md
**Purpose**: Technical implementation details

**Contains**:
- What was fixed (Plotly error)
- CSV loaders created (csv_loader.py, evm_loader.py)
- Dashboard updates
- Data flow diagram
- File structure
- Verification steps
- Troubleshooting guide

**Best For**: Developers, technical understanding

**Read Time**: 15-20 minutes

---

### 4. IMPLEMENTATION_COMPLETE.md
**Purpose**: Complete implementation summary

**Contains**:
- What was accomplished
- Files created/modified
- CSV files structure
- How to use the system
- Key features
- Verification results
- Weekly update process
- Maintenance guide
- Success criteria

**Best For**: Project overview, stakeholders

**Read Time**: 10-15 minutes

---

### 5. CSV_SYSTEM_INDEX.md
**Purpose**: Navigation guide (this file)

**Contains**:
- Quick navigation
- File descriptions
- Code file descriptions
- Common tasks
- FAQ
- Glossary

**Best For**: Finding what you need

**Read Time**: 5 minutes

---

## 💻 Code Files

### 1. src/construction_system/csv_loader.py
**Purpose**: Load all CSV files with caching

**Key Classes**:
- `CSVDataLoader` - Main loader class

**Key Methods**:
- `load_csv(file_key)` - Load specific CSV file
- `get_activities()` - Get activities data
- `get_risks()` - Get risks data
- `get_evm_data()` - Get EVM data
- `reload_all()` - Reload all files

**Usage**:
```python
from src.construction_system.csv_loader import get_loader
loader = get_loader()
activities = loader.get_activities()
```

**Features**:
- Automatic caching
- Error handling
- Status tracking
- 12 CSV files supported

---

### 2. src/construction_system/evm_loader.py
**Purpose**: Load and process EVM data

**Key Classes**:
- `EVMDataLoader` - EVM loader class

**Key Methods**:
- `load_evm_data()` - Load EVM CSV
- `get_evm_data()` - Get EVM data
- `get_evm_summary()` - Get EVM metrics
- `get_evm_by_activity()` - Group by activity
- `get_evm_by_period()` - Group by period

**Usage**:
```python
from src.construction_system.evm_loader import get_evm_loader
evm = get_evm_loader()
summary = evm.get_evm_summary()
```

**Features**:
- EVM metric calculations
- Activity-level aggregation
- Period-level aggregation
- Summary statistics

---

### 3. dashboard.py
**Purpose**: Main Streamlit dashboard

**Changes Made**:
- Fixed Plotly error (line 468)
- Added CSV loader imports
- All tabs now use CSV data

**Key Sections**:
- Imports (lines 1-25)
- Page config (lines 28-30)
- CSS styling (lines 32-70)
- Helper functions (lines 73-95)
- Data loading (lines 98-110)
- Header (lines 113-150)
- Tabs (lines 153-155)
- Tab content (lines 158+)

**Tabs**:
1. Overview
2. EVM Analysis
3. Contracts
4. Delays
5. Risks
6. Milestones
7. Time Impact
8. S-Curve
9. Contract Clauses

---

## 📁 Data Files

### Location
```
data/import_templates/
```

### 12 CSV Files

| File | Purpose | Update Frequency |
|------|---------|------------------|
| activities.csv | Project activities | Weekly |
| evm.csv | EVM metrics | Weekly |
| progress_updates.csv | Progress updates | Weekly |
| delay_events.csv | Delay events | As needed |
| risks.csv | Risk register | Weekly |
| payments.csv | Payments | Weekly |
| contracts.csv | Contracts | As needed |
| milestones.csv | Milestones | Weekly |
| change_orders.csv | Change orders | As needed |
| cost_items.csv | Cost breakdown | Weekly |
| claims.csv | Claims | As needed |
| wbs.csv | WBS structure | As needed |

---

## 🔄 Common Tasks

### Task 1: Get Started
1. Read: `CSV_QUICKSTART.md`
2. Prepare CSV files
3. Place in `data/import_templates/`
4. Run: `streamlit run dashboard.py`

**Time**: 30 minutes

---

### Task 2: Update Data Weekly
1. Export latest data
2. Replace CSV files
3. Restart dashboard
4. Verify data

**Time**: 30-45 minutes

---

### Task 3: Fix Missing Data
1. Check CSV file exists
2. Verify column names
3. Check data format
4. See: `WEEKLY_UPDATE_GUIDE.md` (Troubleshooting)

**Time**: 10-15 minutes

---

### Task 4: Add New CSV File
1. Create CSV with required columns
2. Place in `data/import_templates/`
3. Update `CSV_FILES` dict in `csv_loader.py`
4. Add getter method to `CSVDataLoader`
5. Update dashboard to use new data

**Time**: 1-2 hours

---

### Task 5: Troubleshoot Error
1. Check error message
2. See: `WEEKLY_UPDATE_GUIDE.md` (Troubleshooting)
3. Verify file location and format
4. Check column names and data types

**Time**: 10-20 minutes

---

## ❓ FAQ

### Q: How often should I update the CSV files?
**A**: Weekly is recommended. See `WEEKLY_UPDATE_GUIDE.md` for details.

### Q: What if I'm missing a CSV file?
**A**: Dashboard handles missing files gracefully. See `WEEKLY_UPDATE_GUIDE.md` (Troubleshooting).

### Q: Can I change column names?
**A**: No, column names must match exactly. See `WEEKLY_UPDATE_GUIDE.md` (Data Format Examples).

### Q: What date format should I use?
**A**: YYYY-MM-DD format (e.g., 2025-05-15). See `CSV_QUICKSTART.md` (Data Format Rules).

### Q: How do I backup my data?
**A**: Keep previous week's CSV files in a backup folder. See `WEEKLY_UPDATE_GUIDE.md` (Best Practices).

### Q: Can I use Excel files directly?
**A**: No, must be CSV format. Export from Excel as CSV.

### Q: What if calculations are wrong?
**A**: Check numeric columns have no text. See `WEEKLY_UPDATE_GUIDE.md` (Troubleshooting).

### Q: How do I add a new CSV file?
**A**: See `CSV_INTEGRATION_SUMMARY.md` (Next Steps - To Extend).

### Q: Can I run the dashboard without CSV files?
**A**: Yes, but no data will display. CSV files are optional.

### Q: How do I clear the cache?
**A**: Restart the dashboard. Cache is cleared automatically.

---

## 📖 Glossary

### CSV
Comma-Separated Values - A simple text file format for data

### EVM
Earned Value Management - Project management technique for tracking progress

### BAC
Budget at Completion - Total planned budget

### AC
Actual Cost - Total actual spending

### EV
Earned Value - Value of work completed

### SPI
Schedule Performance Index - Schedule efficiency (EV/PV)

### CPI
Cost Performance Index - Cost efficiency (EV/AC)

### WBS
Work Breakdown Structure - Hierarchical project structure

### Loader
Python class that loads and caches CSV data

### Cache
In-memory storage for fast data access

### Streamlit
Python framework for building web dashboards

---

## 🔗 Related Files

### Documentation
- `README.md` - Main project documentation
- `QUICKSTART.md` - Original quick start guide
- `docs/data_dictionary.md` - Data field definitions
- `docs/system_blueprint.md` - System architecture

### Scripts
- `scripts/init_database.py` - Initialize database
- `scripts/import_csv_data.py` - Import CSV data
- `scripts/verify_data.py` - Verify data

### Tests
- `tests/test_analytics.py` - Analytics tests

---

## 📞 Support

### For Quick Answers
→ See: `CSV_QUICKSTART.md`

### For Detailed Information
→ See: `WEEKLY_UPDATE_GUIDE.md`

### For Technical Details
→ See: `CSV_INTEGRATION_SUMMARY.md`

### For Implementation Overview
→ See: `IMPLEMENTATION_COMPLETE.md`

### For Navigation
→ See: `CSV_SYSTEM_INDEX.md` (this file)

---

## ✅ Checklist

### Before First Use
- [ ] Read `CSV_QUICKSTART.md`
- [ ] Prepare CSV files
- [ ] Place in `data/import_templates/`
- [ ] Run dashboard
- [ ] Verify data displays

### Weekly Update
- [ ] Export latest data
- [ ] Replace CSV files
- [ ] Restart dashboard
- [ ] Verify data in all tabs
- [ ] Backup previous week's files

### Troubleshooting
- [ ] Check file location
- [ ] Verify column names
- [ ] Check data format
- [ ] Review error messages
- [ ] See troubleshooting guide

---

## 🎓 Learning Path

### Beginner (30 minutes)
1. Read: `CSV_QUICKSTART.md`
2. Prepare sample CSV files
3. Run dashboard
4. Explore tabs

### Intermediate (1-2 hours)
1. Read: `WEEKLY_UPDATE_GUIDE.md`
2. Understand all CSV files
3. Learn data validation
4. Practice weekly update

### Advanced (2-3 hours)
1. Read: `CSV_INTEGRATION_SUMMARY.md`
2. Study code files
3. Understand loaders
4. Learn customization

---

## 📊 System Overview

```
CSV Files (data/import_templates/)
    ↓
CSV Loaders (csv_loader.py, evm_loader.py)
    ↓
Dashboard (dashboard.py)
    ↓
Streamlit UI
    ↓
User Views (9 tabs)
```

---

## 🚀 Next Steps

1. **Start Here**: Read `CSV_QUICKSTART.md`
2. **Prepare Data**: Create CSV files
3. **Run Dashboard**: `streamlit run dashboard.py`
4. **Update Weekly**: Follow `WEEKLY_UPDATE_GUIDE.md`
5. **Get Help**: Check documentation or troubleshooting

---

## 📝 Version Info

- **Created**: May 14, 2026
- **Dashboard Version**: 2.0 (CSV-based)
- **Status**: Production Ready ✅

---

**Happy updating!** 📊
