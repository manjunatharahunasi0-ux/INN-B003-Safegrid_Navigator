# Historical Risk Analytics Feature - Implementation Documentation

## Overview
This document describes the newly implemented Historical Risk Analytics features for Safegrid Navigator, providing route-specific risk tracking and comparative analysis capabilities.

## What Was Added

### 1. Backend Enhancements

#### A. History Manager Updates (`src/core/history_manager.py`)
- **Enhanced `add_risk_entry()` method**: Now accepts optional route-specific parameters
  - `route_id`: Unique identifier for the route
  - `origin`: Origin location
  - `destination`: Destination location
  
- **New `get_route_history()` method**: Retrieves historical risk data filtered by route
  - Parameters: `origin`, `destination`, `days`
  - Returns filtered history based on route parameters
  
- **New `compare_routes()` method**: Compares risk profiles of multiple routes
  - Accepts list of routes with origin/destination pairs
  - Returns comparative statistics for each route

#### B. API Routes Updates (`src/api/routes.py`)
- **Updated `/api/calculate_risk` endpoint**: Now logs route-specific history
  - Automatically tracks risk calculations per route
  - Stores origin, destination, and route_id with each entry

- **New `/api/route_history` endpoint** (GET)
  - Parameters: `origin`, `destination`, `days`
  - Returns historical risk data for a specific route
  - Response includes full history array and metadata

- **New `/api/compare_routes` endpoint** (POST)
  - Accepts JSON body with routes array and days parameter
  - Returns comparison data for multiple routes
  - Enables side-by-side route analysis

### 2. Frontend Implementation

#### A. New Page: Route Analytics (`frontend/route-analytics.html`)

**Tab 1: Single Route Analysis**
- Input fields for origin and destination
- Time period selector (7, 14, 30, 60, 90 days)
- Key metrics display:
  - Average Risk Score
  - Risk Range (Min-Max)
  - Total Data Points
  - Risk Trend (Increasing/Decreasing)
- Interactive line chart showing:
  - Risk score percentage over time
  - High severity event count
  - Medium severity event count
- Export functionality (JSON format)

**Tab 2: Multi-Route Comparison**
- Dynamic route list builder
- Add/remove routes interface
- Side-by-side comparison cards showing:
  - Average Risk
  - Current Risk
  - Maximum Risk
  - Minimum Risk
  - Data Points
- Comparative line chart overlaying all routes
- Export functionality for comparison data

#### B. Navigation Updates
Updated navigation menus in all pages:
- `index.html`
- `analytics.html`
- `live-disruptions.html`

All pages now include link to the new Route Analytics page.

### 3. Data Structure

#### Risk History Entry (Enhanced)
```json
{
  "date": "2025-12-02",
  "timestamp": "2025-12-02T10:30:00",
  "risk_score": 0.65,
  "risk_level": "medium",
  "total_disruptions": 12,
  "high_severity_count": 3,
  "medium_severity_count": 5,
  "low_severity_count": 4,
  "route_id": "ROUTE-12345",
  "origin": "Shanghai",
  "destination": "Los Angeles"
}
```

## How to Use

### Single Route Analysis
1. Navigate to Route Analytics page
2. Enter origin city/port (e.g., "Shanghai")
3. Enter destination city/port (e.g., "Los Angeles")
4. Select time period (default: 30 days)
5. Click "Analyze" button
6. View risk metrics and historical chart
7. Optionally export data using "Export" button

### Route Comparison
1. Navigate to Route Analytics page
2. Click "Route Comparison" tab
3. Enter origin and destination for first route
4. Click "Add Route"
5. Repeat for additional routes (minimum 2 required)
6. Select comparison time period
7. Click "Compare Routes"
8. View side-by-side metrics and overlaid chart
9. Optionally export comparison data

## Key Benefits (PRD Alignment)

1. **Proactive Prediction**: Historical patterns help predict future risks
2. **Route-Specific Intelligence**: Eliminates noise by focusing on relevant corridors
3. **Actionable Insights**: Comparison enables optimal route selection
4. **Decision Support**: Trend analysis supports strategic planning

## API Documentation

### GET /api/route_history
**Parameters:**
- `origin` (string): Origin location
- `destination` (string): Destination location  
- `days` (integer, default: 30): Number of days to retrieve

**Response:**
```json
{
  "origin": "Shanghai",
  "destination": "Los Angeles",
  "history": [...],
  "total_records": 15
}
```

### POST /api/compare_routes
**Request Body:**
```json
{
  "routes": [
    {"origin": "Shanghai", "destination": "Los Angeles"},
    {"origin": "Singapore", "destination": "Rotterdam"}
  ],
  "days": 30
}
```

## Files Modified/Created

### Modified Files:
1. `src/core/history_manager.py` - Enhanced with route-specific methods
2. `src/api/routes.py` - Added new endpoints and updated logging
3. `frontend/index.html` - Updated navigation
4. `frontend/analytics.html` - Updated navigation
5. `frontend/live-disruptions.html` - Updated navigation

### New Files:
1. `frontend/route-analytics.html` - Complete new analytics interface
2. `documentation/HISTORICAL_RISK_ANALYTICS.md` - This documentation
