import { useEffect, useState } from 'react';
import { fetchPlayerGamelogs } from '../api/fetchPlayerGamelogs'
import { CandlestickChart } from '../components/CandlestickChart';
import type { Gamelog } from '../types/types';
import { PlayersDropdown } from '../components/PlayerDropdownComponent/PlayersDropdown';

import './App.css';

export function App() {
  const [gamelogs, setGamelogs] = useState<Gamelog[]>([]);

  useEffect(() => {
    console.log("Fetching NBA stats...");
    fetchPlayerGamelogs(1631157, '2025-26').then((gamelogs) => {
      if (gamelogs) {
        setGamelogs(gamelogs);
        console.log("Gamelogs fetched:", gamelogs);
      }
    })
  }, []);


  return (
    <div>
      <div className="grid grid-cols-2 p-4 border-b-2 border-gray-300">
        <h1>HeatCheck</h1>
        <PlayersDropdown onSelect={() => console.log("BAM")}/>
      </div>
      <CandlestickChart gamelogs={gamelogs} />
    </div>
  );
}

