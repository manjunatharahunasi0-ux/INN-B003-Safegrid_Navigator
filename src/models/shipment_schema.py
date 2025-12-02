from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Disruption(BaseModel):
    type: str
    severity: str
    description: str
    confidence: float
    location: Optional[dict] = None

class RouteRequest(BaseModel):
    origin: str
    destination: str
    route_id: Optional[str] = None

class RouteResponse(BaseModel):
    route_id: str
    origin: str
    destination: str
    overall_risk_score: float
    risk_level: str
    disruptions: List[Disruption]
    recommended_action: str
    timestamp: str
    route_coordinates: Optional[List[dict]] = None

class DisruptionEvent(BaseModel):
    id: str
    type: str
    severity: str
    description: str
    location: dict
    timestamp: str
