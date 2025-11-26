from sqlalchemy import Column, Integer, String, Date, SmallInteger, ForeignKey
from ..db import Base

class Team(Base):
    __tablename__ = "Team"

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String)
    team_abbreviation = Column(String)
    team_city = Column(String)