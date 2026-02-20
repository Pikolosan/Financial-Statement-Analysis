"""
Generate Sample Financial Data for Dashboard
=============================================
This script creates realistic sample financial data and updates the dashboard.
Once you have your actual financial_source.xlsx, you can use the other script.

Usage:
    python generate_sample_data.py
"""

import json
from pathlib import Path


def generate_sample_data():
    """Generate realistic financial sample data"""
    
    print("📊 Generating sample financial data...\n")
    
    # Sample Business Segment data
    segment_data = {
        'business_segment': {
            'labels': ['Primary IT Services', 'Cloud Solutions', 'Consulting', 'Other'],
            'values': [450000, 380000, 145000, 25000]
        },
        
        # Sample Regional data
        'region': {
            'labels': ['North America', 'Europe', 'Asia Pacific', 'Others'],
            'values': [420000, 350000, 210000, 20000]
        },
        
        # Sample 5-year trend
        'revenue_profit_trend': {
            'period': ['2018', '2019', '2020', '2021', '2022'],
            'revenue': [850000, 950000, 1050000, 1150000, 1350000],
            'profit': [125000, 165000, 195000, 245000, 310000]
        },
        
        # Sample quarterly data
        'revenue_cost': {
            'period': ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022'],
            'revenue': [280000, 320000, 350000, 400000],
            'costs': [182000, 208000, 227500, 260000]
        },
        
        # Sample cash flow
        'cash_flow': {
            'period': ['2018', '2019', '2020', '2021', '2022'],
            'operating': [95000, 115000, 140000, 175000, 220000],
            'investing': [-45000, -55000, -62000, -75000, -95000]
        },
        
        # Sample balance sheet
        'balance_sheet': {
            'categories': ['Total Assets', 'Total Liabilities', 'Shareholders Equity'],
            'values': [3375000, 1012500, 2362500]
        }
    }
    
    print("✅ Generated sample data:")
    print("  • Business Segments: 4 segments")
    print("  • Regions: 4 regions")
    print("  • Revenue Trend: 5 years (2018-2022)")
    print("  • Quarterly Data: 4 quarters in 2022")
    print("  • Cash Flow: 5 years")
    print("  • Balance Sheet: Assets, Liabilities, Equity\n")
    
    return segment_data


def save_data_to_json(data, filename='data.json'):
    """Save data to JSON file"""
    
    print(f"💾 Saving to {filename}...")
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Saved to {filename}\n")


def update_index_html(data):
    """Update index.html with sample data"""
    
    print("🔄 Updating index.html with sample data...")
    
    html_file = Path('index.html')
    
    if not html_file.exists():
        print("⚠️  index.html not found. Creating a new one...\n")
        create_index_html(data)
        return
    
    # Read current HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Create data JSON string for embedding
    data_json = json.dumps(data, indent=8)
    
    # Create new script section with actual data
    new_script = f"""    <script>
        // Sample financial data - replace with your actual data
        const dashboardData = {data_json};

        function createBusinessSegmentChart() {{
            const data = [{{
                labels: dashboardData.business_segment.labels,
                values: dashboardData.business_segment.values,
                type: 'pie',
                marker: {{ colors: ['#667eea', '#764ba2', '#f0ad4e', '#28a745'] }}
            }}];

            const layout = {{
                title: 'Business Segment Distribution (2022)',
                height: 400,
                margin: {{ l: 0, r: 0, t: 30, b: 0 }}
            }};

            Plotly.newPlot('chart-business-segment', data, layout, {{ responsive: true }});
        }}

        function createRegionChart() {{
            const data = [{{
                labels: dashboardData.region.labels,
                values: dashboardData.region.values,
                type: 'pie',
                marker: {{ colors: ['#667eea', '#764ba2', '#f0ad4e', '#28a745'] }}
            }}];

            const layout = {{
                title: 'Revenue by Region (2022)',
                height: 400,
                margin: {{ l: 0, r: 0, t: 30, b: 0 }}
            }};

            Plotly.newPlot('chart-region', data, layout, {{ responsive: true }});
        }}

        function createRevenueProfitChart() {{
            const trace1 = {{
                x: dashboardData.revenue_profit_trend.period,
                y: dashboardData.revenue_profit_trend.revenue,
                name: 'Revenue',
                type: 'scatter',
                mode: 'lines+markers',
                line: {{ color: '#667eea', width: 3 }},
                marker: {{ size: 8 }},
                fill: 'tozeroy'
            }};

            const trace2 = {{
                x: dashboardData.revenue_profit_trend.period,
                y: dashboardData.revenue_profit_trend.profit,
                name: 'Profit',
                type: 'scatter',
                mode: 'lines+markers',
                line: {{ color: '#764ba2', width: 3 }},
                marker: {{ size: 8 }}
            }};

            const layout = {{
                title: 'Revenue vs Profit Trend (5-Year)',
                xaxis: {{ title: 'Year' }},
                yaxis: {{ title: 'Amount ($)' }},
                hovermode: 'x unified',
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};

            Plotly.newPlot('chart-revenue-profit', [trace1, trace2], layout, {{ responsive: true }});
        }}

        function createRevenueCostChart() {{
            const trace1 = {{
                x: dashboardData.revenue_cost.period,
                y: dashboardData.revenue_cost.revenue,
                name: 'Revenue',
                type: 'bar',
                marker: {{ color: '#667eea' }}
            }};

            const trace2 = {{
                x: dashboardData.revenue_cost.period,
                y: dashboardData.revenue_cost.costs,
                name: 'Costs',
                type: 'bar',
                marker: {{ color: '#f0ad4e' }}
            }};

            const layout = {{
                title: 'Revenue vs Cost (2022 Quarterly)',
                barmode: 'group',
                xaxis: {{ title: 'Quarter' }},
                yaxis: {{ title: 'Amount ($)' }},
                hovermode: 'x unified',
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};

            Plotly.newPlot('chart-revenue-cost', [trace1, trace2], layout, {{ responsive: true }});
        }}

        function createCashFlowChart() {{
            const trace1 = {{
                x: dashboardData.cash_flow.period,
                y: dashboardData.cash_flow.operating,
                name: 'Operating Cash Flow',
                type: 'scatter',
                mode: 'lines+markers',
                fill: 'tozeroy',
                line: {{ color: '#667eea', width: 2 }},
                marker: {{ size: 6 }}
            }};

            const trace2 = {{
                x: dashboardData.cash_flow.period,
                y: dashboardData.cash_flow.investing,
                name: 'Investing Cash Flow',
                type: 'scatter',
                mode: 'lines+markers',
                fill: 'tozeroy',
                line: {{ color: '#f0ad4e', width: 2 }},
                marker: {{ size: 6 }}
            }};

            const layout = {{
                title: 'Cash Flow Performance (5-Year)',
                xaxis: {{ title: 'Year' }},
                yaxis: {{ title: 'Cash Flow ($)' }},
                hovermode: 'x unified',
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};

            Plotly.newPlot('chart-cash-flow', [trace1, trace2], layout, {{ responsive: true }});
        }}

        function createBalanceSheetChart() {{
            const data = [{{
                x: dashboardData.balance_sheet.categories,
                y: dashboardData.balance_sheet.values,
                type: 'bar',
                marker: {{ color: ['#667eea', '#f0ad4e', '#764ba2'] }}
            }}];

            const layout = {{
                title: 'Balance Sheet Overview (2022)',
                xaxis: {{ title: 'Category' }},
                yaxis: {{ title: 'Amount ($)' }},
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};

            Plotly.newPlot('chart-balance-sheet', data, layout, {{ responsive: true }});
        }}

        // Initialize all charts when page loads
        document.addEventListener('DOMContentLoaded', function() {{
            createBusinessSegmentChart();
            createRegionChart();
            createRevenueProfitChart();
            createRevenueCostChart();
            createCashFlowChart();
            createBalanceSheetChart();
        }});
    </script>"""
    
    # Find and replace script section
    import re
    
    script_pattern = r'<script>.*?// Initialize all charts when page loads.*?</script>'
    
    if re.search(script_pattern, html_content, re.DOTALL):
        html_content = re.sub(script_pattern, new_script, html_content, flags=re.DOTALL)
    else:
        html_content = html_content.replace('</body>', new_script + '\n    </body>')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Updated index.html with sample data\n")


def create_index_html(data):
    """Create a new index.html if it doesn't exist"""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Statement Analysis Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }

        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }

        header p {
            font-size: 1.1em;
            opacity: 0.9;
        }

        .content {
            padding: 40px;
        }

        .chart-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        .chart-container {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .chart-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
        }

        .chart-title {
            font-size: 1.3em;
            font-weight: 600;
            color: #333;
            margin-bottom: 15px;
            text-align: center;
        }

        .chart {
            width: 100%;
            height: 400px;
        }

        .insights {
            background: #e7f3ff;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin-top: 40px;
            border-radius: 4px;
        }

        .insights h2 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.3em;
        }

        .insights ul {
            margin-left: 20px;
            line-height: 1.8;
            color: #444;
        }

        .insights li {
            margin-bottom: 8px;
        }

        .sample-badge {
            display: inline-block;
            background: #fff3cd;
            color: #856404;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 0.9em;
            margin-top: 10px;
            border: 1px solid #ffeaa7;
        }

        footer {
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e0e0e0;
        }

        footer a {
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }

        footer a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8em;
            }

            .chart-grid {
                grid-template-columns: 1fr;
            }

            .content {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Financial Statement Analysis</h1>
            <p>Interactive Dashboard - Financial Performance Review</p>
            <div class="sample-badge">📊 Currently Displaying Sample Data</div>
        </header>

        <div class="content">
            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">Revenue by Business Segment</div>
                    <div id="chart-business-segment" class="chart"></div>
                </div>

                <div class="chart-container">
                    <div class="chart-title">Revenue by Region</div>
                    <div id="chart-region" class="chart"></div>
                </div>

                <div class="chart-container">
                    <div class="chart-title">Revenue vs Profit Trend</div>
                    <div id="chart-revenue-profit" class="chart"></div>
                </div>

                <div class="chart-container">
                    <div class="chart-title">Revenue vs Cost Analysis</div>
                    <div id="chart-revenue-cost" class="chart"></div>
                </div>

                <div class="chart-container">
                    <div class="chart-title">Cash Flow Performance</div>
                    <div id="chart-cash-flow" class="chart"></div>
                </div>

                <div class="chart-container">
                    <div class="chart-title">Balance Sheet Overview</div>
                    <div id="chart-balance-sheet" class="chart"></div>
                </div>
            </div>

            <div class="insights">
                <h2>Key Insights</h2>
                <ul>
                    <li>Primary IT Services represents the largest segment of revenue</li>
                    <li>North America is the dominant market with strongest growth</li>
                    <li>Consistent year-over-year revenue and profit growth trend</li>
                    <li>Positive operating cash flow demonstrating strong financial health</li>
                    <li>Healthy balance sheet with strong equity position</li>
                    <li>Cost control measures maintaining healthy profit margins</li>
                </ul>
            </div>
        </div>

        <footer>
            <p>Dashboard created with Plotly.js</p>
            <p>Replace sample data with your actual financial data when ready</p>
        </footer>
    </div>

"""
    
    # Add the script section
    data_json = json.dumps(data, indent=8)
    
    script = f"""    <script>
        const dashboardData = {data_json};

        function createBusinessSegmentChart() {{
            const data = [{{
                labels: dashboardData.business_segment.labels,
                values: dashboardData.business_segment.values,
                type: 'pie',
                marker: {{ colors: ['#667eea', '#764ba2', '#f0ad4e', '#28a745'] }}
            }}];
            const layout = {{
                title: 'Business Segment Distribution (2022)',
                height: 400,
                margin: {{ l: 0, r: 0, t: 30, b: 0 }}
            }};
            Plotly.newPlot('chart-business-segment', data, layout, {{ responsive: true }});
        }}

        function createRegionChart() {{
            const data = [{{
                labels: dashboardData.region.labels,
                values: dashboardData.region.values,
                type: 'pie',
                marker: {{ colors: ['#667eea', '#764ba2', '#f0ad4e', '#28a745'] }}
            }}];
            const layout = {{
                title: 'Revenue by Region (2022)',
                height: 400,
                margin: {{ l: 0, r: 0, t: 30, b: 0 }}
            }};
            Plotly.newPlot('chart-region', data, layout, {{ responsive: true }});
        }}

        function createRevenueProfitChart() {{
            const trace1 = {{
                x: dashboardData.revenue_profit_trend.period,
                y: dashboardData.revenue_profit_trend.revenue,
                name: 'Revenue',
                type: 'scatter',
                mode: 'lines+markers',
                line: {{ color: '#667eea', width: 3 }},
                marker: {{ size: 8 }},
                fill: 'tozeroy'
            }};
            const trace2 = {{
                x: dashboardData.revenue_profit_trend.period,
                y: dashboardData.revenue_profit_trend.profit,
                name: 'Profit',
                type: 'scatter',
                mode: 'lines+markers',
                line: {{ color: '#764ba2', width: 3 }},
                marker: {{ size: 8 }}
            }};
            const layout = {{
                title: 'Revenue vs Profit Trend (5-Year)',
                xaxis: {{ title: 'Year' }},
                yaxis: {{ title: 'Amount ($)' }},
                hovermode: 'x unified',
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};
            Plotly.newPlot('chart-revenue-profit', [trace1, trace2], layout, {{ responsive: true }});
        }}

        function createRevenueCostChart() {{
            const trace1 = {{
                x: dashboardData.revenue_cost.period,
                y: dashboardData.revenue_cost.revenue,
                name: 'Revenue',
                type: 'bar',
                marker: {{ color: '#667eea' }}
            }};
            const trace2 = {{
                x: dashboardData.revenue_cost.period,
                y: dashboardData.revenue_cost.costs,
                name: 'Costs',
                type: 'bar',
                marker: {{ color: '#f0ad4e' }}
            }};
            const layout = {{
                title: 'Revenue vs Cost (2022 Quarterly)',
                barmode: 'group',
                xaxis: {{ title: 'Quarter' }},
                yaxis: {{ title: 'Amount ($)' }},
                hovermode: 'x unified',
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};
            Plotly.newPlot('chart-revenue-cost', [trace1, trace2], layout, {{ responsive: true }});
        }}

        function createCashFlowChart() {{
            const trace1 = {{
                x: dashboardData.cash_flow.period,
                y: dashboardData.cash_flow.operating,
                name: 'Operating Cash Flow',
                type: 'scatter',
                mode: 'lines+markers',
                fill: 'tozeroy',
                line: {{ color: '#667eea', width: 2 }},
                marker: {{ size: 6 }}
            }};
            const trace2 = {{
                x: dashboardData.cash_flow.period,
                y: dashboardData.cash_flow.investing,
                name: 'Investing Cash Flow',
                type: 'scatter',
                mode: 'lines+markers',
                fill: 'tozeroy',
                line: {{ color: '#f0ad4e', width: 2 }},
                marker: {{ size: 6 }}
            }};
            const layout = {{
                title: 'Cash Flow Performance (5-Year)',
                xaxis: {{ title: 'Year' }},
                yaxis: {{ title: 'Cash Flow ($)' }},
                hovermode: 'x unified',
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};
            Plotly.newPlot('chart-cash-flow', [trace1, trace2], layout, {{ responsive: true }});
        }}

        function createBalanceSheetChart() {{
            const data = [{{
                x: dashboardData.balance_sheet.categories,
                y: dashboardData.balance_sheet.values,
                type: 'bar',
                marker: {{ color: ['#667eea', '#f0ad4e', '#764ba2'] }}
            }}];
            const layout = {{
                title: 'Balance Sheet Overview (2022)',
                xaxis: {{ title: 'Category' }},
                yaxis: {{ title: 'Amount ($)' }},
                plot_bgcolor: '#f8f9fa',
                paper_bgcolor: '#f8f9fa'
            }};
            Plotly.newPlot('chart-balance-sheet', data, layout, {{ responsive: true }});
        }}

        document.addEventListener('DOMContentLoaded', function() {{
            createBusinessSegmentChart();
            createRegionChart();
            createRevenueProfitChart();
            createRevenueCostChart();
            createCashFlowChart();
            createBalanceSheetChart();
        }});
    </script>"""
    
    html_content += script + "\n</body>\n</html>"
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Created new index.html with sample data\n")


def main():
    """Main execution"""
    
    print("=" * 60)
    print("Financial Dashboard Sample Data Generator")
    print("=" * 60 + "\n")
    
    # Generate sample data
    data = generate_sample_data()
    
    # Save to JSON
    save_data_to_json(data)
    
    # Update or create HTML
    update_index_html(data)
    
    print("=" * 60)
    print("✅ Dashboard Ready with Sample Data!")
    print("=" * 60)
    print("\n📊 Your interactive dashboard now includes:")
    print("   • Business Segment Distribution")
    print("   • Regional Revenue Analysis")
    print("   • 5-Year Revenue & Profit Trends")
    print("   • Quarterly Revenue vs Cost")
    print("   • Cash Flow Performance")
    print("   • Balance Sheet Overview")
    print("\n🎯 Next Steps:")
    print("   1. Open index.html in your browser to see it in action")
    print("   2. When you get your financial_source.xlsx:")
    print("      Run: python extract_and_update_dashboard.py")
    print("   3. Push to GitHub: git add . && git commit -m 'Add dashboard'")
    print("   4. Deploy to GitHub Pages for live viewing")
    print("\n" + "=" * 60 + "\n")


if __name__ == '__main__':
    main()
