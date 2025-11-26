from fastapi import HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ..models.Player import Player
from ..schemas.Player import PlayerCreate

def select_player_by_id(player_id: int, db: Session) -> Player:
    player = db.query(Player).filter(Player.player_id == player_id).first()
    return player

def insert_player(player_data: PlayerCreate, db: Session):
    # Check if player already exists
    existing_player = db.query(Player).filter(Player.player_id == player_data.player_id).first()
    if existing_player:
        raise HTTPException(status_code=400, detail="Player already exists")

    player = Player(**player_data.model_dump())

    db.add(player)
    
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(e))