from utils.logger import logger


def map_input_to_command(data):
    y = data.get("LY", 0)
    x = data.get("LX", 0)

    command = {}

    if abs(y) > abs(x):
        if y < -0.5:
            command["action"] = "FORWARD"
            command["intensity"] = y
        elif y > 0.5:
            command["action"] = "BACKWARD"
            command["intensity"] = y
    else:
        if x < -0.5:
            command["action"] = "LEFT"
            command["intensity"] = x
        elif x > 0.5:
            command["action"] = "RIGHT"
            command["intensity"] = x

    logger.debug(f"Mapped input LY={y:.2f}, LX={x:.2f} → Command: {command}")
    return command
