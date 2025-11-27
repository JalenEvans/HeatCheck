from fastapi import APIRouter

from ..services.nba_api_fetch import fetch_player_gamelogs, fetch_active_players, fetch_player_info, fetch_all_teams

router = APIRouter(
    prefix = "/api",
    tags = ["API"]
)

@router.get("/player/{player_id}/{season}/gamelogs")
def get_player_gamelogs(player_id: int , season: str):
    gamelogs_df = fetch_player_gamelogs(player_id, season)
    return gamelogs_df.to_dict(orient='records')

@router.get("/active_players")
def get_active_players():
    active_players_df = fetch_active_players()
    return active_players_df.to_dict(orient='records')

@router.get("/player/{player_id}/info")
def get_player_info(player_id: int):
    player_info_df = fetch_player_info(player_id)
    return player_info_df.to_dict(orient='records')

@router.get("/team/get_all_teams")
def get_all_teams():
    teams_df = fetch_all_teams()
    return teams_df.to_dict(orient="records")