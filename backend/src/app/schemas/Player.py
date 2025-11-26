from pydantic import BaseModel, field_validator
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

    @field_validator('height_inches', mode='before')
    def convert_to_inches(cls, value):
        # convert nba_api height format (e.g., "6-7") to total inches (e.g., 79)
        if isinstance(value, str) and '-' in value:
            feet, inches = map(int, value.split('-'))
            return feet * 12 + inches
        return value

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
    