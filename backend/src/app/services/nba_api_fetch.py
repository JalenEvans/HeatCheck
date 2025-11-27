from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import CommonPlayerInfo, PlayerGameLog
import pandas as pd
from time import sleep

def fetch_active_players() -> pd.DataFrame:
    active_players = players.get_active_players()
    return pd.DataFrame(active_players)

def fetch_player_info (player_id: int) -> pd.DataFrame:
    return CommonPlayerInfo(player_id=player_id).get_data_frames()[0]

def fetch_all_teams() -> pd.DataFrame:
    all_teams = teams.get_teams()
    return pd.DataFrame(all_teams)

def fetch_player_gamelogs(player_id: int, season: str = "2025-26") -> pd.DataFrame:
    return PlayerGameLog(player_id=player_id, season=season, season_type_all_star='Regular Season').get_data_frames()[0]
