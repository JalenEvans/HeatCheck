import { useEffect, useState } from 'react';
import { fetchNBAStats } from '../api/nbaStats'
import { CandlestickChart } from '../components/CandlestickChart';
import type { Gamelog } from '../types';

export function App() {
  const [gamelogs, setGamelogs] = useState<Gamelog[]>([]);

  useEffect(() => {
    console.log("Fetching NBA stats...");
    fetchNBAStats(1631157, '2025-26').then((gamelogs) => {
      if (gamelogs) {
        setGamelogs(gamelogs);
        console.log("Gamelogs fetched:", gamelogs);
      }
    })
  }, []);


  return (
    <div style={{ color: 'black', fontSize: 24, padding: 20 }}>
      <h1>Heat Check</h1>
      <CandlestickChart gamelogs={gamelogs} />
    </div>
  );
}

