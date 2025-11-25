import type { Player } from '../../global_types';

interface PlayerDropdownItemProps {
    player: Player;
    index: number;
    isHighlighted?: boolean;
}

const PlayerDropdownItem = ({ player, index, isHighlighted }: PlayerDropdownItemProps) => {
    return (
        <div id={`player-item-${index}`} className={`cursor-pointer p-2 border-b border-black ${isHighlighted ? "bg-gray-300" : "bg-white"}`}>
            {player.first_name} {player.last_name}
        </div>
    );
}

export { PlayerDropdownItem };