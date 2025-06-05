import socket
import json
import time
import threading
import numpy as np

from PySide6.QtCore import Signal, QObject

from src.tools import DebugEmitter
from src.command import Command

SOCKET_BUFFER_SIZE = 1024
MAX_RECONNECT_ATTEMPTS = 3

class SocketData:
    command = ""
    data = {}


class SocketHandler(QObject):

    update_roi_signal = Signal(np.ndarray)
    stop_tracking_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.socket = self.create()
        self.receive_thread = threading.Thread(target=self.receive, daemon=True)
        self.receive_thread.start()
        self.debug = DebugEmitter()


    @staticmethod
    def create() -> socket.socket:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def encode_data(self, command, data) -> bytes:
        packet = {
            "command": command,
            "data": data
        }
        raw_data = json.dumps(packet).encode('utf-8')
        return raw_data


    def decode_data(self, data) -> list[dict]:
        try:
            if not data or data == b'':
                return None
            if b"\n" in data:
                messages = []
                while b"\n" in data:
                    line, data = data.split(b"\n", 1)
                    message = json.loads(line.decode("utf-8"))
                    messages.append(message)
                return  messages
            else:
                return [json.loads(data.decode("utf-8"))]
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            self.debug.send(f"Failed to decode server response: {e}")
            return None


    def handle_messages(self, messages) -> None:
        for message in messages:
            self.debug.send(f"server sent: {message}")
            if "roi" in message:
                received_roi = message["roi"]
                self.update_roi_signal.emit(received_roi)
            elif "command" in message:
                if message["command"] == Command.STOP_TRACKING:
                    self.stop_tracking_signal.emit()
            else:
                self.debug.send(f"Received unknown message: {message}")


    def receive(self) -> None:
        while True:
            try:
                data = self.socket.recv(SOCKET_BUFFER_SIZE)
                messages = self.decode_data(data)
                if data:
                    self.handle_messages(messages)
            except json.JSONDecodeError:
                self.debug.send(f"Received non-JSON data: {data.decode('utf-8').strip()}")
                time.sleep(1)
            except OSError as e:
                if e.winerror == 10057:
                    pass
            except socket.error as e:
                self.debug.send("Socket error:", e)


    def send(self, command: str, data: dict = {}) -> None:
        try:
            if self.socket is not None:
                encoded_data = self.encode_data(command, data)
                self.debug.send(f"socket sent: {command}; {encoded_data}")
                self.socket.send(encoded_data)
            else:
                self.debug.send("No socket has been initialized")
        except (socket.error, BrokenPipeError) as e:
            self.debug.send(f"Socket error: {e}")


    def reconnect(self, ip, port) -> bool:
        self.socket.close()
        self.socket = self.create()
        timeout = 1
        for attempt in range(1, MAX_RECONNECT_ATTEMPTS + 1):
            try:
                self.debug.send(f"Trying to reconnect... Attempt {attempt}/{MAX_RECONNECT_ATTEMPTS}")
                self.socket.connect((ip, port))
                self.debug.send("Reconnected successfully")
                return True
            except socket.error as e:
                self.debug.send(f"Reconnection failed: {e}")
                time.sleep((timeout + attempt) * 2)
        return False


    def connect(self, ip, port) -> None:
        try:
            self.debug.send(f"Trying to connect to the server...")
            self.socket.connect((ip, port))
        except Exception as e:
            print(f"Error occurred when connected to server: {e}")


    def disconnect(self) -> None:
        self.socket.close()
        self.socket = self.create()


