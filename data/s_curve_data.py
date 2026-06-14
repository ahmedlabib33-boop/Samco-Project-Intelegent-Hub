"""S-Curve data for project financial tracking."""

# S-Curve data from the provided CSV
S_CURVE_DATA = {
    "months": [
        "Oct-25", "Nov-25", "Dec-25", "Jan-26", "Feb-26", "Mar-26", "Apr-26",
        "May-26", "Jun-26", "Jul-26", "Aug-26", "Sep-26", "Oct-26", "Nov-26",
        "Dec-26", "Jan-27", "Feb-27", "Mar-27"
    ],
    "monthly_planned": [
        0, 8347296.45, 61405155.86, 67496644.02, 33633991.22, 38111113.51,
        29721101.71, 20259735.78, 13490432.04, 14762397.20, 9924530.76,
        12399329.58, 8650019.18, 14242110.80, 10767589.67, 14357924.01,
        9156113.78, 560539.45
    ],
    "monthly_planned_cumm": [
        0, 8347296.45, 69752452.31, 137249096.33, 170883087.55, 208994201.06,
        238715302.77, 258975038.55, 272465470.59, 287227867.79, 297152398.55,
        309551728.13, 318201747.31, 332443858.11, 343211447.78, 357569371.79,
        366725485.57, 367286025.02
    ],
    "monthly_actual": [
        0, 3974600.57, 8089030.90, 8521118.53, 34796118.93, 20206392.66,
        17551865.86, 14754736.88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    "monthly_actual_cumm": [
        0, 3974600.57, 12063631.47, 20584750.00, 55380868.93, 75587261.59,
        93139127.45, 107893864.33, 107893864.33, 107893864.33, 107893864.33,
        107893864.33, 107893864.33, 107893864.33, 107893864.33, 107893864.33,
        107893864.33, 107893864.33
    ],
    "monthly_invoiced": [
        0, 0, 23485862.02, 46408963.51, 40393706.06, 17641618.94,
        15475615.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    "monthly_invoiced_cumm": [
        0, 0, 23485862.02, 69894825.53, 110288531.59, 127930150.52,
        143405765.52, 143405765.52, 143405765.52, 143405765.52, 143405765.52,
        143405765.52, 143405765.52, 143405765.52, 143405765.52, 143405765.52,
        143405765.52, 143405765.52
    ]
}

def get_s_curve_data():
    """Return S-Curve data dictionary."""
    return S_CURVE_DATA

def get_s_curve_summary():
    """Get S-Curve summary metrics."""
    planned_total = S_CURVE_DATA["monthly_planned_cumm"][-1]
    actual_total = S_CURVE_DATA["monthly_actual_cumm"][-1]
    invoiced_total = S_CURVE_DATA["monthly_invoiced_cumm"][-1]
    
    # Find last month with actual data
    last_actual_month = None
    for i in range(len(S_CURVE_DATA["monthly_actual"]) - 1, -1, -1):
        if S_CURVE_DATA["monthly_actual"][i] > 0:
            last_actual_month = S_CURVE_DATA["months"][i]
            break
    
    # Calculate variances
    planned_to_date = S_CURVE_DATA["monthly_planned_cumm"][7]  # Apr-26
    actual_to_date = actual_total
    schedule_variance = actual_to_date - planned_to_date
    schedule_variance_pct = (schedule_variance / planned_to_date * 100) if planned_to_date > 0 else 0
    
    # Calculate invoicing metrics
    invoicing_to_actual_ratio = (invoiced_total / actual_total * 100) if actual_total > 0 else 0
    invoicing_to_planned_ratio = (invoiced_total / planned_total * 100) if planned_total > 0 else 0
    
    return {
        "planned_total": planned_total,
        "actual_total": actual_total,
        "invoiced_total": invoiced_total,
        "last_actual_month": last_actual_month,
        "schedule_variance": schedule_variance,
        "schedule_variance_pct": schedule_variance_pct,
        "invoicing_to_actual_ratio": invoicing_to_actual_ratio,
        "invoicing_to_planned_ratio": invoicing_to_planned_ratio,
        "planned_to_date": planned_to_date,
        "actual_to_date": actual_to_date,
        "invoiced_to_date": invoiced_total,
    }
