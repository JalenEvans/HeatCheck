export async function fetchPlayerGamelogs(playerId: number, season: string) {
    try {
        const res = await fetch(`http://127.0.0.1:8000/player/${playerId}/${season}/gamelogs`);

        if (!res.ok) throw new Error('Failed to fetch Gamelogs');
        console.log('Fetch Gamelogs response:', res);

        const data = await res.json();
        return data;
    }
    catch (error: any) {
        console.error('Error fetching NBA stats:', error);
    }
}