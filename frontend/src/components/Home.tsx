interface HomeProps {
  onClick: (mode: string) => void;
}

export default function Home({ onClick }: HomeProps) {
  const setCurrentScreen = onClick;
  return (
    <div className="home-container">
      <h1>Welcome to the Adventure Game</h1>
      <div className="mode-buttons">
        <button onClick={() => setCurrentScreen("start")}>Start Game</button>
        <div className="divider"></div>
        <button onClick={() => setCurrentScreen("instructions")}>
          Instructions
        </button>
        <div className="divider"></div>
        <button onClick={() => setCurrentScreen("about")}>About</button>
      </div>
    </div>
  );
}
