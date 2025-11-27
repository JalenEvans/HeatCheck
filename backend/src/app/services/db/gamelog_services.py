from fastapi import HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ...services.nba_api_fetch import fetch_player_gamelogs

from ...models.Gamelog import Gamelog
from ...schemas.Gamelog import GamelogCreate

def select_gamelog_by_id(game_id: int, player_id: int, season_id: int, db: Session) -> Gamelog:
    gamelog = db.query(Gamelog).filter(
        Gamelog.game_id == game_id, 
        Gamelog.player_id == player_id, 
        Gamelog.season_id == season_id
        ).first()
    return gamelog

def select_gamelogs_by_player_id(player_id: int, season_id: int, db: Session):
    gamelogs = db.query(Gamelog).filter(Gamelog.player_id == player_id, Gamelog.season_id == season_id).order_by(Gamelog.game_date).all()

    if not gamelogs:
        insert_player_gamelogs(player_id, db)
    
    gamelogs = db.query(Gamelog).filter(Gamelog.player_id == player_id, Gamelog.season_id == season_id).order_by(Gamelog.game_date).all()
    
    return gamelogs

def insert_gamelog(game_data: GamelogCreate, db: Session):
    # Check if gamelog already exists
    existing_gamelog = db.query(Gamelog).filter(Gamelog.game_id == game_data.game_id).first()
    if existing_gamelog:
        raise HTTPException(status_code=400, detail="Gamelog already exists")

    gamelog = Gamelog(**game_data.model_dump())

    db.add(gamelog)
    
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(e))
    
def insert_player_gamelogs(player_id: int, db: Session):
    """
    Insert gamelogs for a specific player into the database.
    Args:
        player_id (int): The ID of the player whose gamelogs to insert.
        db (Session): The database session.
    """

    gamelogs = fetch_player_gamelogs(player_id).to_dict(orient="records")

    existing_games = {
        g.game_id for g in db.query(Gamelog.game_id).filter(Gamelog.player_id == player_id).all()
    }

    for gamelog_info in gamelogs:
        if gamelog_info.get("Game_ID") in existing_games:
            continue # Skip existing gamelogs

        game = GamelogCreate(
            game_id=gamelog_info.get("Game_ID"),
            player_id=player_id,
            season_id=gamelog_info.get("SEASON_ID"),
            game_date=gamelog_info.get("GAME_DATE"),
            matchup=gamelog_info.get("MATCHUP"),
            win_lose=gamelog_info.get("WL"),
            minutes=gamelog_info.get("MIN"),
            fgm=gamelog_info.get("FGM"),
            fga=gamelog_info.get("FGA"),
            fg3m=gamelog_info.get("FG3M"),
            fg3a=gamelog_info.get("FG3A"),
            ftm=gamelog_info.get("FTM"),
            fta=gamelog_info.get("FTA"),
            oreb=gamelog_info.get("OREB"),
            dreb=gamelog_info.get("DREB"),
            ast=gamelog_info.get("AST"),
            stl=gamelog_info.get("STL"),
            blk=gamelog_info.get("BLK"),
            tov=gamelog_info.get("TOV"),
            pf=gamelog_info.get("PF"),
            pts=gamelog_info.get("PTS"),
            plus_minus=gamelog_info.get("PLUS_MINUS")
        )

        game = Gamelog(**game.model_dump())
        db.add(game)

    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error during insert: " + str(e))


    