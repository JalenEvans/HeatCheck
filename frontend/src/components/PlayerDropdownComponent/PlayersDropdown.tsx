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
  const [highlightedIndex, setHighlightedIndex] = useState<number>(-1);

  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

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
        event.preventDefault();
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

  // Arrow key navigation
  useEffect(() => {
    const handleArrowKeys = (event: KeyboardEvent) => {
      if (!open) return;

      if (event.key == "ArrowDown") {
        event.preventDefault();
        console.log("DOWN");
        setHighlightedIndex((prevIndex) => (prevIndex + 1) % filtered.length);
      } 

      if (event.key == "ArrowUp") {
        event.preventDefault();
        setHighlightedIndex((prevIndex) => (prevIndex - 1 + filtered.length) % filtered.length);
      }

      if (event.key == "Enter") {
        event.preventDefault();
        if (highlightedIndex >= 0 && highlightedIndex < filtered.length) {
          const selectedPlayer = filtered[highlightedIndex];
          onSelect(selectedPlayer);
          setOpen(false);
          setSearch(`${selectedPlayer.first_name} ${selectedPlayer.last_name}`);
        }
      }
    }

    document.addEventListener("keydown", handleArrowKeys);
    return () => {
      document.removeEventListener("keydown", handleArrowKeys);
    }
  }, [open, highlightedIndex, filtered]);

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
          {filtered.map((player) => (
            <div
              key={player.id}
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
              <PlayerDropdownItem player={player} isHighlighted={filtered[highlightedIndex] == player} />
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
