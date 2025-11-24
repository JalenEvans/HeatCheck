import { useEffect, useState } from 'react';
import { fetchPlayerGamelogs } from './api/fetchPlayerGamelogs'
import { CandlestickChart } from './components/CandlestickChart';
import type { Gamelog } from './types/types';
import { PlayersDropdown } from './components/PlayerDropdownComponent/PlayersDropdown';

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
      <CandlestickChart gamelogs={gamelogs} />
      <PlayersDropdown onSelect={() => console.log("BAM")}/>
    </div>
  );
}

