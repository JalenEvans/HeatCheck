export async function fetchPlayerGamelogs(playerId: number, seasonID: number) {
    try {
        const res = await fetch(`http://127.0.0.1:8000/db/gamelog/get_player_gamelogs/${playerId}/season/${seasonID}`);

        if (!res.ok) throw new Error('Failed to fetch Gamelogs');
        console.log('Fetch Gamelogs response:', res);

        const data = await res.json();
        return data;
    }
    catch (error: any) {
        console.error('Error fetching NBA stats:', error);
    }
}