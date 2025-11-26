from sqlalchemy import Column, Integer, String, Date, SmallInteger, ForeignKey
from ..db.db import Base

class Gamelog(Base):
    __tablename__ = "Gamelog"

    game_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("Player.player_id"), primary_key=True)
    season_id = Column(Integer, primary_key=True)
    game_date = Column(Date)
    matchup = Column(String)
    win_lose = Column(String)
    minutes = Column(SmallInteger)
    fgm = Column(SmallInteger)
    fga = Column(SmallInteger)
    fg3m = Column(SmallInteger)
    fg3a = Column(SmallInteger)
    ftm = Column(SmallInteger)
    fta = Column(SmallInteger)
    oreb = Column(SmallInteger)
    dreb = Column(SmallInteger)
    ast = Column(SmallInteger)
    stl = Column(SmallInteger)
    blk = Column(SmallInteger)
    tov = Column(SmallInteger)
    pf = Column(SmallInteger)
    pts = Column(SmallInteger)
    plus_minus = Column(SmallInteger)