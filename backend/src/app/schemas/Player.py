from pydantic import BaseModel, field_validator
from datetime import datetime, date

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
    draft_year: int | None

    @field_validator('player_id', "team_id", "weight", "jersey", "draft_year", mode='before')
    def parse_ints(cls, value):
        return int(value) if value and str(value).isdigit() else None
    
    @field_validator('birthdate', mode='before')
    def parse_birthdate(cls, value):
        if isinstance(value, str) and value:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
        return value

    @field_validator('height_inches', mode='before')
    def convert_to_inches(cls, value):
        # convert nba_api height format (e.g., "6-7") to total inches (e.g., 79)
        if isinstance(value, str) and '-' in value:
            feet, inches = map(int, value.split('-'))
            return feet * 12 + inches
        return value

class PlayerMinCreate(BaseModel):
    player_id: int
    first_name: str
    last_name: str

    @field_validator('player_id', mode='before')
    def parse_ints(cls, value):
        return int(value) if value and str(value).isdigit() else None

class PlayerInfoCreate(BaseModel):
    team_id: int
    birthdate: date
    school: str
    country: str
    height_inches: int
    weight: int
    jersey: int
    position: str
    draft_year: int | None

    @field_validator('team_id', "weight", "jersey", "draft_year", mode='before')
    def parse_ints(cls, value):
        return int(value) if value and str(value).isdigit() else None
    
    @field_validator('birthdate', mode='before')
    def parse_birthdate(cls, value):
        if isinstance(value, str) and value:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
        return value

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
    