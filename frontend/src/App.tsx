import { useState } from "react";
import "./App.css";
import Home from "./components/Home";
import Instructions from "./components/Instructions";
import About from "./components/About";
import Game from "./components/Game";

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
    abilities: [
      { name: "Fireball", description: "Launches a fiery ball of flame.", damage: 50, manaCost: 20 },
      { name: "Heal", description: "Restores health to yourself or an ally.", damage: 0, manaCost: 10 },
      { name: "Teleport", description: "Instantly move to another location.", damage: 0, manaCost: 30 },
    ],
  });

  const [hoveredAbility, setHoveredAbility] = useState(null);

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
    return <Home onClick={setCurrentScreen} />;
  }
  if (currentScreen === "instructions") {
    return <Instructions onClick={setCurrentScreen} />;
  }
  if (currentScreen === "about") {
    return <About onClick={setCurrentScreen} />;
  }
  return <Game />;
}

export default App;
