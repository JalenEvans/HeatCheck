export interface Gamelog {
    game_id: number;
    player_id: number;
    season_id: number;
    game_date: Date;
    matchup: string;
    win_lose: string;
    minutes: number;
    fgm: number;
    fga: number;
    fg3m: number;
    fg3a: number;
    ftm: number;
    fta: number;
    oreb: number;
    dreb: number;
    ast: number;
    stl: number;
    blk: number;
    tov: number;
    pf: number;
    pts: number;
    plus_minus: number;
}

export interface Player {
    player_id: number;
    first_name: string;
    last_name: string;
}