import { usePlayerDropdown } from "./usePlayerDropdown";
import { PlayerDropdownItem } from "./PlayerDropdownItem";

import type { Player } from "../../global_types";
import type { PlayerDropdownProps } from "./types";

import "./PlayerDropdown.css";

const PlayersDropdown = ({ onSelect }: PlayerDropdownProps) => {
  const { dropdownRef, inputRef, search, setSearch, open, setOpen, filtered, highlightedIndex, setHighlightedIndex } = usePlayerDropdown({ onSelect });

  return (
    <div className="w-full relative" ref={dropdownRef}>

      {/* Search Input */}
      <input
        ref={inputRef}
        type="text"
        value={search}
        onFocus={() => {
          setOpen(true)
          setHighlightedIndex(0);
        }}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search players..."
        className="w-full border-2 border-gray-300 rounded p-2"
      />

      {/* Dropdown List */}
      {open && (
        <div className="absolute top-10 w-full max-h-52 overflow-y-auto border border-gray-300 bg-white z-10">
          {filtered.map((player: Player) => (
            <div
              key={player.player_id}
              onClick={() => {
                onSelect(player);
                setOpen(false);
                setSearch(`${player.first_name} ${player.last_name}`);
              }}
              onMouseEnter={() => {
                const index = filtered.indexOf(player);
                setHighlightedIndex(index);
              }}
              onMouseLeave={() => {
                const index = filtered.indexOf(player);
                setHighlightedIndex(index);
              }}
            >
              <PlayerDropdownItem player={player} index={filtered.indexOf(player)} isHighlighted={filtered.indexOf(player) == highlightedIndex} />
            </div>
          ))}

          {/* Show message if no players meet the search */}
          {filtered.length === 0 && (
            <div className="p-2 text-gray-500">
              No Active Players.
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export { PlayersDropdown };
