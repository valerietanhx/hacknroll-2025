import { useState } from "react";
import "./App.css";
import Home from "./components/Home";
import Instructions from "./components/Instructions";
import About from "./components/About";
import Game from "./components/Game";

function App() {
  const [currentScreen, setCurrentScreen] = useState("home");

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
