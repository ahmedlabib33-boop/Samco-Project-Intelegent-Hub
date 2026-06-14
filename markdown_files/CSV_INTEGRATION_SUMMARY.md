# CSV Integration Summary

**Designed and Developed by:** Eng Ahmed Labib | **Department:** Planning Department

## What Was Done

### 1. Fixed Plotly Error
**Issue**: `ValueError: Cannot accept list of column references or list of columns for both x and y`

**Root Cause**: The dashboard was using `px.bar(x=category_counts.index, y=category_counts.values)` which Plotly Express doesn't accept.

**Solution**: Updated to use a DataFrame approach:
```python
df_category = pd.DataFrame({"Category": category_counts.index, "Count": category_counts.values})
fig = px.bar(df_category, x="Category", y="Count", title="Risk Category")
```

**Location**: `dashboard.py` line 468 (Risk Category Distribution chart)

---

### 2. Created CSV Data Loaders

#### **csv_loader.py**
A comprehensive CSV data loader that:
- Loads all 12 CSV files from `data/import_templates/`
- Implements caching for performance
- Handles missing files gracefully
- Provides individual getter methods for each data type
- Tracks load status for debugging

**Features**:
- Automatic file discovery
- Error handling
- Caching mechanism
- Status reporting

**Usage**:
```python
from src.construction_system.csv_loader import get_loader

loader = get_loader()
activities = loader.get_activities()
risks = loader.get_risks()
```

#### **evm_loader.py**
A specialized EVM data loader that:
- Loads EVM data from `evm.csv`
- Calculates EVM metrics (CPI, SPI, CV, SV)
- Groups data by activity or period
- Provides summary statistics

**Features**:
- EVM metric calculations
- Activity-level aggregation
- Period-level aggregation
- Summary statistics

**Usage**:
```python
from src.construction_system.evm_loader import get_evm_loader

evm_loader = get_evm_loader()
evm_data = evm_loader.get_evm_data()
summary = evm_loader.get_evm_summary()
```

---

### 3. Updated Dashboard Imports
Added imports for the new CSV loaders:
```python
from src.construction_system.csv_loader import get_loader as get_csv_loader
from src.construction_system.evm_loader import get_evm_loader
```

---

### 4. Created Weekly Update Guide
**File**: `WEEKLY_UPDATE_GUIDE.md`

Comprehensive guide covering:
- How the CSV system works
- All 12 CSV files with required columns
- Weekly update process (4 steps)
- Data validation checklist
- Data format examples
- Troubleshooting guide
- Best practices
- Quick reference

---

## CSV Files Structure

### Location
```
data/import_templates/
```

### Files (12 total)
1. **activities.csv** - Project activities and progress
2. **evm.csv** - Earned Value Management data
3. **progress_updates.csv** - Weekly progress updates
4. **delay_events.csv** - Delay events and impacts
5. **risks.csv** - Project risks
6. **payments.csv** - Payment and invoicing
7. **contracts.csv** - Contract information
8. **milestones.csv** - Project milestones
9. **change_orders.csv** - Change orders
10. **cost_items.csv** - Cost breakdown
11. **claims.csv** - Claims data
12. **wbs.csv** - Work Breakdown Structure

---

## Weekly Update Process

### Quick Steps
1. **Prepare**: Export latest data from your source
2. **Update**: Replace CSV files in `data/import_templates/`
3. **Refresh**: Restart the dashboard
4. **Verify**: Check all tabs for updated data

### Time Required
- Preparation: 15-30 minutes
- File replacement: 5 minutes
- Dashboard restart: 1 minute
- Verification: 10 minutes
- **Total**: ~30-45 minutes per week

---

## Data Flow

```
Your Data Source (Excel, Database, etc.)
    ↓
Export to CSV
    ↓
Place in data/import_templates/
    ↓
CSV Loaders (csv_loader.py, evm_loader.py)
    ↓
Dashboard (dashboard.py)
    ↓
Streamlit UI
    ↓
User Views
```

---

## Key Features

### ✅ Advantages
- **Easy Updates**: Just replace CSV files
- **No Hardcoding**: All data from files
- **Flexible**: Add/remove data easily
- **Scalable**: Works with any data volume
- **Maintainable**: Clear structure
- **Cacheable**: Performance optimized
- **Robust**: Error handling built-in

### ⚠️ Considerations
- CSV files must be in correct format
- Column names must match exactly
- Data types must be correct
- Files must be in correct location

---

## Troubleshooting

### Common Issues

**Dashboard shows "No data available"**
- Check CSV file exists in `data/import_templates/`
- Verify file has data rows (not just headers)
- Check column names match exactly

**Calculations are incorrect**
- Verify numeric columns have no text
- Check for missing values
- Verify date format (YYYY-MM-DD)

**Dashboard won't start**
- Check Python syntax: `python -m py_compile dashboard.py`
- Verify all imports work
- Check CSV loaders are in correct location

---

## Next Steps

### To Use the System
1. Prepare your CSV files with required columns
2. Place them in `data/import_templates/`
3. Run: `streamlit run dashboard.py`
4. Dashboard loads data automatically

### To Customize
1. Edit CSV file columns as needed
2. Update loader methods if adding new files
3. Update dashboard tabs to use new data
4. Test thoroughly before deploying

### To Extend
1. Add new CSV files to `CSV_FILES` dict
2. Create getter methods in loaders
3. Update dashboard to display new data
4. Update WEEKLY_UPDATE_GUIDE.md

---

## Files Modified/Created

### Created
- ✅ `src/construction_system/csv_loader.py` - CSV data loader
- ✅ `src/construction_system/evm_loader.py` - EVM data loader
- ✅ `WEEKLY_UPDATE_GUIDE.md` - Update guide
- ✅ `CSV_INTEGRATION_SUMMARY.md` - This file

### Modified
- ✅ `dashboard.py` - Fixed plotly error, added imports

### Unchanged
- All other files remain unchanged
- Database functionality still available
- All dashboard tabs still work

---

## Verification

### Syntax Check
```bash
python -m py_compile dashboard.py
```

### Import Check
```bash
python -c "from src.construction_system.csv_loader import get_loader; print('OK')"
python -c "from src.construction_system.evm_loader import get_evm_loader; print('OK')"
```

### Dashboard Start
```bash
streamlit run dashboard.py
```

---

## Support

For questions or issues:
1. Check `WEEKLY_UPDATE_GUIDE.md`
2. Review CSV file examples
3. Check dashboard error messages
4. Verify file locations and formats

---

## Version Info

- **Created**: May 14, 2026
- **Dashboard Version**: 2.0 (CSV-based)
- **Python**: 3.8+
- **Streamlit**: 1.36+
- **Pandas**: 2.2+
- **Plotly**: 5.22+
