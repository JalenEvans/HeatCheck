from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..services.db import team_services
from ..schemas.Team import TeamResponse, TeamCreate
from ..db.db import get_db

router = APIRouter(
    prefix = "/db/team",
    tags = ["Database"]
)

@router.get("/get_team/{team_id}")
def get_player_by_id(team_id: int, db: Session = Depends(get_db)):
    team = team_services.select_team_by_id(team_id, db)
    if team:
        return {
            "team_id": team.team_id,
            "team_name": team.team_name,
            "team_abbreviation": team.team_abbreviation,
            "team_city": team.team_city
        }
    else:
        return {"error": "Team not found"}

@router.post("/", response_model=TeamResponse)
def create_player(team_data: TeamCreate, db: Session = Depends(get_db)):
    team_services.insert_team(team_data, db)
    return team_data

@router.post("/bulk_insert")
def bulk_create_teams(db: Session = Depends(get_db)):
    team_services.bulk_insert_team(db)
    return {"message": "Teams inserted successfully"}