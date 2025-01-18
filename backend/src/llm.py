def begin_conv(theme="fantasy"):
    """initial prompt to the llm to start the story"""
    return [
        {
            "role": "system",
            "content": f"You are a story-teller for a text adventure game, which the user is going to play. \
                Your role is to tell a story. After every turn, present the user with 4 choices, as with any text adventure game. \
                    The user must choose one of the four options. Continue the story following the users choice. \
            No text formatting is required. Now begin the story with a battle. The story has a {theme} theme.",
        }
    ]


def check_story(conversation_history: list, curr_stats: dict):
    """check current stats and stuff"""
    to_check = conversation_history.copy()
    to_check[0] = {
        "role": "system",
        "content": "You are a game-balancer for a text adventure game, which the user is going to play.",
    }
    to_check.append(
        {
            "role": "user",
            "content": f"""Here are the stats of characters so far prior to the latest update of the story:
{curr_stats}

Based on the latest update to the story, deduce whether a new character has been introduced and assign them a power level and health based on how strong you think they are. 
Also deduce if the main character has lost or gained health/power. If a character is dead, the health should be set to 0.
Provide a summary of all updated stats in a code chunk. Here is an example:
```
{"main": {"power": 500, "health": 100},  "goblin": {"power": 20, "health": 10}}
```

""",
        }
    )
    """Now we pass it through the llm and just extract the dict."""
