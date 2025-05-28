import logging
import socket

from config import SAMAIA_IP, SAMAIA_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

logger = logging.getLogger(__name__)


def send_command(msg):
    try:
        sock.sendto(msg.encode(), (SAMAIA_IP, SAMAIA_PORT))
        logger.info(f"Sent: {msg}")
    except Exception as e:
        logger.error(f"Failed to send command: {e}")
