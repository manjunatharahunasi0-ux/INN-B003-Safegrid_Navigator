# SAFEGRID NAVIGATOR - QUICK START GUIDE

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies
Open Command Prompt or PowerShell in the project directory and run:
```bash
cd C:\projects\SAFEGRID
pip install -r requirements.txt
```

### Step 2: Start the Backend Server
Double-click `start.bat` or run in terminal:
```bash
python app.py
```

You should see:
```
🚀 Starting Safegrid Navigator
Backend API: http://localhost:5000
Frontend: Open frontend/index.html in your browser
```

### Step 3: Open the Frontend
Open `C:\projects\SAFEGRID\frontend\index.html` in your web browser
(Chrome, Firefox, or Edge recommended)

## 📊 Using the Application

### Analyze a Route:
1. Enter **Origin** (e.g., "Shanghai", "Singapore", "Rotterdam")
2. Enter **Destination** (e.g., "Los Angeles", "New York", "London")
3. Click **"Analyze Route Risk"**

### View Results:
- **Risk Score**: Overall risk percentage (0-100%)
- **Risk Level**: Low (Green) / Medium (Orange) / High (Red)
- **Active Disruptions**: List of issues affecting your route
- **Recommendations**: Actionable advice for risk mitigation
- **Interactive Map**: Visual route with disruption markers

### Map Features:
- **Green markers**: Low severity disruptions
- **Orange markers**: Medium severity disruptions
- **Red markers**: High severity disruptions
- **Blue/Green line**: Your analyzed route (color-coded by risk)
- Click any marker to see disruption details

## 🎯 Example Routes to Try

1. **Shanghai → Los Angeles** (Trans-Pacific route)
2. **Rotterdam → New York** (Trans-Atlantic route)
3. **Singapore → Dubai** (Asia-Middle East route)
4. **Hong Kong → London** (Long-distance global route)

## 🔧 Troubleshooting

### Problem: "Module not found" errors
**Solution**: Make sure you installed dependencies:
```bash
pip install -r requirements.txt
```

### Problem: Port 5000 already in use
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Then update API_BASE in `frontend/index.html`:
```javascript
const API_BASE = 'http://localhost:5001/api';
```

### Problem: Map not loading
**Solution**: 
- Check internet connection (map needs OpenStreetMap)
- Make sure backend is running first
- Try refreshing the browser (Ctrl+F5)

### Problem: CORS errors in browser console
**Solution**: 
- Ensure Flask-CORS is installed
- Make sure backend is running before opening frontend

## 📁 Project Files

- `app.py` - Main application entry point
- `start.bat` - Windows startup script
- `requirements.txt` - Python dependencies
- `frontend/index.html` - Web interface
- `src/api/routes.py` - API endpoints
- `src/core/` - Core business logic
  - `data_aggregator.py` - Data collection
  - `risk_engine.py` - Risk calculation
  - `recommendation_generator.py` - Advice generation

## 🌐 API Endpoints

Test the API directly:

**Health Check:**
```
http://localhost:5000/api/health
```

**Global Disruptions:**
```
http://localhost:5000/api/global_map_data
```

**Calculate Risk (POST):**
```
http://localhost:5000/api/calculate_risk
Body: {"origin": "Shanghai", "destination": "Los Angeles"}
```

## 💡 Tips

1. **Real-time Updates**: The map refreshes disruptions every 5 minutes
2. **Multiple Analyses**: You can analyze different routes without restarting
3. **Zoom**: Use mouse wheel to zoom in/out on the map
4. **Details**: Click disruption markers for more information
5. **Mobile**: The interface is responsive and works on tablets

## 📞 Need Help?

Check the main README.md for detailed documentation or review the code comments in the source files.

---
**Made for Supply Chain Risk Intelligence** 🌍📦🚢
