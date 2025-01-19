export interface Stats {
  [character: string]: Stat;
}

export interface Stat {
  health: number;
  power: number;
}
