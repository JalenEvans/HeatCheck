from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..services.db import player_services
from ..schemas.Player import PlayerResponse, PlayerCreate
from ..db.db import get_db

router = APIRouter(
    prefix = "/db/player",
    tags = ["Database"]
)

@router.get("/get_player/{player_id}", response_model=PlayerResponse)
def get_player_by_id(player_id: int, db: Session = Depends(get_db)):
    player = player_services.select_player_by_id(player_id, db)
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
    
@router.get("/active_players", response_model=list[PlayerResponse])
def get_active_players(db: Session = Depends(get_db)):
    players = player_services.select_active_players(db)
    return players

@router.post("/", response_model=PlayerResponse)
def create_player(player_data: PlayerCreate, db: Session = Depends(get_db)):
    player_services.insert_player(player_data, db)
    return player_data

@router.post("/bulk_insert")
def bulk_create_players(db: Session = Depends(get_db)):
    player_services.bulk_insert_players(db)
    return {"message": "Bulk insert of players completed"}

@router.post("/enrich/{player_id}")
def enrich_player_info(player_id: int, db: Session = Depends(get_db)):
    player_services.enrich_player(player_id, db)
    return {"message": f"Player {player_id} enriched with additional info"}
