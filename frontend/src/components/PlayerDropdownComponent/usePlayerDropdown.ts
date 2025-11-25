import { useEffect, useRef, useState } from "react";
import { fetchActivePlayers } from "../../api/fetchActivePlayers";

import type { Player } from "../../global_types";
import type { PlayerDropdownProps } from "./types";

export const usePlayerDropdown = ({ onSelect }: PlayerDropdownProps) => {
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
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setOpen(false);
      }
    };

    // Close dropdown on Escape key
    const handleEsc = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        setOpen(false);
        inputRef.current?.blur();
      }
    };

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
        setHighlightedIndex(
          (prevIndex) => (prevIndex - 1 + filtered.length) % filtered.length
        );
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
    };

    document.addEventListener("keydown", handleArrowKeys);
    return () => {
      document.removeEventListener("keydown", handleArrowKeys);
    };
  }, [open, highlightedIndex, filtered]);

  // Scroll highlighted item into view
  useEffect(() => {
    if (highlightedIndex < 0) return;
    const item = document.getElementById(`player-item-${highlightedIndex}`);
    item?.scrollIntoView({ block: "nearest" });
  }, [highlightedIndex]);

  return {
    dropdownRef,
    inputRef,
    search,
    setSearch,
    open,
    setOpen,
    filtered,
    highlightedIndex,
    setHighlightedIndex,
  };
};
