import re


def parse_command(text):
    text = text.lower().strip()

    command = {
        "actuators": [],
        "duration": None,
        "direction": None
    }

    # Special commands
    if "all stop" in text:
        command["direction"] = "all stop"
        return command

    if "all move" in text:
        command["direction"] = "all move"
        return command

    # Direction
    if "up" in text:
        command["direction"] = "up"
    elif "down" in text:
        command["direction"] = "down"

    # Split into tokens
    tokens = text.split()

    actuator_tokens = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Time detection
        if token.isdigit():
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
                if next_token in ["sec", "second", "seconds"]:
                    command["duration"] = int(token)
                    break

            actuator_tokens.append(int(token))

        i += 1

    command["actuators"] = actuator_tokens

    return command