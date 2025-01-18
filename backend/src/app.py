import os

from flask import Flask
from src.mongo import MongoDBHelper

app = Flask(__name__)

BACKEND_CONTAINER_PORT = os.getenv("BACKEND_CONTAINER_PORT", "5000")
mongodb_username = os.getenv("MONGO_INITDB_ROOT_USERNAME", "root")
mongdb_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
port = os.getenv("DATABASE_CONTAINER_PORT", "27017")
connection_string = f"mongodb://{mongodb_username}:{mongdb_password}@mongodb:{port}"
mongodb_db = os.getenv("MONGO_INITDB_DATABASE", "db")
collection = "adventures"


@app.route("/")
def main():
    return "Hello, World!"


@app.route("/create")
def create():
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)

    # Dummy adventure for testing
    adventure = {
        "stats": {"main": {"health": 100, "power": 0}},
        "stories": [{"role": "user", "content": "story"}],
    }

    document_id = mongo.create(adventure)
    mongo.close_connection()
    return f"Inserted document with ID: {document_id}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_CONTAINER_PORT)
