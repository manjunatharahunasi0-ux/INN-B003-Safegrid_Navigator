# Safegrid Navigator

## Supply Chain Disruption Prediction & Optimization System

Safegrid Navigator is a proactive supply chain risk intelligence platform that uses AI/ML to predict disruptions and optimize logistics routes in real-time.

## Features

- 🌍 **Global Disruption Map**: Real-time visualization of worldwide supply chain disruptions
- 📊 **Route Risk Analysis**: AI-powered risk scoring for specific shipping routes
- 📈 **Historical Risk Analytics**: Track and compare route risk patterns over time (NEW!)
- 🎯 **Predictive Intelligence**: Early warning system for weather, conflicts, strikes, and port congestion
- 💡 **Actionable Recommendations**: Automated suggestions for route alternatives and risk mitigation
- 🗺️ **Interactive Mapping**: Visual route planning with disruption overlays
- ⚖️ **Multi-Route Comparison**: Compare risk profiles of multiple routes side-by-side (NEW!)
- 💾 **Data Export**: Export historical analysis and comparison data (NEW!)

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Navigate to the project directory:
```bash
cd C:\projects\SAFEGRID
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the backend server:
```bash
python app.py
```

2. Open the frontend:
   - Open `frontend/index.html` in your web browser
   - Or navigate to: `file:///C:/projects/SAFEGRID/frontend/index.html`

3. The API will be running at: `http://localhost:5000`

## Usage

### Main Interface (Home)
1. **Enter Route Details**:
   - Input origin city/port (e.g., "Shanghai", "Singapore")
   - Input destination city/port (e.g., "Los Angeles", "Rotterdam")
   - Click "Analyze Route Risk"

2. **View Results**:
   - Risk Score (0-100%)
   - Risk Level (Low/Medium/High)
   - Active disruptions affecting your route
   - Actionable recommendations
   - Visual route display on map

3. **Monitor Global Disruptions**:
   - Interactive map shows all active disruptions worldwide
   - Color-coded by severity (Green/Orange/Red)
   - Click markers for detailed information

### Analytics Dashboard
1. **View Global Trends**:
   - Navigate to "Analytics" page
   - See 30-day historical risk trends
   - View disruption type distribution
   - Check statistical summaries

### Route Analytics (NEW!)
1. **Single Route Analysis**:
   - Navigate to "Route Analytics" page
   - Enter origin and destination
   - Select time period (7-90 days)
   - View historical risk trends and metrics
   - Export data for further analysis

2. **Multi-Route Comparison**:
   - Switch to "Route Comparison" tab
   - Add multiple routes (2+)
   - Compare risk profiles side-by-side
   - View overlay chart of all routes
   - Export comparison data

### Live Disruptions Feed
- Real-time disruption updates
- Filter by severity or type
- Detailed event information

## Technology Stack

### Backend
- **Flask**: Lightweight web framework
- **Python**: Core logic and data processing
- **Pandas**: Data manipulation
- **Pydantic**: Data validation
- **Geopy**: Geocoding services

### Frontend
- **HTML/CSS/JavaScript**: Clean, modern interface
- **Leaflet.js**: Interactive mapping library
- **Chart.js**: Historical trend visualizations (NEW!)
- **OpenStreetMap**: Map tiles

### Data
- **JSON**: Historical risk storage
- **RESTful API**: Backend communication

## API Endpoints

### Health Check
```
GET /api/health
```

### Calculate Route Risk
```
POST /api/calculate_risk
Body: {
  "origin": "Shanghai",
  "destination": "Los Angeles"
}
```

### Get Global Disruptions
```
GET /api/global_map_data
```

### Get Risk History (NEW!)
```
GET /api/risk_history?days=30
```

### Get Route-Specific History (NEW!)
```
GET /api/route_history?origin=Shanghai&destination=Los Angeles&days=30
```

### Compare Multiple Routes (NEW!)
```
POST /api/compare_routes
Body: {
  "routes": [
    {"origin": "Shanghai", "destination": "Los Angeles"},
    {"origin": "Singapore", "destination": "Rotterdam"}
  ],
  "days": 30
}
```

### Get Statistics (NEW!)
```
GET /api/statistics
```

### Get Disruption History (NEW!)
```
GET /api/disruption_history?days=7
```

## Project Structure

```
SAFEGRID/
├── app.py                  # Main application runner
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── src/
│   ├── api/
│   │   └── routes.py      # API endpoints (enhanced with history)
│   ├── core/
│   │   ├── data_aggregator.py       # Data ingestion
│   │   ├── risk_engine.py           # Risk scoring logic
│   │   ├── history_manager.py       # Historical data tracking (NEW!)
│   │   └── recommendation_generator.py  # Recommendations
│   ├── models/
│   │   └── shipment_schema.py       # Data models
│   └── utils/
├── frontend/
│   ├── index.html         # Main interface
│   ├── analytics.html     # Global analytics dashboard
│   ├── route-analytics.html  # Route-specific analytics (NEW!)
│   └── live-disruptions.html  # Live disruption feed
├── data/
│   ├── raw/               # Raw data cache
│   └── processed/         # Historical data storage
│       ├── risk_history.json      # Risk history (NEW!)
│       └── disruption_history.json  # Disruption history (NEW!)
└── documentation/         # Project documentation (NEW!)
    ├── HISTORICAL_RISK_ANALYTICS.md  # Technical docs
    ├── QUICK_START_ANALYTICS.md      # User guide
    └── UPDATE_SUMMARY.md             # Update summary
```

## Risk Scoring Algorithm

The system calculates risk scores based on:

1. **Severity Weights**:
   - Low: 0.3
   - Medium: 0.6
   - High: 1.0

2. **Disruption Type Weights**:
   - Geopolitical Conflict: 1.0
   - Severe Weather: 0.9
   - Piracy: 0.85
   - Labor Strike: 0.8
   - Port Congestion: 0.7
   - Infrastructure Failure: 0.6

3. **Risk Rules**:
   - 2+ High severity disruptions → High Risk
   - Average score ≥ 0.7 → High Risk
   - Average score ≥ 0.4 → Medium Risk
   - Average score < 0.4 → Low Risk

## Disruption Types

The system monitors six categories of disruptions:

1. **Severe Weather**: Storms, hurricanes, floods
2. **Port Congestion**: Delays, capacity issues
3. **Labor Strike**: Worker actions, industrial disputes
4. **Geopolitical Conflict**: Political tensions, trade restrictions
5. **Infrastructure Failure**: Equipment breakdowns, power outages
6. **Piracy**: Security threats, armed incidents

## Future Enhancements

- ✅ **Historical route analysis** (COMPLETED!)
- ✅ **Multi-route comparison** (COMPLETED!)
- Integration with real-time weather APIs (OpenWeatherMap)
- Live news feed aggregation
- Machine learning model for disruption prediction
- Predictive risk forecasting with ML
- Multi-modal transport optimization
- ERP system integration
- Mobile application
- Email/SMS alert system
- PDF report generation
- Advanced data export (CSV, Excel)

## Recent Updates

### v1.1.0 - Historical Risk Analytics (December 2, 2025)
- ✨ Added route-specific historical tracking
- ✨ Interactive line charts for risk trends
- ✨ Multi-route comparison functionality
- ✨ Data export capabilities (JSON)
- ✨ New Route Analytics page
- 📊 Enhanced API with 5 new endpoints
- 📚 Comprehensive documentation

See `documentation/UPDATE_SUMMARY.md` for complete details.

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### CORS Issues
Make sure the backend is running before opening the frontend. If you still have issues, check that Flask-CORS is properly installed.

### Map Not Loading
Ensure you have an active internet connection as the map uses OpenStreetMap tiles.

## License

This project is developed for educational and demonstration purposes.

## Contact

For questions or feedback about Safegrid Navigator, please create an issue in the project repository.
