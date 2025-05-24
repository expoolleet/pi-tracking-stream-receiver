import socket
import json
import time
import threading
import numpy as np

from PySide6.QtCore import Qt, Signal, QObject

from src.tools import DebugEmitter

SOCKET_BUFFER_SIZE = 1024
MAX_RECONNECT_ATTEMPTS = 3

SERVER_IP = "10.20.1.1"
SERVER_PORT = 8001

class SocketData:
    command = ""
    data = {}

class SocketHandler(QObject):

    update_roi_signal = Signal(np.ndarray)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.socket = self.create()
        self.receive_thread = threading.Thread(target=self.receive, daemon=True)
        self.receive_thread.start()
        self.debug = DebugEmitter()


    @staticmethod
    def create():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def encode_data(self, command, data):
        packet = {
            "command": command,
            "data": data
        }
        raw_data = json.dumps(packet).encode('utf-8')
        return raw_data


    def decode_data(self, raw_data):
        try:
            data_str = raw_data.decode('utf-8')
            data = json.loads(data_str)
            if "data" not in data or data["data"] is None:
                return data.get("message", "")
            else:
                return data.get("message", ""), data["data"]
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            self.debug.send(f"Failed to decode server response: {e}")
            return None


    def receive(self):
        while True:
            try:
                data = self.socket.recv(SOCKET_BUFFER_SIZE)
                if not data:
                    pass
                while b"\n" in data:
                    try:
                        line, data = data.split(b"\n", 1)
                        message = json.loads(line.decode("utf-8"))
                        if message["roi"]:
                            received_roi = message["roi"]
                            self.update_roi_signal.emit(received_roi)
                        else:
                            self.debug.send(f"Received unknown message: {message}")
                    except json.JSONDecodeError:
                        self.debug.send(f"Received non-JSON data: {data.decode('utf-8').strip()}")
            except OSError as e:
                if e.winerror == 10057:
                    pass
            except socket.error as e:
                self.debug.send("Socket error:", e)


    def send(self, command: str, data: dict = {}):
        try:
            if self.socket is not None:
                encoded_data = self.encode_data(command, data)
                self.debug.send(f"socket sent: {command}; {encoded_data}")
                self.socket.send(encoded_data)
            else:
                self.debug.send("No socket has been initialized")
        except (socket.error, BrokenPipeError) as e:
            self.debug.send(f"Socket error: {e}")
            if self.reconnect():
                self.send(command, data)
            else:
                self.debug.send("Failed to reconnect to server")


    def reconnect(self):
        self.socket.close()
        self.socket = self.create()
        timeout = 1
        for attempt in range(1, MAX_RECONNECT_ATTEMPTS + 1):
            try:
                self.debug.send(f"Trying to reconnect... Attempt {attempt}/{MAX_RECONNECT_ATTEMPTS}")
                self.socket.connect((SERVER_IP, SERVER_PORT))
                self.debug.send("Reconnected successfully")
                return True
            except socket.error as e:
                self.debug.send(f"Reconnection failed: {e}")
                time.sleep((timeout + attempt) * 2)
        return False