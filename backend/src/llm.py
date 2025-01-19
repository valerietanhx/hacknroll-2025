import os
import re

from dotenv import load_dotenv
from together import Together

load_dotenv()


def begin_conv(theme="fantasy") -> tuple[str, list]:
    """initial prompt to the llm to start the story"""
    conv_hist = [
        {
            "role": "system",
            "content": f"You are a story-teller for a text adventure game, which the user is going to play. \
                Your role is to tell a story. After every turn, present the user with 4 choices numbered 1 to 4 if the main character is alive. \
                    The user must choose one of the four options. Continue the story following the users choice. If the main character is dead, conclude the story. \
            No text formatting is required. Now begin the story with an exciting introduction. The story has a {theme} theme.",
        }
    ]

    client = Together()
    response = client.chat.completions.create(
        model=os.environ.get("LLM"),
        messages=conv_hist,
    )
    output = response.choices[0].message.content
    conv_hist.append({"role": "assistant", "content": output})
    return output, conv_hist


def generate_story(
    conversation_history: list, user_choice: str, stats: str
) -> tuple[str, list]:
    """stats to be a string but in dictionary format, output of check_story"""
    conversation_history.append({"role": "user", "content": user_choice})
    analysis_history = conversation_history.copy()
    analysis_history.append(
        {
            "role": "user",
            "content": f"The stats of all relevant characters (including the main character, denoted as main, is as follows {stats})",
        }
    )
    client = Together()
    response = client.chat.completions.create(
        model=os.environ.get("LLM"),
        messages=analysis_history,
    )
    output = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": output})
    return output, conversation_history, updated_stats


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
{str(curr_stats)}

Based on the latest update to the story, deduce whether a new character has been introduced and assign them a power level and health based on how strong you think they are. 
Also deduce if the main character (or "main" for short) has lost or gained health/power. If a character is dead, the health should be set to 0.
Provide a summary of all updated stats in a code chunk. Here is an example:
```
{{"main": {{"power": 500, "health": 100}},  "goblin": {{"power": 20, "health": 10}}}}
```

""",
        }
    )

    print(to_check)

    client = Together()
    response = client.chat.completions.create(
        model=os.environ.get("LLM"),
        messages=to_check,
    )
    # Now we pass it through the llm and just extract the dict as a string
    ext = extract(response.choices[0].message.content)
    print(ext)
    return ext


def extract(message: str, pattern=r"^```(?:\w+)?\s*\n(.*?)(?=^```)```"):
    """Given a string, extract portions of the string within a code chunk demarcated by ``` symbols"""
    return re.findall(pattern, message, re.DOTALL | re.MULTILINE)[0]
