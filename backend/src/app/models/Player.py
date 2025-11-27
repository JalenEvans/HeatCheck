from sqlalchemy import Column, Integer, String, Date, SmallInteger, ForeignKey
from ..db.db import Base

class Player(Base):
    __tablename__ = "Player"

    player_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("Team.team_id"))
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(Date)
    school = Column(String)
    country = Column(String)
    height_inches = Column(SmallInteger)
    weight = Column(SmallInteger)
    jersey = Column(SmallInteger)
    position = Column(String)
    draft_year = Column(SmallInteger)