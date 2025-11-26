from sqlalchemy.orm import Session

from ..db.db import get_db
from ..models.Player import Player
from ..schemas.Player import PlayerCreate

def select_player_by_id(player_id: int, db: Session) -> Player:
    player = db.query(Player).filter(Player.player_id == player_id).first()
    return player

def insert_player(player_data: PlayerCreate, db: Session):
    player = Player(**player_data.model_dump())

    db.add(player)
    db.commit()