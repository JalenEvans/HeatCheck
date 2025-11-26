from nba_api.stats.endpoints import CommonPlayerInfo
import pandas as pd

def fetch_player_info (player_id: int) -> pd.DataFrame:
    return CommonPlayerInfo(player_id=player_id).get_data_frames()[0]