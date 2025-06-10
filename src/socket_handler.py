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
    disconnect_from_server_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_connected = False
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
                try:
                    self.update_roi_signal.emit(received_roi)
                except RuntimeError:
                    self.debug.send("Warning: signal 'update_roi_signal' has been deleted because application is closed")
            elif "command" in message:
                if message["command"] == Command.STOP_TRACKING:
                    self.stop_tracking_signal.emit()
                elif message["command"] == Command.DISCONNECT:
                    self.disconnect_from_server_signal.emit()
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
            if self.is_connected:
                encoded_data = self.encode_data(command, data)
                self.debug.send(f"socket sent: {command}; {encoded_data}")
                self.socket.send(encoded_data)
            else:
                self.debug.send(f"No socket connection to the server has been set, command '{command}' was not sent")
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
            if self.is_connected:
                self.disconnect()
            self.debug.send(f"Trying to connect to the server...")
            self.socket.connect((ip, port))
            self.is_connected = True
        except Exception as e:
            print(f"Error occurred when connected to server: {e}")


    def disconnect(self) -> None:
        self.socket.close()
        self.socket = self.create()
        self.is_connected = False


