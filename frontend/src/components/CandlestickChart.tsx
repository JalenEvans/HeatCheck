import Plot from 'react-plotly.js';
import { createCandlestick } from '../utils/candleLogic';
import type { Gamelog } from '../types/types';

interface CandlestickChartProps {
    gamelogs: Gamelog[];
}

const CandlestickChart = ({ gamelogs }: CandlestickChartProps) => {
    const {x, open, high, low, close} = createCandlestick(gamelogs);

    return (
        <Plot
            data={[
            {type: 'candlestick',
                x: x,
                open: open, 
                high: high, 
                low: low, 
                close: close,
            },
            ]}
            layout={ {autosize: true} }
        />
    );
}

export { CandlestickChart };