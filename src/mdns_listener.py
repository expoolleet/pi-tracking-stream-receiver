import ast
from PySide6.QtCore import Signal, QObject

import socket
def get_local_ip(server_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect((server_ip, 1))
        IP = s.getsockname()[0]
    finally:
        s.close()
    return IP

class MDNSListener(QObject):

    service_added_signal = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.info = None


    def add_service(self, zeroconf, service_type, name) -> None:
        self.info = zeroconf.get_service_info(service_type, name)
        if self.info:
            server_ip = self.info.properties[b"server_ip"].decode("utf-8")
            stream_protocol = self.info.properties[b"stream_protocol"].decode("utf-8")
            server_port = int(self.info.properties[b"server_port"])
            stream_port = int(self.info.properties[b"stream_port"])

            decoded_stream_size = self.info.properties[b"stream_size"].decode()
            stream_size = ast.literal_eval(decoded_stream_size)

            decoded_camera_size = self.info.properties[b"camera_size"].decode()
            camera_size = ast.literal_eval(decoded_camera_size)

            if stream_protocol == "UDP":
                stream_ip = get_local_ip(server_ip)
            else:
                stream_ip = server_ip

            data = {
                "server_ip": server_ip,
                "server_port": server_port,
                "stream_ip": stream_ip,
                "stream_port": stream_port,
                "stream_protocol": stream_protocol.lower(),
                "stream_size": stream_size,
                "camera_size": camera_size,
            }

            self.service_added_signal.emit(data)
            print(data)

    def update_service(self, zeroconf, service_type, name) -> None:
        return

    def remove_service(self, zeroconf, service_type, name) -> None:
        return