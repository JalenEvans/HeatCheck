from fastapi import HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ...models.Gamelog import Gamelog
from ...schemas.Gamelog import GamelogCreate

def select_gamelog_by_id(game_id: int, db: Session) -> Gamelog:
    gamelog = db.query(Gamelog).filter(Gamelog.game_id == game_id).first()
    return gamelog

def insert_gamelog(game_data: GamelogCreate, db: Session):
    # Check if gamelog already exists
    existing_gamelog = db.query(Gamelog).filter(Gamelog.game_id == game_data.game_id).first()
    if existing_gamelog:
        raise HTTPException(status_code=400, detail="Gamelog already exists")

    gamelog = Gamelog(**game_data.model_dump())

    db.add(gamelog)
    
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(e))