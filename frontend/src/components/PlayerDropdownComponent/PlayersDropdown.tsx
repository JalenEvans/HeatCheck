import { useEffect, useState } from "react";
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

  const filtered = players.filter((player) =>
    `${player.first_name} ${player.last_name}`
      .toLowerCase()
      .includes(search.toLowerCase())
  );

  return (
    <div style={{ width: 250, position: "relative" }}>

      {/* Search Input */}
      <input
        value={search}
        onFocus={() => setOpen(true)}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search players..."
        style={{ width: "100%", padding: "8px" }}
      />

      {/* Dropdown List */}
      {open && (
        <div
          style={{
            position: "absolute",
            top: "40px",
            width: "100%",
            maxHeight: "200px",
            overflowY: "auto",
            border: "1px solid #ddd",
            background: "white",
            zIndex: 10,
          }}
        >
          {filtered.map((player) => (
            <div
              key={player.id}
              onClick={() => {
                onSelect(player);
                setOpen(false);
                setSearch(`${player.first_name} ${player.last_name}`);
              }}
              style={{ padding: "8px", cursor: "pointer" }}
              onMouseEnter={(e) => (e.currentTarget.style.background = "#eee")}
              onMouseLeave={(e) => (e.currentTarget.style.background = "white")}
            >
              <PlayerDropdownItem player={player} />
            </div>
          ))}

          {/* Show message if no players meet the search */}
          {filtered.length === 0 && (
            <div className="bg" style={{ padding: "8px", color: "#777" }}>
              No Active Players.
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export { PlayersDropdown };
