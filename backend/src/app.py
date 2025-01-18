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


@app.route("/adventure", methods=["POST"])
def create():

    # TODO: Add LLM generation of story and power

    mongo = MongoDBHelper(connection_string, mongodb_db, collection)

    # TODO: update based on LLM's generated story and power
    adventure = {
        "stats": {"main": {"health": 100, "power": 0}},
        "story": [],
    }

    document_id = mongo.create(adventure)
    mongo.close_connection()
    return document_id


@app.route("/adventure/<document_id>", methods=["GET"])
def retrieve(document_id):
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)
    document = mongo.retrieve(document_id)
    mongo.close_connection()
    return document


@app.route("/adventure/<document_id>", methods=["PATCH"])
def update(document_id):
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)
    is_successful = mongo.update(document_id, {})
    mongo.close_connection()
    return is_successful


@app.route("/adventure/<document_id>", methods=["DELETE"])
def delete(document_id):
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)
    is_successful = mongo.delete(document_id)
    mongo.close_connection()
    return is_successful


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_CONTAINER_PORT)
