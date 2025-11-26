from fastapi import HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ..models.Team import Team
from ..schemas.Team import TeamCreate

def select_team_by_id(team_id: int, db: Session) -> Team:
    player = db.query(Team).filter(Team.team_id == team_id).first()
    return player

def insert_team(team_data: TeamCreate, db: Session):
    # Check if team already exists
    existing_team = db.query(Team).filter(Team.team_id == team_data.team_id).first()
    if existing_team:
        raise HTTPException(status_code=400, detail="Team already exists")
    
    player = Team(**team_data.model_dump())

    db.add(player)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(e))