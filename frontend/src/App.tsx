import { useState } from "react";
import "./App.css";

function App() {
  const [currentScreen, setCurrentScreen] = useState("home");
  const [input, setInput] = useState("");
  const [log, setLog] = useState([
    "You are inside the small building. You discover that this is a one-room house. There are broken windows in all four walls. There is debris spread over the entire floor, and it is obvious that there hasn't been anyone here for a long time. Over in the corner, there is a large open trophy case. There is a large rug covering most of the floor. There is a large gas lamp.",
    "",
    "What would you like to do?",
  ]);
  const [stats, setStats] = useState({
    health: 100,
    mana: 50,
    abilities: ["Fireball", "Heal", "Teleport"],
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

  const handleModeSelect = (mode: string) => {
    setCurrentScreen(mode);
  };

  if (currentScreen === "home") {
    return (
      <div className="home-container">
        <h1>Welcome to the Adventure Game</h1>
        <div className="mode-buttons">
          <button onClick={() => handleModeSelect("start")}>Start Game</button>
          <div className="divider"></div>
          <button onClick={() => handleModeSelect("instructions")}>Instructions</button>
          <div className="divider"></div>
          <button onClick={() => handleModeSelect("about")}>About</button>
        </div>
      </div>
    );
  }

  if (currentScreen === "instructions") {
    return (
      <div className="home-container">
        <h1>Instructions</h1>
        <p>Type commands to interact with the game world. Examples include:</p>
        <ul>
          <li><strong>look</strong>: Inspect your surroundings.</li>
          <li><strong>get lamp</strong>: Pick up an item.</li>
          <li><strong>move north</strong>: Move in a direction.</li>
        </ul>
        <button onClick={() => setCurrentScreen("home")}>Back to Home</button>
      </div>
    );
  }

  if (currentScreen === "about") {
    return (
      <div className="home-container">
        <h1>About</h1>
        <p>
          This text-based adventure game is a fun way to explore a fictional
          world using your imagination and commands. Built with React!
        </p>
        <button onClick={() => setCurrentScreen("home")}>Back to Home</button>
      </div>
    );
  }

  return (
    <div className="body">
      <div className="game-container">
        {/* Stats Section */}
        <div className="stats-container">
          <h2>Stats</h2>
          <p><strong>Health:</strong> {stats.health}</p>
          <p><strong>Mana:</strong> {stats.mana}</p>
          <p><strong>Abilities:</strong></p>
          <ul>
            {stats.abilities.map((ability, index) => (
              <li key={index}>{ability}</li>
            ))}
          </ul>
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

export default App;
