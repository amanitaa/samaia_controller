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

    ly = joy.get_axis(1)  # vertical
    lx = joy.get_axis(0)  # horizontal

    btn_a = joy.get_button(0)

    logger.debug(f"LY: {ly:.2f}, LX: {lx:.2f}, BTN_A: {btn_a}")

    return {"LY": ly, "LX": lx, "BTN_A": btn_a}
