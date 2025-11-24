import type { Player } from '../../types/types';

interface PlayerDropdownItemProps {
    player: Player;
}

const PlayerDropdownItem = ({ player }: PlayerDropdownItemProps) => {
    return (
        <div className='cursor-pointer p-2 border-b border-black'>
            {player.first_name} {player.last_name}
        </div>
    );
}

export { PlayerDropdownItem };