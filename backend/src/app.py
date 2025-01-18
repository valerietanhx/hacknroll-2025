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
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)

    # Dummy adventure for testing
    default_adventure = {
        "stats": {"main": {"health": 100, "power": 0}},
        "stories": [{"role": "user", "content": "story"}],
    }

    document_id = mongo.create(default_adventure)
    mongo.close_connection()
    return document_id


@app.route("/adventure/<str:document_id>", methods=["GET"])
def retrieve(document_id):
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)
    document = mongo.retrieve(document_id)
    mongo.close_connection()
    return document


@app.route("/adventure/<str:document_id>", methods=["PATCH"])
def update(document_id):
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)
    is_successful = mongo.update(document_id, {})
    mongo.close_connection()
    return is_successful


@app.route("/adventure/<str:document_id>", methods=["DELETE"])
def delete(document_id):
    mongo = MongoDBHelper(connection_string, mongodb_db, collection)
    is_successful = mongo.delete(document_id)
    mongo.close_connection()
    return is_successful



def begin_conv(theme="fantasy"):
    '''initial prompt to the llm to start the story'''
    return [
        {
            "role": "system", "content": f"You are a story-teller for a text adventure game, which the user is going to play. \
                Your role is to tell a story. After every turn, present the user with 4 choices, as with any text adventure game. \
                    The user must choose one of the four options. Continue the story following the users choice. \
            No text formatting is required. Now begin the story with a battle. The story has a {theme} theme."
        }
    ]

def check_story(conversation_history: list, curr_stats: dict):
    '''check current stats and stuff'''
    to_check = conversation_history.copy()
    to_check[0] = {
            "role": "system", "content": f"You are a game-balancer for a text adventure game, which the user is going to play."
            }
    to_check.append(
        {
            "role": "user", "content": f"""Here are the stats of characters so far prior to the latest update of the story:
{curr_stats}

Based on the latest update to the story, deduce whether a new character has been introduced and assign them a power level and health based on how strong you think they are. 
Also deduce if the main character has lost or gained health/power. If a character is dead, the health should be set to 0.
Provide a summary of all updated stats in a code chunk. Here is an example:
```
{{"Main": {"Power": 500, "Health": 100},  "Goblin": {"Power": 20, "Health": 10}}}
```

"""
        }
    
    )
    '''Now we pass it through the llm and just extract the dict.'''
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_CONTAINER_PORT)
