from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..services.db import player_services
from ..schemas.Player import PlayerResponse, PlayerCreate
from ..db.db import get_db

router = APIRouter(
    prefix = "/db/player",
    tags = ["Database"]
)

@router.get("/{player_id}")
def get_player_by_id(player_id: int, db: Session = Depends(get_db)):
    player = player_services.select_player_by_id(player_id)
    if player:
        return {
            "player_id": player.player_id,
            "team_id": player.team_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birthdate": player.birthdate,
            "school": player.school,
            "country": player.country,
            "height_inches": player.height_inches,
            "weight": player.weight,
            "jersey": player.jersey,
            "position": player.position
        }
    else:
        return {"error": "Player not found"}

@router.post("/", response_model=PlayerResponse)
def create_player(player_data: PlayerCreate, db: Session = Depends(get_db)):
    player_services.insert_player(player_data, db)
    return player_data
