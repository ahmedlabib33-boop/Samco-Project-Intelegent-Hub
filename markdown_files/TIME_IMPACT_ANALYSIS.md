# Time Impact Analysis - Steel Activities Delay Study

## Executive Summary

This document analyzes the time impact of material delivery delays on the RFT (Reinforcement) activities in the construction project. The analysis identifies two critical delay events that impact the project schedule by 45-46 days each, affecting the critical path and requiring activity fragmentation strategies.

---

## 1. Delay Event Overview

### Event 1: B01 Material Delivery Delay

**Activity Details:**
- **Activity ID**: CON-B01-BAS02-1010
- **Activity Name**: RFT for Walls, Col. & Cores (B01) (Bas 02)
- **Building**: B01
- **Original Duration**: 15 days
- **Planned Schedule**: 25-Dec-25 to 12-Jan-26

**Delay Impact:**
- **Delay Days**: 46 days
- **Material Delivery Date**: 13-Feb-26 (partial - 371 tons out of 726 tons)
- **Root Cause**: Delay on Employee free-issue materials
- **Activity Progress**: 41% complete at time of delay

**Schedule Impact:**
- Original finish: 12-Jan-26
- Actual finish: 25-Feb-26 (with fragmentation)
- Schedule slip: 44 days

---

### Event 2: B04 Material Delivery Delay

**Activity Details:**
- **Activity ID**: CON-B04-FOOT-1050
- **Activity Name**: RFT for RC Raft & Footings (B04)
- **Building**: B04
- **Original Duration**: 8 days
- **Planned Schedule**: 22-Mar-26 to 30-Mar-26

**Delay Impact:**
- **Delay Days**: 45 days
- **Material Delivery Date**: 05-May-26
- **Root Cause**: Delay on Employee free-issue materials
- **Activity Progress**: 28% complete at time of delay

**Schedule Impact:**
- Original finish: 30-Mar-26
- Actual finish: 14-May-26 (with fragmentation)
- Schedule slip: 45 days

---

## 2. Time Impact Analysis Logic

### 2.1 Delay Calculation Methodology

**Formula:**
```
Delay Days = Actual Material Delivery Date - Planned Material Delivery Date
```

**For Event 1:**
- Planned Delivery: 27-Oct-25
- Actual Delivery: 13-Feb-26
- Delay = 108 days (but activity impact = 46 days due to fragmentation)

**For Event 2:**
- Planned Delivery: 05-May-26 (implied from schedule)
- Actual Delivery: 05-May-26
- Delay = 45 days (from original planned start)

### 2.2 Critical Path Impact

**Event 1 - B01 Critical Path:**
```
B01-FOOT-1050 (12 days)
    ↓
B01-FOOT-1070 (8 days)
    ↓
B01-BAS02-1010 (15 days) ← DELAYED 46 DAYS
    ↓
B01-BAS02-1070 (10 days)
    ↓
B01-BAS02-1080 (6 days)
    ↓
B01-BAS02-1090 (8 days)

Original Path Duration: 59 days
With Delay: 105 days
Schedule Slip: 46 days
```

**Event 2 - B04 Critical Path:**
```
B04-FOOT-1050 (8 days) ← DELAYED 45 DAYS
    ↓
B04-FOOT-1070 (5 days)
    ↓
B04-BAS02-1010 (10 days)
    ↓
B04-BAS02-1060 (10 days)
    ↓
B04-BAS02-1080 (5 days)

Original Path Duration: 38 days
With Delay: 83 days
Schedule Slip: 45 days
```

### 2.3 Activity Fragmentation Strategy

**Fragmentation Logic:**
When a material delivery delay occurs mid-activity, the activity is split into:
1. **Part 1**: Work completed before delay (using available materials)
2. **Delay Period**: Waiting for material delivery
3. **Part 2**: Work resumed after material arrival

**Event 1 Fragmentation:**
```
Original Activity: 25-Dec-25 to 12-Jan-26 (15 days)
    ↓
Part 1: 25-Dec-25 to 31-Dec-25 (6 days)
    - Budgeted Units: 48.92 tons
    - Completed: ~20 tons (41% progress)
    ↓
Delay Period: 01-Jan-26 to 16-Feb-26 (46 days)
    - Waiting for material delivery
    - Material arrives: 13-Feb-26 (371 tons partial)
    ↓
Part 2: 16-Feb-26 to 25-Feb-26 (10 days)
    - Remaining Units: ~29 tons
    - Completion: 100%
```

**Event 2 Fragmentation:**
```
Original Activity: 22-Mar-26 to 30-Mar-26 (8 days)
    ↓
Part 1: 22-Mar-26 to 24-Mar-26 (2 days)
    - Budgeted Units: 296.46 tons
    - Completed: ~83 tons (28% progress)
    ↓
Delay Period: 25-Mar-26 to 04-May-26 (45 days)
    - Waiting for material delivery
    - Material arrives: 05-May-26
    ↓
Part 2: 08-May-26 to 14-May-26 (6 days)
    - Remaining Units: ~213 tons
    - Completion: 100%
```

---

## 3. Root Cause Analysis

### Material Supply Chain Failure

**Primary Cause:** Delay on Employee free-issue materials

**Contributing Factors:**
1. **Supplier Performance**: Late delivery from material supplier
2. **Procurement Delay**: Extended procurement cycle
3. **Quality Issues**: Possible inspection/rework delays
4. **Logistics**: Transportation/handling delays
5. **Coordination**: Inadequate material planning

**Impact Chain:**
```
Supplier Delay
    ↓
Material Not Available
    ↓
Activity Cannot Progress
    ↓
Crew Idle Time
    ↓
Schedule Slip
    ↓
Cascading Delays to Dependent Activities
```

---

## 4. Schedule Impact Analysis

### 4.1 Direct Impact

| Metric | Event 1 | Event 2 |
|--------|---------|---------|
| Activity Duration | 15 days | 8 days |
| Delay Days | 46 days | 45 days |
| Total Duration | 61 days | 53 days |
| Schedule Slip | 46 days | 45 days |
| % Increase | 307% | 663% |

### 4.2 Cascading Impact

**Event 1 Cascading Effects:**
- B01-BAS02-1070 delayed by 46 days
- B01-BAS02-1080 delayed by 46 days
- B01-BAS02-1090 delayed by 46 days
- B01-BAS01-1010 delayed by 46 days
- Total activities affected: 8+

**Event 2 Cascading Effects:**
- B04-FOOT-1070 delayed by 45 days
- B04-BAS02-1010 delayed by 45 days
- B04-BAS02-1060 delayed by 45 days
- B04-BAS02-1080 delayed by 45 days
- Total activities affected: 6+

### 4.3 Project-Level Impact

**Total Schedule Impact:**
- Combined delay: 91 days
- Critical path extension: 91 days
- Project completion delay: 91 days (if no mitigation)

---

## 5. Mitigation Strategies

### 5.1 Activity Fragmentation

**Benefits:**
- ✓ Maintains crew productivity during delay
- ✓ Reduces idle time costs
- ✓ Allows partial progress documentation
- ✓ Enables resource reallocation

**Implementation:**
- Execute Part 1 with available materials
- Prepare site for Part 2 during delay
- Maintain crew continuity where possible

### 5.2 Resource Optimization

**Strategies:**
1. **Crew Reallocation**: Move crews to non-impacted activities (B02, B03)
2. **Parallel Execution**: Accelerate independent activities
3. **Preparation Work**: Use delay period for site preparation
4. **Material Staging**: Prepare for material receipt and inspection

### 5.3 Schedule Compression

**Techniques:**
1. **Concurrent Activities**: Execute dependent activities in parallel
2. **Extended Hours**: Increase working hours for non-delayed activities
3. **Additional Resources**: Deploy extra crews to accelerate
4. **Prefabrication**: Prepare components off-site during delay

### 5.4 Supply Chain Management

**Improvements:**
1. **Backup Suppliers**: Establish alternative material sources
2. **Early Warning System**: Implement delivery tracking
3. **Safety Stock**: Maintain buffer inventory
4. **Supplier Performance**: Monitor and enforce SLAs

---

## 6. Key Performance Indicators

### Schedule Performance

| KPI | Value | Status |
|-----|-------|--------|
| Schedule Variance (Days) | -91 | ⚠️ Behind |
| Critical Activities Impacted | 2 | ⚠️ Critical |
| Average Delay Impact | 45.5 days | ⚠️ High |
| Material Delivery Reliability | 50% | ⚠️ Low |
| Activity Fragmentation Rate | 100% | ⚠️ High |

### Cost Impact

| Item | Impact |
|------|--------|
| Crew Idle Time | High |
| Extended Overhead | 91 days × daily cost |
| Acceleration Costs | Additional resources |
| Material Handling | Extra staging/inspection |

---

## 7. Recommendations

### Immediate Actions (0-7 days)

1. **Activate Contingency Plan**
   - Implement activity fragmentation
   - Reallocate crews to non-impacted activities
   - Prepare material staging areas

2. **Stakeholder Communication**
   - Notify client of 91-day delay
   - Escalate to project management
   - Prepare delay claim documentation

3. **Resource Planning**
   - Identify available crews for reallocation
   - Plan for extended project duration
   - Adjust resource schedules

### Short-term Actions (1-4 weeks)

1. **Supply Chain Recovery**
   - Contact suppliers for expedited delivery
   - Explore alternative material sources
   - Negotiate delivery terms

2. **Schedule Optimization**
   - Compress non-critical path activities
   - Implement concurrent execution
   - Identify acceleration opportunities

3. **Cost Management**
   - Document all delay-related costs
   - Prepare delay claim
   - Negotiate cost recovery

### Long-term Actions (1-3 months)

1. **Process Improvement**
   - Implement early warning system
   - Establish backup suppliers
   - Improve material planning

2. **Risk Management**
   - Increase safety stock
   - Diversify supplier base
   - Enhance procurement process

3. **Performance Monitoring**
   - Track actual vs. planned delivery
   - Monitor schedule recovery
   - Measure mitigation effectiveness

---

## 8. Conclusion

The analysis reveals that material delivery delays have a significant impact on the project schedule, causing 45-46 day delays per event. The fragmentation strategy effectively mitigates crew idle time, but the cascading effects require comprehensive schedule optimization and resource reallocation.

**Key Takeaways:**
- ✓ Material supply chain is critical to schedule performance
- ✓ Activity fragmentation reduces but doesn't eliminate delay impact
- ✓ Cascading delays affect 14+ dependent activities
- ✓ Proactive supply chain management is essential
- ✓ Early warning systems can prevent future delays

**Recommended Actions:**
1. Implement backup supplier strategy
2. Establish material delivery tracking system
3. Increase safety stock for critical materials
4. Enhance procurement planning process
5. Monitor supplier performance metrics

---

## Appendix: Detailed Activity Schedule

### Event 1 - B01 Activities Affected

| Activity ID | Activity Name | Original Duration | Delay Impact | New Duration |
|-------------|---------------|-------------------|--------------|--------------|
| CON-B01-BAS02-1010 | RFT for Walls, Col. & Cores | 15 days | 46 days | 61 days |
| CON-B01-BAS02-1070 | RFT for Slabs & Beams | 10 days | 46 days | 56 days |
| CON-B01-BAS02-1080 | RFT for Stairs | 6 days | 46 days | 52 days |
| CON-B01-BAS02-1090 | RFT for Ramps | 8 days | 46 days | 54 days |

### Event 2 - B04 Activities Affected

| Activity ID | Activity Name | Original Duration | Delay Impact | New Duration |
|-------------|---------------|-------------------|--------------|--------------|
| CON-B04-FOOT-1050 | RFT for RC Raft & Footings | 8 days | 45 days | 53 days |
| CON-B04-FOOT-1070 | RFT for Columns & Walls | 5 days | 45 days | 50 days |
| CON-B04-BAS02-1010 | RFT for Walls, Col. & Cores | 10 days | 45 days | 55 days |
| CON-B04-BAS02-1060 | RFT for Slabs & Beams | 10 days | 45 days | 55 days |

---

*Document Version: 1.0*
*Last Updated: May 14, 2026*
*Analysis Period: Dec 2025 - May 2027*
