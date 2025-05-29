import logging
import socket

from config import SAMAYA_PORT, SAMAYA_IP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

logger = logging.getLogger(__name__)


def send_command(msg):
    try:
        sock.sendto(msg.encode(), (SAMAYA_IP, SAMAYA_PORT))
        logger.info(f"Sent: {msg}")
    except Exception as e:
        logger.error(f"Failed to send command: {e}")


def receive_event():
    try:
        data, _ = sock.recvfrom(1024)
        msg = data.decode().strip().upper()
        logger.info(f"Received: {msg}")
        return msg
    except Exception as e:
        logger.error(f"Failed to receive msg: {e}")
