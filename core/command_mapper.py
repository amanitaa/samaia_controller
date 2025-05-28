import logging

logger = logging.getLogger(__name__)


def map_input_to_command(data):
    y = data.get("LY", 0)

    if y < -0.5:
        command = "FORWARD"
    elif y > 0.5:
        command = "BACKWARD"
    else:
        command = "STOP"

    logger.debug(f"Mapped input Y={y:.2f} → Command: {command}")
    return command
