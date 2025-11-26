from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..services.db import gamelog_services
from ..schemas.Gamelog import GamelogResponse, GamelogCreate
from ..db.db import get_db

router = APIRouter(
    prefix = "/db/gamelog",
    tags = ["Database"]
)

@router.get("/{game_id}")
def get_gamelog_by_id(game_id: int, db: Session = Depends(get_db)):
    gamelog = gamelog_services.select_gamelog_by_id(game_id, db)
    if gamelog:
        return {
            "game_id": gamelog.game_id,
            "player_id": gamelog.player_id,
            "season_id": gamelog.season_id,
            "game_date": gamelog.game_date,
            "matchup": gamelog.matchup,
            "win_lose": gamelog.win_lose,
            "minutes": gamelog.minutes,
            "fgm": gamelog.fgm,
            "fga": gamelog.fga,
            "fg3m": gamelog.fg3m,
            "fg3a": gamelog.fg3a,
            "ftm": gamelog.ftm,
            "fta": gamelog.fta,
            "oreb": gamelog.oreb,
            "dreb": gamelog.dreb,
            "ast": gamelog.ast,
            "stl": gamelog.stl,
            "blk": gamelog.blk,
            "tov": gamelog.tov,
            "pf": gamelog.pf,
            "pts": gamelog.pts,
            "plus_minus": gamelog.plus_minus
        }
    else:
        return {"error": "Gamelog not found"}

@router.post("/", response_model=GamelogResponse)
def create_gamelog(game_data: GamelogCreate, db: Session = Depends(get_db)):
    gamelog_services.insert_gamelog(game_data, db)
    return game_data
