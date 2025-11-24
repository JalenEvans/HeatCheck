import type { Player } from '../../types/types';

interface PlayerDropdownItemProps {
    player: Player;
    isHighlighted?: boolean;
}

const PlayerDropdownItem = ({ player, isHighlighted }: PlayerDropdownItemProps) => {
    return (
        <div className={`cursor-pointer p-2 border-b border-black ${isHighlighted ? "bg-gray-300" : "bg-white"}`}>
            {player.first_name} {player.last_name}
        </div>
    );
}

export { PlayerDropdownItem };