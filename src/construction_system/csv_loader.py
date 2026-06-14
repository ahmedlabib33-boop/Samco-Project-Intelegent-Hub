"""CSV Data Loader - Load all dashboard data from CSV files."""

import pandas as pd
import os
from pathlib import Path
from typing import Dict, Optional

# Define CSV file paths
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "import_templates"

CSV_FILES = {
    "projects": DATA_DIR / "projects.csv",
    "activities": DATA_DIR / "activities.csv",
    "contracts": DATA_DIR / "contracts.csv",
    "cost_items": DATA_DIR / "cost_items.csv",
    "delay_events": DATA_DIR / "delay_events.csv",
    "risks": DATA_DIR / "risks.csv",
    "milestones": DATA_DIR / "milestones.csv",
    "payments": DATA_DIR / "payments.csv",
    "progress_updates": DATA_DIR / "progress_updates.csv",
    "change_orders": DATA_DIR / "change_orders.csv",
    "claims": DATA_DIR / "claims.csv",
    "wbs": DATA_DIR / "wbs.csv",
}


class CSVDataLoader:
    """Load and cache CSV data for dashboard."""
    
    def __init__(self):
        """Initialize data loader with cache."""
        self.cache = {}
        self.load_status = {}
    
    def load_csv(self, file_key: str, required: bool = False) -> Optional[pd.DataFrame]:
        """Load CSV file with caching.
        
        Args:
            file_key: Key in CSV_FILES dict
            required: If True, raise error if file not found
            
        Returns:
            DataFrame or None if file not found
        """
        # Return cached data if available
        if file_key in self.cache:
            return self.cache[file_key]
        
        # Get file path
        if file_key not in CSV_FILES:
            if required:
                raise ValueError(f"Unknown CSV file: {file_key}")
            return None
        
        file_path = CSV_FILES[file_key]
        
        # Check if file exists
        if not file_path.exists():
            self.load_status[file_key] = f"File not found: {file_path}"
            if required:
                raise FileNotFoundError(f"Required CSV file not found: {file_path}")
            return None
        
        try:
            # Load CSV
            df = pd.read_csv(file_path)
            self.cache[file_key] = df
            self.load_status[file_key] = f"Loaded: {len(df)} rows"
            return df
        except Exception as e:
            self.load_status[file_key] = f"Error loading: {str(e)}"
            if required:
                raise
            return None
    
    def get_projects(self) -> pd.DataFrame:
        """Get projects data."""
        df = self.load_csv("projects", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_activities(self) -> pd.DataFrame:
        """Get activities data."""
        df = self.load_csv("activities", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_contracts(self) -> pd.DataFrame:
        """Get contracts data."""
        df = self.load_csv("contracts", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_cost_items(self) -> pd.DataFrame:
        """Get cost items data."""
        df = self.load_csv("cost_items", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_delay_events(self) -> pd.DataFrame:
        """Get delay events data."""
        df = self.load_csv("delay_events", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_risks(self) -> pd.DataFrame:
        """Get risks data."""
        df = self.load_csv("risks", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_milestones(self) -> pd.DataFrame:
        """Get milestones data."""
        df = self.load_csv("milestones", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_payments(self) -> pd.DataFrame:
        """Get payments data."""
        df = self.load_csv("payments", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_progress_updates(self) -> pd.DataFrame:
        """Get progress updates data."""
        df = self.load_csv("progress_updates", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_change_orders(self) -> pd.DataFrame:
        """Get change orders data."""
        df = self.load_csv("change_orders", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_claims(self) -> pd.DataFrame:
        """Get claims data."""
        df = self.load_csv("claims", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_wbs(self) -> pd.DataFrame:
        """Get WBS data."""
        df = self.load_csv("wbs", required=False)
        if df is None:
            return pd.DataFrame()
        return df
    
    def get_load_status(self) -> Dict[str, str]:
        """Get status of all loaded files."""
        return self.load_status
    
    def reload_all(self):
        """Clear cache and reload all files."""
        self.cache.clear()
        self.load_status.clear()
        for key in CSV_FILES.keys():
            self.load_csv(key, required=False)


# Global loader instance
_loader = None


def get_loader() -> CSVDataLoader:
    """Get or create global loader instance."""
    global _loader
    if _loader is None:
        _loader = CSVDataLoader()
    return _loader


def reload_data():
    """Reload all CSV data."""
    get_loader().reload_all()
