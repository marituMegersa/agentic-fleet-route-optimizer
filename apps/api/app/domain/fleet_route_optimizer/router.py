from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.fleet_route_optimizer.schemas import AgenticFleetRouteOptimizerSessionCreate, AgenticFleetRouteOptimizerSessionResponse
from app.domain.fleet_route_optimizer.service import AgenticFleetRouteOptimizerService

router = APIRouter(prefix="/api/v1/fleet_route_optimizer", tags=["Agentic Fleet Route Optimizer Domain"])

@router.post("/sessions", response_model=AgenticFleetRouteOptimizerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticFleetRouteOptimizerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Fleet Route Optimizer.
    """
    return AgenticFleetRouteOptimizerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticFleetRouteOptimizerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticFleetRouteOptimizerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
