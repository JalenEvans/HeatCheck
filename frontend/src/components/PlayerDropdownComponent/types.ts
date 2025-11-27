import type { Player } from "../../global_types";

export interface PlayerDropdownProps {
  onSelect: (player: Player) => void;
}