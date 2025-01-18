db.createUser({
  user: "root",
  pwd: "password",
  roles: [
    {
      role: "readWrite",
      db: "db",
    },
  ],
});

db = new Mongo().getDB("db");
db.createCollection("adventures", { capped: false });
