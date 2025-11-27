from fastapi import HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ...services.nba_api_fetch import fetch_active_players, fetch_player_info

from ...models.Player import Player
from ...schemas.Player import PlayerCreate, PlayerMinCreate, PlayerInfoCreate

def select_player_by_id(player_id: int, db: Session) -> Player:
    """
    Select a player by their ID.
    Args:
        player_id (int): The ID of the player to select.
        db (Session): The database session.
    Returns:
        Player: The player object if found, else None.
    """
    player = db.query(Player).filter(Player.player_id == player_id).first()
    return player

def select_active_players(db: Session) -> list[Player]:
    """
    Select all active players from the database.
    Args:
        db (Session): The database session.
    Returns:
        list[Player]: A list of active player objects.
    """
    players = db.query(Player).order_by(Player.last_name).all()
    return players

def insert_player(player_data: PlayerCreate, db: Session):
    """
    Insert a new player into the database.
    Args:
        player_data (PlayerCreate): The player data to insert.
        db (Session): The database session.
    """
    # Check if player already exists
    existing_player = db.query(Player).filter(Player.player_id == player_data.player_id).first()
    if existing_player:
        raise HTTPException(status_code=400, detail="Player already exists")

    player = Player(**player_data.model_dump())
    db.add(player)
    
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(e))


def bulk_insert_players(db: Session):
    """
    Insert all active players into the database using basic information from the NBA API.

    Args:
        db (Session): The database session.
    """
    players = fetch_active_players().to_dict(orient="records")

    existing_player_ids = {
        p.player_id for p in db.query(Player.player_id).all()
    }

    for player_info in players:
        if player_info.get("id") in existing_player_ids:
            continue  # Skip existing players

        player = PlayerMinCreate(
            player_id=player_info.get("id"),
            first_name=player_info.get("first_name"),
            last_name=player_info.get("last_name"),
        )

        player = Player(**player.model_dump())
        db.add(player)

    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error during bulk insert: " + str(e))
    
def enrich_player(player_id: int, db: Session):
    """
    Enrich an existing player's record with additional information from the NBA API.

    Args:
        player_id (int): The ID of the player to enrich.
        db (Session): The database session.
    """
    player = db.query(Player).filter(Player.player_id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    if player.team_id is not None:
        raise HTTPException(status_code=400, detail="Player already enriched")

    player_info_df = fetch_player_info(player_id)
    if player_info_df.empty:
        raise HTTPException(status_code=404, detail="Player info not found in NBA API")

    info = player_info_df.iloc[0]

    player_info = PlayerInfoCreate(
        team_id=info.get("TEAM_ID"),
        birthdate=info.get("BIRTHDATE"),
        school=info.get("SCHOOL"),
        country=info.get("COUNTRY"),
        height_inches=info.get("HEIGHT"),
        weight=info.get("WEIGHT"),
        jersey=info.get("JERSEY"),
        position=info.get("POSITION"),
        draft_year=info.get("DRAFT_YEAR"),
    )

    for key, value in player_info.model_dump().items():
        setattr(player, key, value)

    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error during enrichment: " + str(e))
