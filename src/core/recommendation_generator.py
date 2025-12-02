from typing import Dict, List

class RecommendationGenerator:
    """Generate actionable recommendations based on risk assessment"""
    
    def generate_recommendations(self, risk_level: str, disruptions: List[Dict], 
                                origin: str, destination: str) -> str:
        """Generate route-specific recommendations"""
        
        recommendations = []
        
        # Risk level based recommendations
        if risk_level == "high":
            recommendations.append("⚠️ HIGH RISK ROUTE: Consider postponing shipment or using alternative corridor")
            recommendations.append("🔄 Immediate Action: Review alternative routes and carriers")
            recommendations.append("📦 Increase safety stock levels by 25-40%")
        elif risk_level == "medium":
            recommendations.append("⚡ MODERATE RISK: Monitor situation closely")
            recommendations.append("📊 Consider buffer time of 2-3 additional days")
            recommendations.append("📦 Increase inventory buffer by 15-20%")
        else:
            recommendations.append("✅ LOW RISK: Route appears stable")
            recommendations.append("📈 Maintain standard inventory levels")
            recommendations.append("🔍 Continue routine monitoring")
        
        # Disruption-specific recommendations
        disruption_types = [d.get("type", "") for d in disruptions]
        
        if "severe_weather" in disruption_types:
            recommendations.append("🌩️ Weather Alert: Secure weather-sensitive cargo, consider weather delays")
        
        if "port_congestion" in disruption_types:
            recommendations.append("🚢 Port Congestion: Book earlier slots, consider nearby alternative ports")
        
        if "labor_strike" in disruption_types:
            recommendations.append("👷 Labor Action: Engage alternative labor sources, expedite customs clearance")
        
        if "geopolitical_conflict" in disruption_types:
            recommendations.append("🌐 Geopolitical Risk: Explore neutral territory routes, increase insurance coverage")
        
        if "infrastructure_failure" in disruption_types:
            recommendations.append("🔧 Infrastructure Issues: Use redundant systems, verify backup facilities")
        
        if "piracy" in disruption_types:
            recommendations.append("🛡️ Security Threat: Enhance security protocols, consider naval escort routes")
        
        return " | ".join(recommendations)
    
    def get_alternative_routes(self, origin: str, destination: str) -> List[str]:
        """Suggest alternative routes"""
        alternatives = [
            f"Alternative 1: {origin} → Regional Hub → {destination} (+2-3 days)",
            f"Alternative 2: Air freight option (+cost, -5 days)",
            f"Alternative 3: Multi-modal transport via rail/road segments"
        ]
        return alternatives
