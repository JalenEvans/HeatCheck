from pydantic import BaseModel

class TeamCreate(BaseModel):
    team_id: int
    team_name: str
    team_abbreviation: str
    team_city: str

class TeamResponse(BaseModel):
    team_id: int
    team_name: str
    team_abbreviation: str
    team_city: str

    class Config:
        from_attributes = True