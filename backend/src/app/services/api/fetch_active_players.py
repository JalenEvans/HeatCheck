from nba_api.stats.static import players
import pandas as pd

def fetch_active_players() -> pd.DataFrame:
    active_players = players.get_active_players()
    return pd.DataFrame(active_players)