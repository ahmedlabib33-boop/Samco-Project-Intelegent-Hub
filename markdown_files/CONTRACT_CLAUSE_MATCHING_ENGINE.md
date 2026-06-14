# Contract Clause Matching Engine

## Executive Summary

The Contract Clause Matching Engine is a professional tool that automatically matches project events (delays, claims, variations, payments) to applicable contract clauses and provides:

- **Entitlement Analysis**: Determines if the event qualifies for compensation/EOT
- **Notice Requirements**: Specifies what notices must be sent and when
- **Financial Impact**: Calculates exposure and recovery potential
- **Schedule Impact**: Assesses time implications and delay damages
- **Critical Actions**: Lists required evidence and procedural steps

---

## 1. System Architecture

### 1.1 Core Components

```
Contract Clause Matching Engine
├── Clause Library (10 key clauses)
├── Event Matcher (matches events to clauses)
├── Delay Analyzer (calculates damages & entitlements)
├── Search Engine (keyword-based clause search)
└── Evidence Tracker (required documentation)
```

### 1.2 Data Model

**ContractClause Object:**
```python
{
    clause_id: "8.7",
    topic: "Delay damages",
    location: "Appendix / Clause 8.7",
    plain_english: "Delay damages are 1% per week...",
    beneath_lines: "Even part of a week counts...",
    leverage_holder: "Employer",
    notice_requirement: "EOT must be claimed before...",
    money_impact: "High exposure, capped at 10%",
    schedule_impact: "Critical if no approved EOT",
    practical_action: "Update EOT register weekly..."
}
```

---

## 2. Contract Clause Library

### 2.1 Key Clauses Included

| Clause ID | Topic | Leverage | Risk Level |
|-----------|-------|----------|-----------|
| 1.0 | Contract Basics | Neutral | LOW |
| 1.1 | Accepted Contract Amount | Employer | HIGH |
| 1.2 | Re-measured Contract | Shared | MEDIUM |
| 4.20 | Employer Equipment & Materials | Shared | HIGH |
| 8.2 | Time for Completion | Employer | HIGH |
| 8.4 | Extension of Time | Shared | CRITICAL |
| 8.7 | Delay Damages | Employer | CRITICAL |
| 13.1 | Right to Vary | Employer | HIGH |
| 13.3 | Variation Procedure | Shared | CRITICAL |
| 14.7 | Payment Period | Employer | MEDIUM |
| 20.1 | Claims Time Bar | Employer | CRITICAL |

### 2.2 Contract Baseline

- **Employer**: Roya
- **Contractor**: Samco
- **Project**: Big Project Civil Works
- **Commencement**: 30-Apr-2025
- **Contract Value**: EGP 367,286,025
- **Time for Completion**: 19 months
- **Delay Damages**: 1% per week (capped 10%)

---

## 3. Event Matching Logic

### 3.1 Material Delivery Delay

**Applicable Clauses:**
1. **Clause 4.20** - Employer Equipment & Free-Issue Materials
   - Relevance: HIGH
   - Requirement: Proof of timely requisition and readiness
   - Entitlement: Possible EOT if critical path affected

2. **Clause 8.2** - Time for Completion
   - Relevance: HIGH
   - Requirement: Measure against 19-month baseline
   - Entitlement: EOT available if compliant

3. **Clause 8.4** - Extension of Time
   - Relevance: HIGH
   - Requirement: Strict notice and monthly updates
   - Entitlement: EOT protects against delay damages

4. **Clause 8.7** - Delay Damages
   - Relevance: HIGH
   - Requirement: Secure EOT before damages crystallize
   - Exposure: 1% per week, capped 10%

5. **Clause 20.1** - Claims Time Bar
   - Relevance: CRITICAL
   - Requirement: Immediate notice, monthly account
   - Risk: Missed notice = waived claim

**Critical Actions:**
- Send protective notice immediately (Clause 20.1)
- Maintain approved programme and requisitions (Clause 4.20)
- Submit monthly claim account (Clause 20.1)
- Document critical path impact (Clause 8.2)
- Secure EOT before damages crystallize (Clause 8.7)

### 3.2 Variation / Change Order

**Applicable Clauses:**
1. **Clause 13.1** - Right to Vary
   - Relevance: HIGH
   - Requirement: Written instruction from Employer/Engineer
   - Entitlement: Possible EOT if variation delays critical path

2. **Clause 13.3** - Variation Procedure
   - Relevance: CRITICAL
   - Requirement: Notice/proposal within required period
   - Risk: Missed procedure = lost claim

3. **Clause 1.1** - Accepted Contract Amount
   - Relevance: MEDIUM
   - Requirement: Prove variation is outside scope
   - Risk: High barrier to extra payment

**Critical Actions:**
- Get written instruction from Engineer
- Submit notice/proposal within required period
- Include time and cost impact analysis
- Maintain monthly claim account
- Update approved programme

### 3.3 Payment Delay

**Applicable Clauses:**
1. **Clause 14.7** - Payment Period
   - Relevance: HIGH
   - Requirement: Complete submission with all documents
   - Entitlement: 45-day payment period from complete submission

2. **Clause 20.1** - Claims Time Bar
   - Relevance: CRITICAL
   - Requirement: Strict notice and monthly account
   - Risk: Missed notice = waived claim

**Critical Actions:**
- Ensure complete IPC submission
- Attach all supporting documents
- Track Engineer receipt date
- Monitor 45-day payment period
- Send payment reminder if overdue

### 3.4 Remeasurement

**Applicable Clauses:**
1. **Clause 1.2** - Re-measured Contract
   - Relevance: HIGH
   - Requirement: Timely measurement records
   - Entitlement: Payment follows measured work

**Critical Actions:**
- Keep survey sheets and IR approvals
- Maintain measurement sheets
- Map to BOQ items
- Resolve disagreements promptly

---

## 4. Delay Event Analysis

### 4.1 Delay Damages Calculation

**Formula:**
```
Delay Damages = (Contract Value × 1%) × Number of Weeks
Cap: 10% of Contract Value
```

**Example - 46-Day Delay:**
```
Delay Days: 46
Weeks: 46 ÷ 7 = 6.57 weeks
Contract Value: EGP 367,286,025
Damages per Week: EGP 367,286,025 × 1% = EGP 3,672,860
Total Damages: EGP 3,672,860 × 6.57 = EGP 24,142,761
Cap (10%): EGP 36,728,603
Exposure: EGP 24,142,761 (within cap)
```

### 4.2 Entitlement Analysis

**If Contractor-Caused:**
- ❌ NO EOT
- ❌ NO Cost Recovery
- ⚠️ Delay Damages Accrue
- ✓ Recovery Plan Required

**If Employer-Caused:**
- ✓ POSSIBLE EOT (if compliant)
- ✓ POSSIBLE Cost Recovery (if compliant)
- ✓ Delay Damages Protected
- ✓ Prolongation Cost Claimable

**If Concurrent Delay:**
- ✓ POSSIBLE EOT (if compliant)
- ❌ NO Cost Recovery (concurrent period)
- ✓ Delay Damages Protected (for non-concurrent)

### 4.3 Critical Path Impact

**High Impact If:**
- Delay affects critical path activities
- No float available
- Delays project completion
- Triggers delay damages

**Low Impact If:**
- Delay on non-critical activities
- Float available
- No impact on completion
- Can be recovered

---

## 5. Notice Requirements

### 5.1 Immediate Actions (Within 24 Hours)

1. **Send Protective Notice**
   - Reference: Clause 20.1 (Claims Time Bar)
   - Content: Event description, preliminary impact
   - To: Engineer, Employer
   - Evidence: Email with timestamp

2. **Preserve Evidence**
   - Photographs of delay cause
   - Delivery notes (if material delay)
   - Requisition records
   - Programme updates

### 5.2 Within 7 Days

1. **Submit Detailed Notice**
   - Reference: Clause 20.1 (Claims Time Bar)
   - Content: Full event description, impact analysis
   - Attachments: Evidence, programme impact
   - To: Engineer, Employer

2. **Update Approved Programme**
   - Show delay impact
   - Identify critical path
   - Propose recovery measures

### 5.3 Monthly

1. **Submit Monthly Claim Account**
   - Reference: Clause 20.1 (Monthly Claim Account)
   - Content: All claims and variations
   - Status: Updated status of each claim
   - To: Engineer

2. **Update Delay Analysis**
   - Current delay status
   - Revised completion date
   - Cumulative impact
   - Recovery progress

---

## 6. Financial Impact Analysis

### 6.1 Delay Damages Exposure

| Delay Days | Weeks | Damages (EGP) | % of Contract |
|-----------|-------|---------------|---------------|
| 7 | 1 | 3,672,860 | 1.0% |
| 14 | 2 | 7,345,720 | 2.0% |
| 46 | 6.57 | 24,142,761 | 6.6% |
| 91 | 13 | 47,746,318 | 13.0% (capped) |

### 6.2 Cost Recovery Potential

**If Employer-Caused & Compliant:**
- ✓ Prolongation Cost (labor, equipment, overhead)
- ✓ Material Price Adjustment (if applicable)
- ✓ Acceleration Cost (if instructed)
- ✓ Demobilization/Remobilization

**If Contractor-Caused:**
- ❌ NO Cost Recovery
- ⚠️ Delay Damages Exposure
- ✓ Recovery Plan Cost (Contractor's risk)

---

## 7. Schedule Impact Analysis

### 7.1 Critical Path Impact

**High Impact:**
- Delay on critical path activities
- No float available
- Delays project completion
- Triggers delay damages

**Example - Material Delay Event 1:**
```
Activity: CON-B01-BAS02-1010
Original Duration: 15 days
Delay: 46 days
New Duration: 61 days
Critical Path Impact: YES
Delay Damages: YES (if not Employer-caused)
```

### 7.2 Cascading Effects

**Direct Impact:**
- Activity delayed by 46 days

**Cascading Impact:**
- Dependent activities delayed by 46 days
- Subsequent activities delayed by 46 days
- Project completion delayed by 46 days

**Total Project Impact:**
- 46 days schedule slip
- Delay damages: EGP 24.1M (if not Employer-caused)

---

## 8. Evidence Requirements

### 8.1 For Material Delay Claims

**Required Evidence:**
1. Approved baseline programme
2. Monthly programme updates
3. Material requisitions
4. Delivery notes
5. Inspection records
6. Stock records
7. Activity impact analysis
8. Critical path proof
9. Timely notices
10. Monthly claim accounts

### 8.2 For Variation Claims

**Required Evidence:**
1. Written instruction from Engineer
2. Variation notice/proposal
3. Time impact analysis
4. Cost impact analysis
5. Updated programme
6. Monthly claim account
7. Supporting calculations
8. Photographs/documentation

### 8.3 For Payment Claims

**Required Evidence:**
1. Complete IPC submission
2. Supporting documents
3. Measurement sheets
4. Quality certificates
5. Delivery notes
6. Inspection records
7. Transmittal letter
8. Engineer receipt proof

---

## 9. Dashboard Integration

### 9.1 Tab: "⚖️ Contract Clauses"

**Features:**
1. **Event-to-Clause Matching**
   - Select event type
   - Enter description
   - Get applicable clauses

2. **Delay Event Analysis**
   - Input delay days
   - Specify if contractor-caused
   - Specify if critical path
   - Get entitlement analysis

3. **Clause Library Browser**
   - Search by keyword
   - View full clause details
   - See practical actions

4. **Clause Summary Table**
   - All clauses at a glance
   - Quick reference

### 9.2 Key Metrics Displayed

- Delay Days
- Entitlement Status
- Delay Damages per Week
- Total Exposure
- Critical Actions
- Applicable Clauses

---

## 10. Best Practices

### 10.1 Claim Management

1. **Send Protective Notice Immediately**
   - Don't wait for full analysis
   - Reference Clause 20.1
   - Preserve claim rights

2. **Maintain Monthly Claim Account**
   - Update every month
   - Include all claims/variations
   - Track status

3. **Document Everything**
   - Photographs
   - Emails
   - Meeting minutes
   - Delivery notes
   - Requisitions

4. **Update Programme Monthly**
   - Show delay impact
   - Identify critical path
   - Propose recovery

### 10.2 Risk Management

1. **Track Delay Damages Exposure**
   - Calculate weekly
   - Monitor against cap
   - Secure EOT before crystallization

2. **Comply with Procedures**
   - Follow notice requirements
   - Submit on time
   - Include required evidence

3. **Preserve Entitlements**
   - Don't miss time bars
   - Maintain monthly accounts
   - Keep all records

---

## 11. Common Pitfalls

### 11.1 Missed Notices

**Risk**: Clause 20.1 - Claims Time Bar
- Failure to comply = irrevocable waiver
- Missed notice = lost claim
- No cost recovery
- No EOT

**Prevention:**
- Send protective notice immediately
- Maintain claims register
- Track notice deadlines

### 11.2 Incomplete Monthly Accounts

**Risk**: Clause 20.1 - Monthly Claim Account
- Omitted items may not be considered
- Weak claims become weaker
- Delay damages continue

**Prevention:**
- Submit complete monthly account
- Include all claims/variations
- Update status monthly

### 11.3 Weak Critical Path Proof

**Risk**: Clause 8.2 - Time for Completion
- Without critical path proof, EOT harder to prove
- Delay damages may apply
- Schedule impact unclear

**Prevention:**
- Maintain approved baseline programme
- Update monthly with actual progress
- Show critical path clearly

---

## 12. Conclusion

The Contract Clause Matching Engine provides a systematic approach to:
- Identify applicable contract clauses
- Analyze entitlements and risks
- Calculate financial exposure
- Determine required actions
- Preserve claim rights

**Key Success Factors:**
1. ✓ Send notices immediately (Clause 20.1)
2. ✓ Maintain monthly claim accounts (Clause 20.1)
3. ✓ Document everything (Practical Action)
4. ✓ Update programme monthly (Clause 8.3)
5. ✓ Comply with procedures (All Clauses)

---

*Document Version: 1.0*
*Created: May 14, 2026*
*Contract: Big Project Civil Works*
*Employer: Roya | Contractor: Samco*
