# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Import Your Data
Your CSV files are already in `data/import_templates/`. Run:
```bash
python scripts/import_csv_data.py
```

### Step 3: Launch Dashboard
```bash
streamlit run dashboard.py
```

The dashboard opens automatically at `http://localhost:8501`

---

## 📊 What You'll See

### Overview Tab
- Project summary with key metrics
- Budget vs Actual cost comparison
- Schedule and cost performance indices
- WBS cost breakdown
- Monthly spend trends

### EVM Analysis Tab
- Complete Earned Value Management metrics
- Schedule and cost performance gauges
- Activity-level details
- Variance analysis

### Contracts Tab
- Contract value tracking
- Payment status
- Certified vs paid amounts
- Contract status distribution

### Delays Tab
- Delay events and impact
- Responsible parties
- EOT (Extension of Time) potential
- Pending exposure days

### Risks Tab
- Risk severity distribution
- Risk categories
- Probability and impact assessment
- Mitigation status

### Milestones Tab
- Milestone tracking
- Change orders
- Cost and time impacts

---

## 📁 Your Data

Your real project data is in CSV format:
- `data/import_templates/activities.csv` - 1,363 activities
- `data/import_templates/cost_items.csv` - Budget and actual costs
- `data/import_templates/contracts.csv` - Contract information
- `data/import_templates/delay_events.csv` - Delay tracking
- `data/import_templates/risks.csv` - Risk register
- `data/import_templates/milestones.csv` - Milestone tracking

All data is automatically imported into the SQLite database.

---

## 🔍 Verify Your Data

Check that data was imported correctly:
```bash
python scripts/verify_data.py
```

Expected output:
```
Activities: total=1363, avg_planned=57.0%, avg_actual=25.3%, critical=578
Total cost_items: budget=367,286,025, actual=112,676,722
```

---

## ✅ Run Tests

Verify all analytics functions work:
```bash
pytest tests/test_analytics.py -v
```

Expected: 4 passed tests

---

## 🎨 Dashboard Features

### KPI Cards
- **BAC**: Budget at Completion (total planned budget)
- **AC**: Actual Cost (total spent)
- **SPI**: Schedule Performance Index (>1 = ahead)
- **CPI**: Cost Performance Index (>1 = under budget)

### Status Indicators
- 🟢 **Green**: On Track (SPI/CPI ≥ 0.95)
- 🟡 **Yellow**: At Risk (SPI/CPI 0.85-0.94)
- 🔴 **Red**: Critical (SPI/CPI < 0.85)

### Charts
- Bar charts for cost breakdown
- Line charts for spend trends
- Pie charts for status distribution
- Gauge charts for performance indices

---

## 🛠️ Troubleshooting

### Dashboard won't start
```bash
# Check Python version (need 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### No data showing
```bash
# Re-import data
python scripts/import_csv_data.py

# Verify data was imported
python scripts/verify_data.py
```

### Charts not displaying
- Refresh the browser page
- Check that Plotly is installed: `pip install plotly>=5.22`

---

## 📚 Documentation

- **README.md** - Full documentation
- **COMPLETION_SUMMARY.md** - What was built
- **docs/data_dictionary.md** - Field definitions
- **docs/system_blueprint.md** - System architecture

---

## 💡 Tips

1. **Data Caching**: Dashboard caches data for 60 seconds. Refresh to see latest data.

2. **Sorting**: Click column headers in tables to sort.

3. **Filtering**: Use browser's find function (Ctrl+F) to search tables.

4. **Export**: Right-click charts to save as PNG.

5. **Full Screen**: Press F11 in browser for full-screen mode.

---

## 🎯 Next Steps

1. **Explore the data** - Click through all tabs to see your project metrics
2. **Check status** - Look for yellow/red indicators that need attention
3. **Review trends** - Check monthly spend and progress charts
4. **Monitor risks** - Review risk register and mitigation status
5. **Track contracts** - Monitor payment status and variations

---

## 📞 Support

For issues:
1. Check COMPLETION_SUMMARY.md for what was built
2. Run `python scripts/verify_data.py` to check data
3. Run `pytest tests/test_analytics.py -v` to verify functions
4. Check README.md for detailed documentation

---

**Ready to go!** 🚀

Run `streamlit run dashboard.py` and start exploring your project data.
