import sys, sqlite3, csv
sys.path.insert(0, 'src')
from construction_system.database import DEFAULT_DB_PATH

conn = sqlite3.connect(DEFAULT_DB_PATH)
conn.row_factory = sqlite3.Row

# Fix project_id mismatch in cost_items
conn.execute(
    "UPDATE cost_items SET project_id = 'The Big -P.01-UP-20-April-26' "
    "WHERE project_id = 'The Big -P01-UP-20-April-26'"
)
print(f"Fixed project_id: {conn.total_changes} rows")

# Check cost_items columns
cols = [r[1] for r in conn.execute("PRAGMA table_info(cost_items)").fetchall()]
print("cost_items columns:", cols)

# Sample non-zero rows
rows = conn.execute(
    "SELECT * FROM cost_items WHERE budget_cost > 0 LIMIT 3"
).fetchall()
for r in rows:
    print(dict(r))

# The cost_code column from CSV maps to cost_category in DB
# But cost_code IS the activity_id - check if it's stored
print()
print("cost_category sample (should be activity_id):")
rows = conn.execute(
    "SELECT cost_category, budget_cost FROM cost_items WHERE budget_cost > 0 LIMIT 5"
).fetchall()
for r in rows:
    print(dict(r))

# Check totals
r = conn.execute(
    "SELECT SUM(budget_cost), SUM(actual_cost) FROM cost_items"
).fetchone()
print(f"\nTotal budget_cost={r[0]:,.0f}, actual_cost={r[1]:,.0f}")

conn.commit()
conn.close()
