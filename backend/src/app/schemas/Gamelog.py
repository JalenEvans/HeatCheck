from pydantic import BaseModel, field_validator
from datetime import datetime, date

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

    @field_validator('game_date', mode='before')
    def parse_birthdate(cls, value):
        if isinstance(value, str) and value:
            return datetime.strptime(value, "%b %d, %Y").date()
        return value

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