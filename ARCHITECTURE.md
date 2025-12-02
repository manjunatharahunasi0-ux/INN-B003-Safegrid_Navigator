# SAFEGRID NAVIGATOR - SYSTEM ARCHITECTURE

## Overview

Safegrid Navigator is a full-stack web application designed to provide real-time supply chain risk intelligence through an intuitive interface backed by intelligent risk assessment algorithms.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │  HTML/CSS/JavaScript + Leaflet.js Maps          │  │
│  │  - Route Input Forms                             │  │
│  │  - Interactive Global Disruption Map            │  │
│  │  - Risk Visualization Dashboard                  │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↓ HTTP REST API
┌─────────────────────────────────────────────────────────┐
│                     API LAYER                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Flask Web Framework                             │  │
│  │  - /api/health (Health check)                    │  │
│  │  - /api/calculate_risk (Route analysis)         │  │
│  │  - /api/global_map_data (Disruption feed)       │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                  BUSINESS LOGIC LAYER                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │    Data      │  │    Risk      │  │Recommendation│  │
│  │  Aggregator  │→│   Engine     │→│  Generator   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                    DATA LAYER                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Simulated Disruption Data                       │  │
│  │  (Weather, Conflicts, Strikes, Congestion, etc.) │  │
│  │  Future: Real APIs (OpenWeather, News feeds)     │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend Layer (HTML/CSS/JavaScript)

**File**: `frontend/index.html`

**Responsibilities**:
- User input collection (origin/destination)
- Risk visualization (scores, charts, badges)
- Interactive map rendering using Leaflet.js
- Real-time disruption marker display
- Route line drawing with risk-based coloring

**Key Technologies**:
- Leaflet.js for mapping
- OpenStreetMap for tile data
- Vanilla JavaScript for API communication
- CSS3 for modern, responsive design

**Features**:
- Color-coded risk badges (Green/Orange/Red)
- Disruption markers with popup details
- Animated route lines
- Auto-refresh every 5 minutes
- Responsive design for mobile/tablet

---

### 2. API Layer (Flask)

**File**: `src/api/routes.py`

**Endpoints**:


#### `/api/health` (GET)
- Returns server health status
- Used for monitoring and debugging

#### `/api/calculate_risk` (POST)
- **Input**: JSON with origin and destination
- **Process**: 
  1. Fetch global disruptions
  2. Filter route-specific disruptions
  3. Calculate risk score
  4. Generate recommendations
  5. Get geocoordinates
- **Output**: Complete risk assessment with route data

#### `/api/global_map_data` (GET)
- Returns all active global disruptions
- Includes location, type, severity, description
- Used to populate the global disruption map

**Technologies**:
- Flask: Lightweight Python web framework
- Flask-CORS: Enable cross-origin requests
- Pydantic: Data validation and serialization

---

### 3. Business Logic Layer

#### A. Data Aggregator (`src/core/data_aggregator.py`)

**Purpose**: Collect and structure disruption data

**Methods**:
- `fetch_weather_data(location)`: Simulates weather conditions
- `fetch_global_disruptions()`: Generates 8-15 random disruptions
- `get_route_specific_disruptions()`: Filters relevant disruptions

**Disruption Types**:
1. Severe Weather
2. Port Congestion
3. Labor Strike
4. Geopolitical Conflict
5. Infrastructure Failure
