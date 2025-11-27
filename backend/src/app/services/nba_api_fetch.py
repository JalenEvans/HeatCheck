from nba_api.stats.static import players
from nba_api.stats.endpoints import CommonPlayerInfo, PlayerGameLog
import pandas as pd
from time import sleep

def fetch_active_players() -> pd.DataFrame:
    active_players = players.get_active_players()
    return pd.DataFrame(active_players)

def fetch_player_info (player_id: int) -> pd.DataFrame:
    return CommonPlayerInfo(player_id=player_id).get_data_frames()[0]

def append_fpts(gamelog_df: pd.DataFrame) -> pd.DataFrame:
    gamelog_df['FPTS'] = (
        (gamelog_df['FGM'] * 2) +
        (gamelog_df['FGA'] * -1) +
        gamelog_df['FTM'] +
        (gamelog_df['FTA'] * -1) +
        gamelog_df['FG3M'] +
        gamelog_df['REB'] +
        (gamelog_df['AST'] * 2) +
        (gamelog_df['STL'] * 4) +
        (gamelog_df['BLK'] * 4) +
        (gamelog_df['TOV'] * -2) +
        gamelog_df['PTS']
    )
    return gamelog_df

def fetch_player_gamelogs(player_id: int, season: str) -> pd.DataFrame:
    return append_fpts(PlayerGameLog(player_id=player_id, season=season, season_type_all_star='Regular Season').get_data_frames()[0])
