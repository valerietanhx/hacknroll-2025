interface AboutProps {
  onClick: (mode: string) => void;
}

export default function About({ onClick }: AboutProps) {
  const setCurrentScreen = onClick;
  return (
    <div className="home-container">
      <h1>About</h1>
      <p>
        This text-based adventure game is a fun way to explore a fictional world
        using your imagination and commands. Built with React!
      </p>
      <button onClick={() => setCurrentScreen("home")}>Back to Home</button>
    </div>
  );
}
