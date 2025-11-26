from pydantic import BaseModel
from datetime import date

class PlayerCreate(BaseModel):
    player_id: int
    team_id: int
    first_name: str
    last_name: str
    birthdate: date
    school: str
    country: str
    height_inches: int
    weight: int
    jersey: int
    position: str
    draft_year: int

class PlayerResponse(BaseModel):
    player_id: int
    team_id: int
    first_name: str
    last_name: str
    birthdate: date
    school: str
    country: str
    height_inches: int
    weight: int
    jersey: int
    position: str
    draft_year: int
    
    class Config:
        from_attributes = True
    