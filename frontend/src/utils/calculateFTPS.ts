import type { Gamelog } from "../global_types";

/**
 * Calculates Fantasy Points (FTPS) based on various basketball statistics.
 * 
 * @param gamelog - The gamelog object containing player statistics
 * @param fgm - Field Goals Made Multiplier
 * @param fga - Field Goals Attempted Multiplier
 * @param ftm - Free Throws Made Multiplier
 * @param fta - Free Throws Attempted Multiplier
 * @param fg3m - Three-Point Field Goals Made Multiplier
 * @param reb - Total Rebounds Multiplier
 * @param ast - Assists Multiplier
 * @param stl - Steals Multiplier
 * @param blk - Blocks Multiplier
 * @param tov - Turnovers Multiplier
 * @param pts - Points Scored Multiplier
 * @returns The calculated Fantasy Points (FTPS)
 */
export const calculateFTPS = (
    gamelog: Gamelog,
    fgm: number,
    fga: number,
    ftm: number,
    fta: number,
    fg3m: number,
    reb: number,
    ast: number,
    stl: number,
    blk: number,
    tov: number,
    pts: number
) => {
    const ftps = (gamelog.fgm * fgm) +
        (gamelog.fga * fga) +
        (gamelog.ftm * ftm) +
        (gamelog.fta * fta) +
        (gamelog.fg3m * fg3m) +
        ((gamelog.oreb + gamelog.dreb) * reb) +
        (gamelog.ast * ast) +
        (gamelog.stl * stl) +
        (gamelog.blk * blk) +
        (gamelog.tov * tov) +
        (gamelog.pts * pts)

    console.log(ftps)

    return ftps;
}