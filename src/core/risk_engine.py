import random
from typing import List, Dict, Tuple
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

class RiskEngine:
    """Calculate route risk scores based on disruption data"""
    
    def __init__(self):
        self.severity_weights = {
            "low": 0.3,
            "medium": 0.6,
            "high": 1.0
        }
        
        self.type_weights = {
            "severe_weather": 0.9,
            "port_congestion": 0.7,
            "labor_strike": 0.8,
            "geopolitical_conflict": 1.0,
            "infrastructure_failure": 0.6,
            "piracy": 0.85
        }
    
    def calculate_risk_score(self, disruptions: List[Dict], origin: str, destination: str) -> Tuple[float, str]:
        """
        Calculate overall risk score for a route
        Returns: (risk_score, risk_level)
        """
        if not disruptions:
            return 0.2, "low"
        
        total_score = 0
        high_severity_count = 0
        
        for disruption in disruptions:
            severity = disruption.get("severity", "low")
            disruption_type = disruption.get("type", "")
            
            # Calculate weighted score
            severity_weight = self.severity_weights.get(severity, 0.3)
            type_weight = self.type_weights.get(disruption_type, 0.5)
            
            disruption_score = severity_weight * type_weight
            total_score += disruption_score
            
            if severity == "high":
                high_severity_count += 1
        
        # Average score
        avg_score = total_score / len(disruptions)
        
        # Apply rule: if 2+ high severity factors, overall risk is high
        if high_severity_count >= 2:
            return 0.85, "high"
        
        # Determine risk level based on average score
        if avg_score >= 0.7:
            risk_level = "high"
        elif avg_score >= 0.4:
            risk_level = "medium"
        else:
            risk_level = "low"
        
        # Normalize score to 0-1 range
        normalized_score = min(avg_score, 1.0)
        
        return normalized_score, risk_level
    
    def get_risk_breakdown(self, disruptions: List[Dict]) -> Dict[str, int]:
        """Get count of disruptions by type"""
        breakdown = {}
        for disruption in disruptions:
            d_type = disruption.get("type", "unknown")
            breakdown[d_type] = breakdown.get(d_type, 0) + 1
        return breakdown
    
    def get_location_coordinates(self, location: str) -> Tuple[float, float]:
        """Get lat/lon for a location using geocoding"""
        try:
            geolocator = Nominatim(user_agent="safegrid_navigator")
            location_data = geolocator.geocode(location)
            if location_data:
                return location_data.latitude, location_data.longitude
        except:
            pass
        
        # Fallback to major cities
        fallback_coords = {
            "shanghai": (31.2304, 121.4737),
            "singapore": (1.3521, 103.8198),
            "rotterdam": (51.9244, 4.4777),
            "los angeles": (34.0522, -118.2437),
            "new york": (40.7128, -74.0060),
            "london": (51.5074, -0.1278),
            "tokyo": (35.6762, 139.6503),
            "dubai": (25.2048, 55.2708)
        }
        
        location_lower = location.lower()
        for city, coords in fallback_coords.items():
            if city in location_lower:
                return coords
        
        return 0.0, 0.0
