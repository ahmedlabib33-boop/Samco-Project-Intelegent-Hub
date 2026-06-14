from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from construction_system.database import DEFAULT_DB_PATH
from construction_system.importers import import_csv_folder


def main():
    parser = argparse.ArgumentParser(description="Import CSV files into the construction project database.")
    parser.add_argument(
        "folder",
        nargs="?",
        default=str(ROOT / "data" / "import_templates"),
        help="Folder containing CSV files. Defaults to data/import_templates",
    )
    parser.add_argument("--reset", action="store_true", help="Recreate the database before import")
    args = parser.parse_args()

    results = import_csv_folder(args.folder, DEFAULT_DB_PATH, reset=args.reset)

    if not results:
        print("No CSV files were imported.")
        return

    for table_name, count in results.items():
        print(f"{table_name}: {count} rows imported")

    print(f"Database updated at: {DEFAULT_DB_PATH}")


if __name__ == "__main__":
    main()
