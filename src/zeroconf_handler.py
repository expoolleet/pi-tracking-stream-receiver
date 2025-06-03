from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
from src.mdns_listener import MDNSListener

from PySide6.QtCore import QObject

SERVICE_TYPE = "_http._tcp.local."

class ZeroconfHandler(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.zeroconf = Zeroconf()
        self.listener = MDNSListener()

    def browse(self) -> None:
        ServiceBrowser(self.zeroconf, SERVICE_TYPE, self.listener)