from utils.logger import logger


def map_input_to_command(data):
    y = data.get("LY", 0)
    x = data.get("LX", 0)

    command = "STOP"

    if abs(y) > abs(x):
        if y < -0.5:
            command = "FORWARD"
        elif y > 0.5:
            command = "BACKWARD"
    else:
        if x < -0.5:
            command = "LEFT"
        elif x > 0.5:
            command = "RIGHT"

    logger.debug(f"Mapped input LY={y:.2f}, LX={x:.2f} → Command: {command}")
    return command
