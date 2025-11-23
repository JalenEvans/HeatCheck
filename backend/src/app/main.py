from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .services import fetch_player_gamelogs


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/player/{player_id}/{season}/gamelogs")
def get_player_gamelogs(player_id: int , season: str):
    gamelogs_df = fetch_player_gamelogs.fetch_player_gamelogs(player_id, season)
    return gamelogs_df.to_dict(orient='records')
