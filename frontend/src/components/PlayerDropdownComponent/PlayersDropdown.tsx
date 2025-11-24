import { useEffect, useRef, useState } from "react";
import { fetchActivePlayers } from "../../api/fetchActivePlayers";

import type { Player } from "../../types/types";

import { PlayerDropdownItem } from "./PlayerDropdownItem";

import "./PlayerDropdown.css";

interface PlayerDropdownProps {
  onSelect: (player: Player) => void;
}

const PlayersDropdown = ({ onSelect }: PlayerDropdownProps) => {
  const [players, setPlayers] = useState<Player[]>([]);
  const [search, setSearch] = useState<string>("");
  const [open, setOpen] = useState<boolean>(false);

  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Close dropdown
  useEffect(() => {
    // Close dropdown when clicking outside
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setOpen(false);
      }
    }

    // Close dropdown on Escape key
    const handleEsc = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setOpen(false);
        inputRef.current?.blur();
      }
    }

    document.addEventListener("mousedown", handleClickOutside);
    document.addEventListener("keydown", handleEsc);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
      document.removeEventListener("keydown", handleEsc);
    };
  });

  // Fetch list of active players on component mount
  useEffect(() => {
    console.log("Fetching active players...");
    fetchActivePlayers().then((players) => {
      if (players) {
        setPlayers(players);
        console.log("Active players fetched:", players);
      }
    });
  }, []);

  // Filter players based on search input
  const filtered = players.filter((player) =>
    `${player.first_name} ${player.last_name}`
      .toLowerCase()
      .includes(search.toLowerCase())
  );

  return (
    <div className="w-full relative" ref={dropdownRef}>

      {/* Search Input */}
      <input
        ref={inputRef}
        type="text"
        value={search}
        onFocus={() => setOpen(true)}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search players..."
        className="w-full border-2 border-gray-300 rounded p-2"
      />

      {/* Dropdown List */}
      {open && (
        <div className="absolute top-10 w-full max-h-52 overflow-y-auto border border-gray-300 bg-white z-10">
          {filtered.map((player) => (
            <div
              key={player.id}
              onClick={() => {
                onSelect(player);
                setOpen(false);
                setSearch(`${player.first_name} ${player.last_name}`);
              }}
              onMouseEnter={(e) => (e.currentTarget.style.background = "#eee")}
              onMouseLeave={(e) => (e.currentTarget.style.background = "white")}
            >
              <PlayerDropdownItem player={player} />
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
