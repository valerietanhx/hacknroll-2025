import json
import os

import src.llm as llm
from flask import Flask, jsonify, request
from flask_cors import CORS
from src.mongo import MongoDBHelper

app = Flask(__name__)
CORS(app)

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


@app.route("/adventure", methods=["GET"])
def create():

    output, conv_hist = llm.begin_conv()
    checked = llm.check_story(conv_hist, {})
    stats = json.loads(checked)

    mongo = MongoDBHelper(connection_string, mongodb_db, collection)

    adventure = {
        "stats": stats,
        "story": conv_hist,
    }

    document_id = mongo.create(adventure)
    mongo.close_connection()

    return jsonify({"stats": stats, "output": output, "document_id": document_id}), 200


@app.route("/adventure/<document_id>", methods=["GET"])
def continue_adventure(document_id):
    userInput = request.args.get("input")  # using query parameter

    mongo = MongoDBHelper(connection_string, mongodb_db, collection)
    document = mongo.retrieve(document_id)

    output, conv_hist = llm.generate_story(
        document["story"], userInput, document["stats"]
    )
    stats = json.loads(llm.check_story(conv_hist, document["stats"]))

    adventure = {
        "stats": stats,
        "story": conv_hist,
    }

    mongo.update(document_id, adventure)
    mongo.close_connection()

    return jsonify({"stats": stats, "output": output}), 200


# @app.route("/adventure/<document_id>", methods=["PATCH"])
# def update(document_id):
#     mongo = MongoDBHelper(connection_string, mongodb_db, collection)
#     is_successful = mongo.update(document_id, {})
#     mongo.close_connection()
#     return is_successful


# @app.route("/adventure/<document_id>", methods=["DELETE"])
# def delete(document_id):
#     mongo = MongoDBHelper(connection_string, mongodb_db, collection)
#     is_successful = mongo.delete(document_id)
#     mongo.close_connection()
#     return is_successful


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_CONTAINER_PORT)
