import socket
import time

import orjson
import struct

from config import SAMAYA_PORT, SAMAYA_IP
from utils.logger import logger

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SAMAYA_IP, SAMAYA_PORT))


def send_command(msg):
    try:
        json_bytes = orjson.dumps(msg)
        sock.send(struct.pack('>I', len(json_bytes)) + json_bytes)
        logger.info(f"Sent: {msg}")
        time.sleep(0.01)
    except Exception as e:
        logger.error(f"Failed to send command: {e}")


def receive_event():
    try:
        raw_msg = sock.recv(4)
        msg_len = struct.unpack('>I', raw_msg)[0]
        data = sock.recv(msg_len)
        msg = orjson.loads(data)
        logger.info(f"Received: {msg}")
        return msg
    except Exception as e:
        logger.error(f"Failed to receive msg: {e}")
