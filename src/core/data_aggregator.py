import requests
import random
from datetime import datetime
from typing import List, Dict
import json

class DataAggregator:
    """Handles data ingestion from external sources"""
    
    def __init__(self):
        self.disruption_types = [
            "severe_weather", "port_congestion", "labor_strike", 
            "geopolitical_conflict", "infrastructure_failure", "piracy"
        ]
        self.severities = ["low", "medium", "high"]
    
    def fetch_weather_data(self, location: str) -> Dict:
        """Fetch weather data for a location"""
        # Simulated weather data for hackathon demo
        weather_conditions = ["clear", "rain", "storm", "snow", "fog"]
        condition = random.choice(weather_conditions)
        
        severity = "low"
        if condition in ["storm", "snow"]:
            severity = random.choice(["medium", "high"])
        elif condition in ["rain", "fog"]:
            severity = random.choice(["low", "medium"])
        
        return {
            "location": location,
            "condition": condition,
            "severity": severity,
            "temperature": random.randint(-10, 40),
            "wind_speed": random.randint(0, 100)
        }
    
    def fetch_global_disruptions(self) -> List[Dict]:
        """Fetch simulated global disruption events"""
        disruptions = []
        
        # Major shipping chokepoints and ports
        critical_locations = [
            {"name": "Suez Canal", "lat": 30.5, "lon": 32.3},
            {"name": "Panama Canal", "lat": 9.0, "lon": -79.5},
            {"name": "Strait of Hormuz", "lat": 26.5, "lon": 56.3},
            {"name": "Port of Shanghai", "lat": 31.2, "lon": 121.5},
            {"name": "Port of Singapore", "lat": 1.3, "lon": 103.8},
            {"name": "Port of Rotterdam", "lat": 51.9, "lon": 4.5},
            {"name": "Port of Los Angeles", "lat": 33.7, "lon": -118.3},
            {"name": "Port of Hamburg", "lat": 53.5, "lon": 10.0},
            {"name": "Malacca Strait", "lat": 2.5, "lon": 101.5},
            {"name": "Port of Hong Kong", "lat": 22.3, "lon": 114.2},
            {"name": "Bab el-Mandeb", "lat": 12.6, "lon": 43.3},
            {"name": "English Channel", "lat": 50.3, "lon": -1.0}
        ]
        
        # Generate 8-15 random disruptions
        num_disruptions = random.randint(8, 15)
        
        for i in range(num_disruptions):
            location = random.choice(critical_locations)
            disruption_type = random.choice(self.disruption_types)
            severity = random.choice(self.severities)
            
            descriptions = {
                "severe_weather": f"Severe weather alert: {random.choice(['Hurricane', 'Typhoon', 'Storm', 'Heavy rainfall'])} affecting area",
                "port_congestion": f"Port congestion: {random.randint(2, 10)} day delays reported",
                "labor_strike": f"Labor strike: {random.choice(['Dock workers', 'Port staff', 'Customs officials'])} industrial action",
                "geopolitical_conflict": f"Geopolitical tension: {random.choice(['Border closure', 'Trade restrictions', 'Military activity'])} reported",
                "infrastructure_failure": f"Infrastructure issue: {random.choice(['Power outage', 'Equipment failure', 'System malfunction'])}",
                "piracy": f"Security alert: {random.choice(['Piracy incident', 'Armed robbery', 'Security threat'])} reported"
            }
            
            disruptions.append({
                "id": f"DISR-{i+1:04d}",
                "type": disruption_type,
                "severity": severity,
                "description": descriptions[disruption_type],
                "location": {
                    "name": location["name"],
                    "lat": location["lat"] + random.uniform(-2, 2),
                    "lon": location["lon"] + random.uniform(-2, 2)
                },
                "timestamp": datetime.now().isoformat()
            })
        
        return disruptions
    
    def get_route_specific_disruptions(self, origin: str, destination: str, all_disruptions: List[Dict]) -> List[Dict]:
        """Filter disruptions relevant to a specific route"""
        # For demo purposes, return a subset of disruptions
        # In production, this would use actual route corridors
        num_relevant = random.randint(2, min(5, len(all_disruptions)))
        return random.sample(all_disruptions, num_relevant)
