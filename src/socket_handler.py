import socket
import json
import time
import threading
import numpy as np

from PySide6.QtCore import Qt, Signal, QObject

SOCKET_BUFFER_SIZE = 1024
MAX_RECONNECT_ATTEMPTS = 3

SERVER_IP = "10.20.1.1"
SERVER_PORT = 8001

class SocketData:
    command = ""
    data = {}

class SocketHandler(QObject):

    roi_changed_signal = Signal(np.ndarray)

    def __init__(self):
        self.socket = self.create_socket()
        threading.Thread(target=self.receive_socket)

    def receive_socket(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if not data:
                    print("Server disconnected.")
                    break
                try:
                    message = json.loads(data.decode('utf-8'))
                    if "roi" in message:
                        received_roi = message["roi"]
                        self.roi_changed_signal.emit(received_roi)
                    else:
                        print(f"Received unknown message: {message}")
                except json.JSONDecodeError:
                    print(f"Received non-JSON data: {data.decode('utf-8').strip()}")
            except socket.error as e:
                print("Socket error:", e)


    def create_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def decode_data(self, command, data):
        packet = {
            "command": command,
            "data": data
        }
        raw_data = json.dumps(packet).encode('utf-8')
        return raw_data

    def encode_data(self, raw_data):
        try:
            data_str = raw_data.decode('utf-8')
            data = json.loads(data_str)
            if "data" not in data or data["data"] is None:
                return data.get("message", "")
            else:
                return (data.get("message", ""), data["data"])
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Failed to decode server response: {e}")
            return None


    def socket_send(self, command: str, data: dict = {}):
        try:
            if self.socket is not None:
                print('socket sent:', command, data)
                self.socket.send(self.decode_data(command, data))
                #answer = self.socket.recv(SOCKET_BUFFER_SIZE)
                #return self.encode_data(answer)
            else:
                print("No socket has been initialized")
                #return None
        except (socket.error, BrokenPipeError) as e:
            print(f"Socket error: {e}")
            # if self.reconnect():
            #     return self.socket_send(command, data)
            # else:
            #     print("Failed to reconnect to server")
            #     return None

    def reconnect(self):
        self.socket.close()
        self.socket = self.create_socket()
        timeout = 1
        for attempt in range(1, MAX_RECONNECT_ATTEMPTS + 1):
            try:
                print(f"Trying to reconnect... Attempt {attempt}/{MAX_RECONNECT_ATTEMPTS}")
                self.socket.connect((SERVER_IP, SERVER_PORT))
                print("Reconnected successfully")
                return True
            except socket.error as e:
                print(f"Reconnection failed: {e}")
                time.sleep((timeout + attempt) * 2)
        return False