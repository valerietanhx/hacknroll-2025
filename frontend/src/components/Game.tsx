import { useState } from "react";
import { Stats } from "../utils/types";

export default function Game() {
  const [input, setInput] = useState("");
  const [log, setLog] = useState([
    "You are inside the small building. You discover that this is a one-room house. There are broken windows in all four walls. There is debris spread over the entire floor, and it is obvious that there hasn't been anyone here for a long time. Over in the corner, there is a large open trophy case. There is a large rug covering most of the floor. There is a large gas lamp.",
    "",
    "What would you like to do?",
  ]);
  const [stats, setStats] = useState<Stats>({
    health: 100,
    power: 0,
  });
  
  const handleInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      setLog([...log, `> ${input}`]);
      setInput("");
    }
  };

  return (
    <div className="body">
      <div className="game-container">
        {/* Stats Section */}
        <div className="stats-container">
          <h2>Stats</h2>
          <p>
            <strong>Health:</strong> {stats.health}
          </p>
          <p>
            <strong>Power:</strong> {stats.power}
          </p>
        </div>
        {/* Game Section */}
        <div className="game-content">
          <div className="game-log">
            {log.map((line, index) => (
              <p key={index}>{line}</p>
            ))}
          </div>
          <form onSubmit={handleSubmit} className="game-input">
            <input
              type="text"
              value={input}
              onChange={handleInput}
              placeholder="Type your command..."
            />
            <button type="submit">Enter</button>
          </form>
        </div>
      </div>
    </div>
  );
}
