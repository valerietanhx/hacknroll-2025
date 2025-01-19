import { useEffect, useState } from "react";
import { Stats } from "../utils/types";

export default function Game() {
  const [input, setInput] = useState("");
  const [log, setLog] = useState<String[]>([]);
  const [stats, setStats] = useState<Stats>({});
  const [documentId, setDocumentId] = useState(-1);

  const backendHost = import.meta.env.VITE_BACKEND_HOST;
  const backendPort = import.meta.env.VITE_BACKEND_CONTAINER_PORT;

  const handleInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      setLog([...log, `> ${input}`]);
      setInput("");

      const apiUrl = `${backendHost}:${backendPort}/adventure/${documentId}?input=${input}`;

      try {
        const response = await fetch(apiUrl, {
          method: "GET",
        });
        if (!response.ok) {
          throw new Error(`${response.status}`);
        }
        const data = await response.json();
        setStats(data.stats);
        setLog([...log, data.output]);
      } catch (err: any) {}
    }
  };

  useEffect(() => {
    const apiUrl = `${backendHost}:${backendPort}/adventure`;

    const fetchData = async () => {
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`${response.status}`);
        }
        const data = await response.json();
        setStats(data.stats);
        setLog([...log, data.output]);
        setDocumentId(data.document_id);
      } catch (err) {}
    };

    fetchData();
  }, []);

  return (
    <div className="body">
      <div className="game-container">
        {/* Stats Section */}
        <div className="stats-container">
          <h2>Stats</h2>
          {stats &&
            Object.entries(stats).map(([characterName, stat]) => (
              <div key={characterName}>
                <h3>{characterName}</h3>
                <p>
                  <strong>Health:</strong> {stat.health}
                </p>
                <p>
                  <strong>Power:</strong> {stat.power}
                </p>
              </div>
            ))}
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
