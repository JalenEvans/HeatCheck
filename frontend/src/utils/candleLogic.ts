import { rolling } from "./rolling";

interface Gamelog {
    GAME_DATE: string;
    FPTS: number;
}

export const createCandlestick = (gamelogs: Gamelog[]) => {
    gamelogs = [...gamelogs].reverse();

    const x = gamelogs.map((gamelog: Gamelog) => gamelog.GAME_DATE);

    const windows = rolling(gamelogs.map((gamelog: Gamelog) => gamelog.FPTS), 3);

    const open = windows.map(window => window.length > 0 ? window[0] : NaN);
    const close = windows.map(window => window.length > 0 ? window[window.length - 1] : NaN);
    const high = windows.map(window => window.length > 0 ? Math.max(...window) : NaN);
    const low = windows.map(window => window.length > 0 ? Math.min(...window) : NaN);

    return { x, open, high, low, close };
}