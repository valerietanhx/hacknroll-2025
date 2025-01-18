interface InstructionsProps {
  onClick: (mode: string) => void;
}

export default function Instructions({ onClick }: InstructionsProps) {
  const setCurrentScreen = onClick;
  return (
    <div className="home-container">
      <h1>Instructions</h1>
      <p>Type commands to interact with the game world. Examples include:</p>
      <ul>
        <li>
          <strong>look</strong>: Inspect your surroundings.
        </li>
        <li>
          <strong>get lamp</strong>: Pick up an item.
        </li>
        <li>
          <strong>move north</strong>: Move in a direction.
        </li>
      </ul>
      <button onClick={() => setCurrentScreen("home")}>Back to Home</button>
    </div>
  );
}
