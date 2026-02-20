# Website Dashboard Setup Guide

## Overview
Your interactive dashboard website has been created with sample data. Follow these steps to populate it with your actual financial data and deploy it to GitHub Pages.

## Step 1: Export Data from Jupyter Notebooks

You need to export your data in JSON format from your Jupyter notebooks. Add this code to each notebook after your analysis:

### Example: Export Business Segment Data
```python
import json

# After your analysis, convert dataframe to dictionary
business_segment_data = {
    'labels': filter_df['Operating_Segment'].tolist(),
    'values': filter_df['Revenue'].tolist()
}

# Save to JSON
with open('business_segment.json', 'w') as f:
    json.dump(business_segment_data, f)
```

### Export Multiple Data Sources
Create a Python script (e.g., `export_data.py`) to export all your data:

```python
import json
import pandas as pd

# Read your processed data
# (Adjust paths based on your actual data sources)

export_data = {
    'business_segment': {
        'labels': ['IT Business A', 'IT Business B', 'Other'],
        'values': [45, 52, 3]
    },
    'region': {
        'labels': ['Domestic', 'International', 'Emerging Markets'],
        'values': [40, 45, 15]
    },
    'revenue_profit_trend': {
        'years': ['2018', '2019', '2020', '2021', '2022'],
        'revenue': [100, 125, 140, 165, 190],
        'profit': [20, 28, 32, 42, 55]
    },
    'revenue_cost': {
        'quarters': ['Q1', 'Q2', 'Q3', 'Q4'],
        'revenue': [45, 52, 48, 55],
        'costs': [30, 35, 33, 37]
    },
    'cash_flow': {
        'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'operating': [5, 8, 6, 10, 9, 12, 11, 13, 10, 12, 14, 16],
        'investing': [-3, -2, -4, -3, -5, -2, -3, -4, -2, -3, -2, -1]
    },
    'balance_sheet': {
        'categories': ['Assets', 'Liabilities', 'Equity'],
        'values': [500, 200, 300]
    }
}

with open('data.json', 'w') as f:
    json.dump(export_data, f, indent=2)
```

## Step 2: Update index.html with Your Data

Replace the sample data in `index.html` with your actual data. Find these functions:

- `createBusinessSegmentChart()`
- `createRegionChart()`
- `createRevenueProfitChart()`
- `createRevenueCostChart()`
- `createCashFlowChart()`
- `createBalanceSheetChart()`

### Option A: Direct Data Update
Replace the hardcoded values with your actual data:

```javascript
function createBusinessSegmentChart() {
    const data = [{
        labels: ['Your Segment 1', 'Your Segment 2', 'Other'],
        values: [your_value1, your_value2, your_value3],
        // ... rest of config
    }];
    // ...
}
```

### Option B: Load from JSON File (Advanced)
Create a `data.json` file in the same directory and load it:

```javascript
// Add this to load data from JSON
async function loadData() {
    const response = await fetch('data.json');
    const data = await response.json();
    
    createBusinessSegmentChart(data.business_segment);
    createRegionChart(data.region);
    // ... etc
}

document.addEventListener('DOMContentLoaded', loadData);
```

## Step 3: Set Up GitHub Repository

### 3a. Create GitHub Account
If you don't have one, go to [github.com](https://github.com) and create a free account.

### 3b. Create a New Repository
1. Click "+" → "New repository"
2. Name it: `financial-analysis-dashboard` (or any name)
3. Choose "Public"
4. **Check**: "Add a README file"
5. Click "Create repository"

### 3c. Upload Your Files
You have two options:

**Option 1: Web Upload (Easiest)**
1. Click "Add file" → "Upload files"
2. Select your files:
   - `index.html`
   - `data.json` (if using)
   - Any image assets you want to include
3. Click "Commit changes"

**Option 2: Git Command Line**
```bash
# Navigate to your project folder
cd "c:\Users\Parth J Chaudhary\Documents\CODE\Projects\DataProjects\Financial Statement Analysis"

# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Add financial dashboard website"

# Add remote (replace USERNAME and REPO with your GitHub username and repo name)
git remote add origin https://github.com/USERNAME/financial-analysis-dashboard.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to "Pages" section
4. Under "Source", select "main" branch
5. Click "Save"
6. GitHub will generate a URL like: `https://USERNAME.github.io/financial-analysis-dashboard`

Your website will be live in a few seconds!

## Step 5: Update Your README

Add this to your main README.md:

```markdown
## Interactive Dashboard Website

View the interactive financial analysis dashboard here:
[Financial Statement Analysis Dashboard](https://USERNAME.github.io/financial-analysis-dashboard)

This dashboard provides:
- Revenue analysis by business segment
- Regional revenue distribution
- 5-year revenue and profit trends
- Cost vs revenue comparison
- Cash flow analysis
- Balance sheet overview
```

## Updating Your Dashboard

To update the dashboard with new data:

1. Update your data in `data.json` or modify the JavaScript data
2. Commit the changes:
   ```bash
   git add .
   git commit -m "Update dashboard data"
   git push
   ```
3. GitHub Pages will automatically redeploy within seconds

## Tips

- Keep your `index.html` file updated with the latest data exports from your Jupyter notebooks
- Use `data.json` for larger datasets or frequent updates
- Test locally by opening `index.html` in your browser before pushing to GitHub
- Customize colors, fonts, and layout by editing the CSS in the `<style>` section
- Add more charts by creating new functions and chart containers

## Troubleshooting

**Dashboard not showing?**
- Wait 5 minutes after enabling GitHub Pages
- Check that `index.html` is in the root directory
- Clear browser cache (Ctrl+Shift+Delete)

**Data not loading from JSON?**
- Ensure `data.json` is in the same directory as `index.html`
- Check browser console (F12) for errors
- Use absolute paths if loading from subdirectories

**Charts not rendering?**
- Verify Plotly.js CDN is accessible (check internet connection)
- Check that data format matches the expected structure
- Open browser console (F12) to see error messages

---

Need help? Check the [Plotly.js documentation](https://plotly.com/javascript/) for customizing charts.
