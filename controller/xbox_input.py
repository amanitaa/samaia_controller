import logging

import pygame


logger = logging.getLogger(__name__)


def init_controller():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        logger.error("No Xbox controller detected!")
        raise RuntimeError("No Xbox controller found.")

    joy = pygame.joystick.Joystick(0)
    joy.init()
    logger.info(f"Connected to controller: {joy.get_name()}")
    return joy


def read_input(joy):
    pygame.event.pump()
    return {
        "LY": joy.get_axis(1),  # Left Y-axis
        "RX": joy.get_axis(3),  # Right X-axis (for expansion)
        "BTN_A": joy.get_button(0),
    }
