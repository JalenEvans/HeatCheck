import { rolling } from "./rolling";

import type { Gamelog } from "../global_types";
import { calculateFTPS } from "./calculateFTPS";

export const createCandlestick = (gamelogs: Gamelog[]) => {
    gamelogs = [...gamelogs].reverse();

    const x = gamelogs.map((gamelog: Gamelog) => gamelog.game_date);

    const windows = rolling(gamelogs.map((gamelog: Gamelog) => calculateFTPS(
        gamelog,
        2, //fgm
        -1, //fga
        1, //ftm
        -1, //fta
        1, //fg3m
        1, //reb
        2, //ast
        4, //stl
        4, //blk
        -2, //tov
        1 //pts
    )), 3);

    const open = windows.map(window => window.length > 0 ? window[0] : NaN);
    const close = windows.map(window => window.length > 0 ? window[window.length - 1] : NaN);
    const high = windows.map(window => window.length > 0 ? Math.max(...window) : NaN);
    const low = windows.map(window => window.length > 0 ? Math.min(...window) : NaN);

    return { x, open, high, low, close };
}