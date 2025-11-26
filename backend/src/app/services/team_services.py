from sqlalchemy.orm import Session

from ..models.Team import Team
from ..schemas.Team import TeamCreate

def select_team_by_id(team_id: int, db: Session) -> Team:
    player = db.query(Team).filter(Team.team_id == team_id).first()
    return player

def insert_team(team_data: TeamCreate, db: Session):
    player = Team(**team_data.model_dump())

    db.add(player)
    db.commit()