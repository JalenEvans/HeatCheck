import type { Player } from '../../global_types';

import "./PlayerDropdown.css";

interface PlayerDropdownItemProps {
    player: Player;
    index: number;
    isHighlighted?: boolean;
}

const PlayerDropdownItem = ({ player, index, isHighlighted }: PlayerDropdownItemProps) => {
    return (
        <div id={`player-item-${index}`} className={`cursor-pointer p-2 border-b border-black ${isHighlighted ? "flex flex-row items-center bg-gray-300" : "bg-white"}`}>
            {isHighlighted ? <img src={`src/assets/headshots/${player.id}.png`} width={100} height={100} alt="No image found."/> : null}
            {player.first_name} {player.last_name}
        </div>
    );
}
export { PlayerDropdownItem };