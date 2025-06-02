import socket

from config import SAMAYA_PORT, SAMAYA_IP
from utils.logger import logger

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((SAMAYA_IP, SAMAYA_PORT))


def send_command(msg):
    try:
        sock.send(msg.encode())
        logger.info(f"Sent: {msg}")
    except Exception as e:
        logger.error(f"Failed to send command: {e}")


def receive_event():
    try:
        data, _ = sock.recvfrom(1024)
        msg = data.decode().strip()
        logger.info(f"Received: {msg}")
        return msg
    except Exception as e:
        logger.error(f"Failed to receive msg: {e}")
