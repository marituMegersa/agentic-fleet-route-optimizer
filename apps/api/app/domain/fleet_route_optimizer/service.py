from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.fleet_route_optimizer.models import AgenticFleetRouteOptimizerSession, AgenticFleetRouteOptimizerItem
from app.domain.fleet_route_optimizer.schemas import AgenticFleetRouteOptimizerSessionCreate, AgenticFleetRouteOptimizerItemCreate

class AgenticFleetRouteOptimizerService:
    @staticmethod
    def create_session(db: Session, data: AgenticFleetRouteOptimizerSessionCreate) -> AgenticFleetRouteOptimizerSession:
        db_obj = AgenticFleetRouteOptimizerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticFleetRouteOptimizerSession:
        return db.query(AgenticFleetRouteOptimizerSession).filter(AgenticFleetRouteOptimizerSession.id == session_id).first()
