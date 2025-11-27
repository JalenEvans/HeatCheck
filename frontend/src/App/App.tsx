import { useEffect, useState } from 'react';
import { fetchPlayerGamelogs } from '../api/fetchPlayerGamelogs'
import { CandlestickChart } from '../components/CandlestickChart';
import type { Gamelog, Player } from '../global_types';
import { PlayersDropdown } from '../components/PlayerDropdownComponent/PlayersDropdown';

import './App.css';

export function App() {
  const [gamelogs, setGamelogs] = useState<Gamelog[]>([]);
  const [selectedPlayer, setSelectedPlayer] = useState<Player>();

  const handleSelectPlayer = (player: Player) => {
    console.log(`Selected Player: ${player.first_name} ${player.last_name}`);
    setSelectedPlayer(player);
  }

  useEffect(() => {
    console.log(`Fetching Gamelogs for ${selectedPlayer?.first_name} ${selectedPlayer?.last_name}`);
    if (selectedPlayer) {
      fetchPlayerGamelogs(selectedPlayer.player_id, 22025).then((gamelogs) => {
        if (gamelogs) {
          setGamelogs(gamelogs);
          console.log("Gamelogs fetched:", gamelogs);
        }
      })
    }
    else {
      console.log(`Failed to fetch gamelogs`);
    }
  }, [selectedPlayer]);


  return (
    <div>
      <div className="grid grid-cols-2 p-4 border-b-2 border-gray-300">
        <h1>HeatCheck</h1>
        <PlayersDropdown onSelect={handleSelectPlayer}/>
      </div>
      <CandlestickChart gamelogs={gamelogs} />
    </div>
  );
}

