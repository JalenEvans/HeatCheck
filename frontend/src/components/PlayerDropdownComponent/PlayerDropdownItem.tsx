import type { Player } from '../../types/types';

interface PlayerDropdownItemProps {
    player: Player;
}

const PlayerDropdownItem = ({ player }: PlayerDropdownItemProps) => {
    return (
        <div>
            {player.first_name} {player.last_name}
        </div>
    );
}

export { PlayerDropdownItem };