import sys, sqlite3
sys.path.insert(0, 'src')
from construction_system.database import DEFAULT_DB_PATH


def fmt_num(value):
    return f"{float(value or 0):,.0f}"


conn = sqlite3.connect(DEFAULT_DB_PATH)
conn.row_factory = sqlite3.Row

# Fix project_id mismatch in cost_items
changed = conn.execute(
    "UPDATE cost_items SET project_id = 'The Big -P.01-UP-20-April-26' "
    "WHERE project_id = 'The Big -P01-UP-20-April-26'"
).rowcount
conn.commit()
print(f"Fixed project_id in cost_items: {changed} rows")

# Verify cost_item_id (mapped from cost_code = activity_id)
r = conn.execute(
    "SELECT cost_item_id, wbs_id, budget_cost, actual_cost FROM cost_items WHERE budget_cost > 0 LIMIT 3"
).fetchall()
print("\nSample cost_items (budget>0):")
for row in r:
    print(dict(row))

# Verify join: cost_items.cost_item_id -> activities.activity_id
r = conn.execute("""
    SELECT COUNT(*) as cnt, SUM(ci.budget_cost) as bac, SUM(ci.actual_cost) as ac
    FROM cost_items ci
    JOIN activities a ON a.activity_id = ci.cost_item_id
    WHERE ci.budget_cost > 0
""").fetchone()
print(f"\nJoin cost_items->activities: {r['cnt']} rows, BAC={fmt_num(r['bac'])}, AC={fmt_num(r['ac'])}")

# Verify totals
r = conn.execute(
    "SELECT SUM(budget_cost), SUM(actual_cost) FROM cost_items"
).fetchone()
print(f"Total cost_items: budget={fmt_num(r[0])}, actual={fmt_num(r[1])}")

# Activities progress
r = conn.execute("""
    SELECT COUNT(*) as total,
           AVG(planned_progress) as avg_planned,
           AVG(actual_progress) as avg_actual,
           SUM(CASE WHEN is_critical=1 THEN 1 ELSE 0 END) as critical
    FROM activities
""").fetchone()
avg_planned = float(r["avg_planned"] or 0)
avg_actual = float(r["avg_actual"] or 0)
print(f"\nActivities: total={r['total']}, avg_planned={avg_planned:.1f}%, avg_actual={avg_actual:.1f}%, critical={r['critical']}")

conn.close()
print("\nData verification complete.")
