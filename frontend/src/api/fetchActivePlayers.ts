export async function fetchActivePlayers() {
    try {
        const res = await fetch(`http://127.0.0.1:8000/db/player/active_players`);

        if(!res.ok) throw new Error('Failed to fetch active players');
        console.log('Fetch active players response:', res);

        const data = await res.json();
        return data;
    }
    catch (error: any) {
        console.error('Error fetching NBA stats:', error);
    }
}