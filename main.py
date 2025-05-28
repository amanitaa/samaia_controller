import logging

from controller.xbox_input import init_controller, read_input
from network.udp_client import send_command
from core.command_mapper import map_input_to_command
import time

logger = logging.getLogger(__name__)


def main():
    logger.info("Samaia Controller starting up...")

    try:
        joy = init_controller()
    except RuntimeError as e:
        logger.critical(f"Startup failed: {e}")
        return

    logger.info("Controller initialized. Entering control loop.")

    while True or KeyboardInterrupt:
        try:
            data = read_input(joy)
            command = map_input_to_command(data)
            send_command(command)
            time.sleep(0.1)
        except Exception as e:
            logger.exception(f"Error in main loop: {e}")


if __name__ == "__main__":
    main()
