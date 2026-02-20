"""
Data Export Helper Script
========================
Use this script in your Jupyter notebooks to export data for the dashboard.
Run this in a cell after your data analysis is complete.
"""

import json
import pandas as pd
from pathlib import Path

class DashboardDataExporter:
    """Helper class to export financial analysis data to JSON format"""
    
    def __init__(self, output_dir=None):
        """
        Initialize exporter
        
        Args:
            output_dir (str): Directory to save JSON files. Defaults to current directory.
        """
        self.output_dir = Path(output_dir) if output_dir else Path.cwd()
        self.output_dir.mkdir(exist_ok=True)
        self.data = {}
    
    def add_segment_data(self, df, segment_col, revenue_col, name='business_segment'):
        """
        Export business segment data
        
        Args:
            df (DataFrame): Input dataframe
            segment_col (str): Column name for segments
            revenue_col (str): Column name for revenue
            name (str): Key name for storing data
        """
        self.data[name] = {
            'labels': df[segment_col].tolist(),
            'values': df[revenue_col].tolist()
        }
        print(f"✓ Added {name} data")
        return self
    
    def add_region_data(self, df, region_col, revenue_col, name='region'):
        """Export region data"""
        self.data[name] = {
            'labels': df[region_col].tolist(),
            'values': df[revenue_col].tolist()
        }
        print(f"✓ Added {name} data")
        return self
    
    def add_trend_data(self, df, time_col, metric_cols, name='trend'):
        """
        Export trend data
        
        Args:
            df (DataFrame): Input dataframe
            time_col (str): Column with time period (year, quarter, month)
            metric_cols (dict): Dict mapping metric names to column names
                                e.g., {'revenue': 'Revenue', 'profit': 'Profit'}
            name (str): Key name for storing data
        """
        self.data[name] = {'period': df[time_col].tolist()}
        for metric_name, col_name in metric_cols.items():
            self.data[name][metric_name] = df[col_name].tolist()
        print(f"✓ Added {name} data")
        return self
    
    def add_custom_data(self, name, data_dict):
        """
        Add custom data
        
        Args:
            name (str): Key name
            data_dict (dict): Custom data dictionary
        """
        self.data[name] = data_dict
        print(f"✓ Added {name} data")
        return self
    
    def save(self, filename='dashboard_data.json'):
        """
        Save all data to JSON file
        
        Args:
            filename (str): Output filename
        """
        output_path = self.output_dir / filename
        with open(output_path, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f"\n✅ Data exported to: {output_path}")
        return self
    
    def view_data(self):
        """Display current data structure"""
        print("\nCurrent Data Structure:")
        print(json.dumps(self.data, indent=2))
        return self


# ============================================================
# USAGE EXAMPLES IN JUPYTER NOTEBOOKS
# ============================================================

"""
EXAMPLE 1: Simple Segment Export
---------------------------------

In your 1_business_segment_operating.ipynb notebook, add:

```python
from dashboard_data_exporter import DashboardDataExporter

# After your data analysis
exporter = DashboardDataExporter()
exporter.add_segment_data(
    df=filter_df,  # Your filtered dataframe
    segment_col='Operating_Segment',
    revenue_col='Revenue',
    name='business_segment'
).save()
```

---

EXAMPLE 2: Multiple Data Exports
---------------------------------

To export all dashboard data:

```python
from dashboard_data_exporter import DashboardDataExporter

# Initialize exporter
exporter = DashboardDataExporter()

# Add business segment data
exporter.add_segment_data(
    df=segment_df,
    segment_col='Operating_Segment',
    revenue_col='Revenue'
)

# Add region data
exporter.add_region_data(
    df=region_df,
    region_col='Region',
    revenue_col='Revenue'
)

# Add trend data (multiple columns)
exporter.add_trend_data(
    df=yearly_df,
    time_col='Year',
    metric_cols={'revenue': 'Revenue', 'profit': 'Profit', 'costs': 'Total_Costs'}
)

# Add custom data
exporter.add_custom_data('balance_sheet', {
    'categories': ['Assets', 'Liabilities', 'Equity'],
    'values': [500, 200, 300]
})

# Save to file
exporter.save('dashboard_data.json')
```

---

EXAMPLE 3: Export with Custom Date Formatting
----------------------------------------------

```python
from dashboard_data_exporter import DashboardDataExporter

exporter = DashboardDataExporter()

# Convert dates to strings for JSON compatibility
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

exporter.add_trend_data(
    df=df,
    time_col='Date',
    metric_cols={
        'cash_flow': 'Cash_Flow',
        'operating_cf': 'Operating_CF',
        'investing_cf': 'Investing_CF'
    }
).save('cash_flow_data.json')
```

---

EXAMPLE 4: Export All Quarterly Data
--------------------------------------

```python
from dashboard_data_exporter import DashboardDataExporter

exporter = DashboardDataExporter()

exporter.add_trend_data(
    df=quarterly_df,
    time_col='Quarter',
    metric_cols={
        'revenue': 'Revenue',
        'costs': 'Costs',
        'profit': 'Profit',
        'cash_flow': 'Cash_Flow'
    }
).save('quarterly_data.json')
```

"""
