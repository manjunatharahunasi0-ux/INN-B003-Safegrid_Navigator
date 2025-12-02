"""
History Manager - Stores and retrieves historical risk data
"""
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict
import random

class HistoryManager:
    """Manages historical risk data storage and retrieval"""
    
    def __init__(self, data_dir: str = "data/processed"):
        self.data_dir = data_dir
        self.history_file = os.path.join(data_dir, "risk_history.json")
        self.disruption_history_file = os.path.join(data_dir, "disruption_history.json")
        self._ensure_data_directory()
        self._initialize_sample_data()
    
    def _ensure_data_directory(self):
        """Ensure data directory exists"""
        os.makedirs(self.data_dir, exist_ok=True)
    
    def _initialize_sample_data(self):
        """Initialize with sample historical data if files don't exist"""
        if not os.path.exists(self.history_file):
            # Generate 30 days of sample data
            sample_data = []
            base_date = datetime.now() - timedelta(days=30)
            
            for i in range(30):
                date = base_date + timedelta(days=i)
                # Simulate varying risk levels over time
                base_risk = 0.3 + (i % 10) * 0.05
                risk_variation = random.uniform(-0.1, 0.1)
                risk_score = max(0.1, min(0.9, base_risk + risk_variation))
                
                risk_level = "low" if risk_score < 0.4 else "medium" if risk_score < 0.7 else "high"
                
                sample_data.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "timestamp": date.isoformat(),
                    "risk_score": round(risk_score, 2),
                    "risk_level": risk_level,
                    "total_disruptions": random.randint(5, 15),
                    "high_severity_count": random.randint(1, 5),
                    "medium_severity_count": random.randint(2, 6),
                    "low_severity_count": random.randint(2, 8)
                })
            
            with open(self.history_file, 'w') as f:
                json.dump(sample_data, f, indent=2)
        
        if not os.path.exists(self.disruption_history_file):
            # Generate sample disruption history
            disruption_types = [
                "severe_weather", "port_congestion", "labor_strike",
                "geopolitical_conflict", "infrastructure_failure", "piracy"
            ]
            
            sample_disruptions = []
            base_date = datetime.now() - timedelta(days=7)
            
            for day in range(7):
                date = base_date + timedelta(days=day)
                daily_disruptions = []
                
                for _ in range(random.randint(3, 8)):
                    disruption_type = random.choice(disruption_types)
                    severity = random.choice(["low", "medium", "high"])
                    
                    daily_disruptions.append({
                        "id": f"HIST-{day}-{random.randint(1000, 9999)}",
                        "type": disruption_type,
                        "severity": severity,
                        "timestamp": (date + timedelta(hours=random.randint(0, 23))).isoformat(),
                        "location": random.choice([
                            "Suez Canal", "Panama Canal", "Port of Shanghai",
                            "Port of Singapore", "Strait of Hormuz"
                        ])
                    })
                
                sample_disruptions.extend(daily_disruptions)
            
            with open(self.disruption_history_file, 'w') as f:
                json.dump(sample_disruptions, f, indent=2)
    
    def get_risk_history(self, days: int = 30) -> List[Dict]:
        """Get historical risk data for the specified number of days"""
        try:
            with open(self.history_file, 'r') as f:
                all_data = json.load(f)
            
            # Return last N days
            return all_data[-days:] if len(all_data) > days else all_data
        except:
            return []
    
    def get_disruption_history(self, days: int = 7) -> List[Dict]:
        """Get disruption history for specified days"""
        try:
            with open(self.disruption_history_file, 'r') as f:
                all_disruptions = json.load(f)
            
            # Filter by date
            cutoff_date = datetime.now() - timedelta(days=days)
            filtered = [
                d for d in all_disruptions
                if datetime.fromisoformat(d["timestamp"]) >= cutoff_date
            ]
            
            return filtered
        except:
            return []
    
    def add_risk_entry(self, risk_score: float, risk_level: str, disruption_counts: Dict, 
                      route_id: str = None, origin: str = None, destination: str = None):
        """Add a new risk entry to history with optional route information"""
        try:
            # Load existing data
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    data = json.load(f)
            else:
                data = []
            
            # Add new entry
            entry = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "timestamp": datetime.now().isoformat(),
                "risk_score": round(risk_score, 2),
                "risk_level": risk_level,
                "total_disruptions": sum(disruption_counts.values()),
                "high_severity_count": disruption_counts.get("high", 0),
                "medium_severity_count": disruption_counts.get("medium", 0),
                "low_severity_count": disruption_counts.get("low", 0)
            }
            
            # Add route information if provided
            if route_id:
                entry["route_id"] = route_id
            if origin:
                entry["origin"] = origin
            if destination:
                entry["destination"] = destination
            
            data.append(entry)
            
            # Keep only last 90 days
            data = data[-90:]
            
            with open(self.history_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error adding risk entry: {e}")
    
    def get_statistics(self) -> Dict:
        """Get statistical summary of historical data"""
        history = self.get_risk_history()
        
        if not history:
            return {}
        
        risk_scores = [h["risk_score"] for h in history]
        
        return {
            "average_risk": round(sum(risk_scores) / len(risk_scores), 2),
            "max_risk": max(risk_scores),
            "min_risk": min(risk_scores),
            "total_days": len(history),
            "high_risk_days": sum(1 for h in history if h["risk_level"] == "high"),
            "medium_risk_days": sum(1 for h in history if h["risk_level"] == "medium"),
            "low_risk_days": sum(1 for h in history if h["risk_level"] == "low"),
            "trend": "increasing" if len(history) > 1 and risk_scores[-1] > risk_scores[0] else "decreasing"
        }
    
    def get_route_history(self, origin: str = None, destination: str = None, days: int = 30) -> List[Dict]:
        """Get historical risk data filtered by route"""
        try:
            with open(self.history_file, 'r') as f:
                all_data = json.load(f)
            
            # Filter by date
            cutoff_date = datetime.now() - timedelta(days=days)
            recent_data = [
                d for d in all_data
                if datetime.fromisoformat(d["timestamp"]) >= cutoff_date
            ]
            
            # Filter by route if specified
            if origin or destination:
                filtered_data = []
                for entry in recent_data:
                    if origin and destination:
                        if entry.get("origin") == origin and entry.get("destination") == destination:
                            filtered_data.append(entry)
                    elif origin:
                        if entry.get("origin") == origin:
                            filtered_data.append(entry)
                    elif destination:
                        if entry.get("destination") == destination:
                            filtered_data.append(entry)
                return filtered_data
            
            return recent_data
        except:
            return []
    
    def compare_routes(self, routes: List[Dict], days: int = 30) -> Dict:
        """Compare risk profiles of multiple routes"""
        comparison = {}
        
        for route in routes:
            origin = route.get("origin")
            destination = route.get("destination")
            route_key = f"{origin} → {destination}"
            
            history = self.get_route_history(origin, destination, days)
            
            if history:
                risk_scores = [h["risk_score"] for h in history]
                comparison[route_key] = {
                    "average_risk": round(sum(risk_scores) / len(risk_scores), 2),
                    "max_risk": max(risk_scores),
                    "min_risk": min(risk_scores),
                    "data_points": len(history),
                    "current_risk": risk_scores[-1] if risk_scores else 0,
                    "history": history
                }
        
        return comparison
