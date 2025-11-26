from pydantic import BaseModel
from datetime import date

class GamelogCreate(BaseModel):
    game_id: int
    player_id: int
    season_id: int
    game_date: date
    matchup: str
    win_lose: str
    minutes: int
    fgm: int
    fga: int
    fg3m: int
    fg3a: int
    ftm: int
    fta: int
    oreb: int
    dreb: int
    ast: int
    stl: int
    blk: int
    tov: int
    pf: int
    pts: int
    plus_minus: int

class GamelogResponse(BaseModel):
    game_id: int
    player_id: int
    season_id: int
    game_date: date
    matchup: str
    win_lose: str
    minutes: int
    fgm: int
    fga: int
    fg3m: int
    fg3a: int
    ftm: int
    fta: int
    oreb: int
    dreb: int
    ast: int
    stl: int
    blk: int
    tov: int
    pf: int
    pts: int
    plus_minus: int
    
    class Config:
        from_attributes = True