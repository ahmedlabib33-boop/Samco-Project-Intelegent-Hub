# Credits & Attribution

## Project Leadership

**Designed and Developed by:** Eng Ahmed Labib  
**Department:** Planning Department  
**Organization:** SAMCO Egypt

---

## Project Overview

### SAMCO Egypt Construction Project Control Dashboard
A professional, multi-layer Streamlit dashboard for construction project management with comprehensive analytics, contract tracking, and project control capabilities.

**Project:** Roya Construction Project  
**Contractor:** SAMCO Egypt  
**Employer:** Roya  
**Contract Value:** EGP 367.3M  
**Duration:** 19 Months

---

## System Components

### Core Dashboard
- **dashboard.py** - Main Streamlit application with 9 analytical tabs
- Professional UI with SAMCO Egypt branding
- Real-time project metrics and KPIs

### Data Management
- **CSV Data Loaders** - Load project data from CSV files
  - csv_loader.py - General CSV data loader
  - evm_loader.py - Earned Value Management data loader
- **Database System** - SQLite database for data persistence
- **Analytics Engine** - EVM calculations and project analytics

### Features
1. **Overview Tab** - Project summary and KPIs
2. **EVM Analysis** - Earned Value Management metrics
3. **Contracts** - Contract management and payments
4. **Delays** - Delay tracking and analysis
5. **Risks** - Risk register and management
6. **Milestones** - Milestone tracking
7. **Time Impact** - Schedule impact analysis
8. **S-Curve** - Financial progress tracking
9. **Contract Clauses** - Clause matching engine

---

## Documentation

### User Guides
- **CSV_QUICKSTART.md** - 5-minute quick start guide
- **WEEKLY_UPDATE_GUIDE.md** - Comprehensive weekly update guide
- **README.md** - Main project documentation

### Technical Documentation
- **CSV_INTEGRATION_SUMMARY.md** - Technical implementation details
- **CSV_SYSTEM_INDEX.md** - Navigation and reference guide
- **IMPLEMENTATION_COMPLETE.md** - Implementation summary

### Data Documentation
- **docs/data_dictionary.md** - Data field definitions
- **docs/system_blueprint.md** - System architecture

---

## Technology Stack

### Frontend
- **Streamlit** - Web application framework
- **Plotly** - Interactive visualizations
- **HTML/CSS** - Custom styling

### Backend
- **Python 3.8+** - Programming language
- **Pandas** - Data manipulation
- **SQLite** - Database

### Development Tools
- **Git** - Version control
- **pytest** - Testing framework

---

## Key Metrics & Analytics

### Earned Value Management (EVM)
- Budget at Completion (BAC)
- Actual Cost (AC)
- Earned Value (EV)
- Planned Value (PV)
- Schedule Performance Index (SPI)
- Cost Performance Index (CPI)
- Schedule Variance (SV)
- Cost Variance (CV)
- Estimate at Completion (EAC)
- Estimate to Complete (ETC)
- To-Complete Performance Index (TCPI)

### Project Tracking
- Activity progress monitoring
- WBS cost breakdown
- Monthly spend trends
- Critical path analysis
- Delay impact analysis
- Risk assessment
- Milestone tracking
- Contract management

---

## Data Sources

### CSV Files (12 total)
1. activities.csv - Project activities
2. evm.csv - EVM metrics
3. progress_updates.csv - Progress updates
4. delay_events.csv - Delay events
5. risks.csv - Risk register
6. payments.csv - Payment tracking
7. contracts.csv - Contract data
8. milestones.csv - Milestones
9. change_orders.csv - Change orders
10. cost_items.csv - Cost breakdown
11. claims.csv - Claims data
12. wbs.csv - WBS structure

### Database
- SQLite database for persistent storage
- Automatic data import from CSV files

---

## Version History

### Version 2.0 (May 2026)
- CSV data integration
- Fixed Plotly visualization errors
- Added EVM data loaders
- Comprehensive documentation
- Weekly update process

### Version 1.0 (Previous)
- Initial dashboard development
- Database schema design
- Analytics engine
- Contract matching system

---

## Support & Maintenance

### Documentation
- Comprehensive user guides
- Technical documentation
- Troubleshooting guides
- Quick reference materials

### Updates
- Weekly data updates via CSV files
- Regular maintenance and improvements
- Bug fixes and enhancements

### Contact
**Department:** Planning Department  
**Organization:** SAMCO Egypt

---

## Acknowledgments

### Planning Department
- Project planning and coordination
- Data management and validation
- Requirements definition
- Testing and verification

### SAMCO Egypt
- Project execution
- Data provision
- System deployment
- Ongoing support

---

## License & Usage

This dashboard is developed for SAMCO Egypt's internal use for the Roya Construction Project.

**Confidentiality:** This system contains proprietary project information and should be treated as confidential.

**Usage Rights:** Authorized SAMCO Egypt personnel only.

---

## System Status

✅ **Production Ready**
- All features implemented
- Comprehensive documentation
- Fully tested and verified
- Ready for deployment

---

## Contact Information

**For Questions or Support:**
- Department: Planning Department
- Organization: SAMCO Egypt
- Project: Roya Construction Project

---

**Last Updated:** May 14, 2026  
**Dashboard Version:** 2.0  
**Status:** Active & Maintained

---

## Dedication

This dashboard is dedicated to supporting the Planning Department's mission to deliver professional project management and control systems for SAMCO Egypt's construction projects.

**Designed and Developed by:** Eng Ahmed Labib  
**Planning Department, SAMCO Egypt**

---

*"Excellence in Project Management Through Technology"*
