from fastapi import HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ...services.nba_api_fetch import fetch_all_teams

from ...models.Team import Team
from ...schemas.Team import TeamCreate

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
    
def bulk_insert_team(db: Session):
    """
    Insert all teams into the database
    Args:
        db (Session): The database session.
    """
    teams = fetch_all_teams().to_dict(orient="records")

    existing_teams = {
        t.team_id for t in db.query(Team.team_id).all()
    }

    for team_info in teams:
        if team_info.get("id") in existing_teams:
            continue # Skip exising teams
        
        team = TeamCreate(
            team_id=team_info.get("id"),
            team_name=team_info.get("nickname"),
            team_abbreviation=team_info.get("abbreviation"),
            team_city=team_info.get("city")
        )

        team = Team(**team.model_dump())
        db.add(team)

    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error during bulk insert: " + str(e))
