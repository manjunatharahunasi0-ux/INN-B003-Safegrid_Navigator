from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import uuid
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.data_aggregator import DataAggregator
from core.risk_engine import RiskEngine
from core.recommendation_generator import RecommendationGenerator
from core.history_manager import HistoryManager
from models.shipment_schema import RouteRequest, RouteResponse, Disruption

app = Flask(__name__)
CORS(app)

# Initialize core components
data_aggregator = DataAggregator()
risk_engine = RiskEngine()
recommendation_generator = RecommendationGenerator()
history_manager = HistoryManager()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/api/calculate_risk', methods=['POST'])
def calculate_risk():
    """Calculate risk for a given route"""
    try:
        data = request.json
        origin = data.get('origin', '')
        destination = data.get('destination', '')
        route_id = data.get('route_id', str(uuid.uuid4()))
        
        if not origin or not destination:
            return jsonify({"error": "Origin and destination are required"}), 400
        
        # Fetch global disruptions
        all_disruptions = data_aggregator.fetch_global_disruptions()
        
        # Get route-specific disruptions
        route_disruptions = data_aggregator.get_route_specific_disruptions(
            origin, destination, all_disruptions
        )
        
        # Calculate risk score
        risk_score, risk_level = risk_engine.calculate_risk_score(
            route_disruptions, origin, destination
        )
        
        # Generate recommendations
        recommendations = recommendation_generator.generate_recommendations(
            risk_level, route_disruptions, origin, destination
        )
        
        # Log this risk calculation to history
        disruption_severity_counts = {"high": 0, "medium": 0, "low": 0}
        for d in route_disruptions:
            severity = d.get("severity", "low")
            disruption_severity_counts[severity] = disruption_severity_counts.get(severity, 0) + 1
        
        history_manager.add_risk_entry(
            risk_score=risk_score,
            risk_level=risk_level,
            disruption_counts=disruption_severity_counts,
            route_id=route_id,
            origin=origin,
            destination=destination
        )
        
        # Get route coordinates
        origin_coords = risk_engine.get_location_coordinates(origin)
        destination_coords = risk_engine.get_location_coordinates(destination)
        
        # Format disruptions
        formatted_disruptions = []
        for disr in route_disruptions:
            formatted_disruptions.append({
                "type": disr["type"],
                "severity": disr["severity"],
                "description": disr["description"],
                "confidence": 0.85,
                "location": disr.get("location")
            })
        
        response = {
            "route_id": route_id,
            "origin": origin,
            "destination": destination,
            "overall_risk_score": round(risk_score, 2),
            "risk_level": risk_level,
            "disruptions": formatted_disruptions,
            "recommended_action": recommendations,
            "timestamp": datetime.now().isoformat(),
            "route_coordinates": {
                "origin": {"lat": origin_coords[0], "lon": origin_coords[1]},
                "destination": {"lat": destination_coords[0], "lon": destination_coords[1]}
            }
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/global_map_data', methods=['GET'])
def get_global_map_data():
    """Get all current global disruptions for map visualization"""
    try:
        disruptions = data_aggregator.fetch_global_disruptions()
        return jsonify({
            "disruptions": disruptions,
            "timestamp": datetime.now().isoformat(),
            "total_count": len(disruptions)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.route('/api/risk_history', methods=['GET'])
def get_risk_history():
    """Get historical risk data"""
    try:
        days = request.args.get('days', default=30, type=int)
        history = history_manager.get_risk_history(days)
        return jsonify({
            "history": history,
            "total_records": len(history)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/disruption_history', methods=['GET'])
def get_disruption_history():
    """Get historical disruption data"""
    try:
        days = request.args.get('days', default=7, type=int)
        disruptions = history_manager.get_disruption_history(days)
        return jsonify({
            "disruptions": disruptions,
            "total_count": len(disruptions)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """Get statistical summary"""
    try:
        stats = history_manager.get_statistics()
        return jsonify(stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/api/route_history', methods=['GET'])
def get_route_history():
    """Get historical risk data for a specific route"""
    try:
        origin = request.args.get('origin', type=str)
        destination = request.args.get('destination', type=str)
        days = request.args.get('days', default=30, type=int)
        
        history = history_manager.get_route_history(origin, destination, days)
        return jsonify({
            "origin": origin,
            "destination": destination,
            "history": history,
            "total_records": len(history)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/compare_routes', methods=['POST'])
def compare_routes():
    """Compare historical risk data for multiple routes"""
    try:
        data = request.json
        routes = data.get('routes', [])
        days = data.get('days', 30)
        
        comparison = history_manager.compare_routes(routes, days)
        return jsonify({
            "comparison": comparison,
            "days_analyzed": days
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
