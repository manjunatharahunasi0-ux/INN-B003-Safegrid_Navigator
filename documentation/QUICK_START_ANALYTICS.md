# Safegrid Navigator - Historical Risk Analytics Quick Start Guide

## What's New? 🎉

Safegrid Navigator now includes **Route-Specific Historical Risk Analytics** - a powerful feature that tracks and compares risk patterns over time for your logistics routes.

## Key Features

### 1. 📊 Historical Risk Line Charts
- Visualize risk trends over 7, 14, 30, 60, or 90 days
- Track high, medium, and low severity disruptions
- See how risk levels change over time
- Identify patterns and seasonal variations

### 2. 🛣️ Route-Specific Tracking  
- Every risk calculation is automatically saved
- Filter historical data by origin and destination
- View complete risk history for specific corridors
- Understand route-specific risk patterns

### 3. ⚖️ Multi-Route Comparison
- Compare up to 6 different routes side-by-side
- Overlay risk trends on a single chart
- Identify the safest corridor for your shipments
- Make data-driven routing decisions

### 4. 💾 Data Export
- Export analysis results as JSON
- Use data in external tools
- Share insights with your team
- Archive historical reports

## Quick Start

### View Global Risk Trends
1. Click **"Analytics"** in the navigation menu
2. See 30 days of global risk history by default
3. Use filter buttons to change time period (7/14/30 days)
4. View disruption type distribution chart

### Analyze a Specific Route
1. Navigate to **"Route Analytics"**
2. Enter your **Origin** (e.g., "Shanghai")
3. Enter your **Destination** (e.g., "Los Angeles")
4. Select time period from dropdown
5. Click **"Analyze"** button
6. View metrics: Average Risk, Risk Range, Trend, Data Points
7. See the interactive line chart with historical risk data

### Compare Multiple Routes
1. Go to **"Route Analytics"** → **"Route Comparison"** tab
2. Enter first route (Origin + Destination)
3. Click **"Add Route"**
4. Repeat for more routes (minimum 2 required)
5. Select comparison time period
6. Click **"Compare Routes"**
7. View side-by-side comparison cards
8. Analyze the overlay chart showing all routes

## Understanding the Charts

### Line Chart Elements
- **Blue Line**: Risk Score percentage (0-100%)
- **Red Line**: High severity disruption count
- **Orange Line**: Medium severity disruption count
- **Left Y-Axis**: Risk Score percentage
- **Right Y-Axis**: Disruption count
- **X-Axis**: Date

### Risk Levels
- **0-40%**: Low Risk (Green) ✅
- **40-70%**: Medium Risk (Yellow) ⚠️
- **70-100%**: High Risk (Red) ❌

## Tips for Best Results

### 1. Build Your History
- Perform risk calculations regularly to build historical data
- More data points = better trend analysis
- Use consistent origin/destination names

### 2. Comparative Analysis
- Compare similar routes (same general direction)
- Look for consistent patterns across time
- Consider external factors (seasons, geopolitical events)

### 3. Use Trends for Planning
- **Increasing Trend**: Consider alternative routes or buffers
- **Decreasing Trend**: Potential opportunity for optimization
- **Volatile Pattern**: Plan for contingencies

### 4. Export and Share
- Export data before making presentations
- Share JSON files with team members
- Keep archive of historical analysis

## Common Use Cases

### Supply Chain Planning
```
Scenario: Planning Q1 shipments from Asia to Europe

Steps:
1. Compare 3 routes: Shanghai→Rotterdam, Singapore→Rotterdam, Busan→Hamburg
2. Analyze 30-day trends
3. Identify lowest average risk route
4. Factor in current risk level
5. Make routing decision
```

### Risk Monitoring
```
Scenario: Monitor critical route performance

Steps:
1. Analyze specific route weekly
2. Track trend direction
3. Set threshold (e.g., >70% risk)
4. Export data for reports
5. Adjust strategy as needed
```

### Route Optimization
```
Scenario: Find alternative to high-risk corridor

Steps:
1. Analyze current route
2. Identify alternative routes
3. Compare historical performance
4. Consider min/max risk ranges
5. Select optimal alternative
```

## Troubleshooting

**Q: I see "No historical data found"**  
A: This route hasn't been analyzed yet. Perform a risk calculation on the main page first.

**Q: Chart is empty**  
A: Ensure you've selected a route with existing history. Try a longer time period.

**Q: Export button doesn't work**  
A: Check your browser's popup blocker settings and allow downloads.

**Q: Comparison shows incomplete data**  
A: Some routes may have more data points than others. This is normal if they've been analyzed at different frequencies.

## Navigation Guide

### Main Pages
1. **Home** - Perform new risk calculations
2. **Analytics** - View global risk trends and statistics
3. **Route Analytics** - Analyze and compare specific routes (NEW!)
4. **Live Feed** - See real-time disruption events

### Route Analytics Tabs
1. **Single Route Analysis** - Focus on one corridor
2. **Route Comparison** - Compare multiple routes

## Data Retention

- Historical data retained: **90 days**
- Automatic cleanup: Old entries removed
- Sample data: Generated on first use
- Manual export: Keep data indefinitely

## Getting Help

- Check console logs for errors (F12 in browser)
- Ensure backend server is running
- Verify API endpoints are accessible
- Review documentation folder for details

## Next Steps

1. ✅ Start using Route Analytics today
2. 📈 Build your historical database
3. 🔍 Identify route patterns
4. 📊 Make data-driven decisions
5. 💡 Share insights with your team

---

**Remember**: The more you use Safegrid Navigator, the more valuable your historical data becomes! Regular risk calculations build a comprehensive database for strategic planning.

For technical details, see `HISTORICAL_RISK_ANALYTICS.md` in the documentation folder.
