from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
from src.mdns_listener import MDNSListener

from PySide6.QtCore import QObject

SERVICE_TYPE = "_http._tcp.local."

class ZeroconfHandler(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.zeroconf = Zeroconf()
        self.listener = MDNSListener()
        self.browser = None


    def browse(self) -> None:
        """
        Starts browsing for available services or emitting existing data.
        :return None:
        """
        if self.browser:
            self._clear_browser()
        if not self.zeroconf:
            self.zeroconf = Zeroconf()

        self.browser = ServiceBrowser(self.zeroconf, SERVICE_TYPE, self.listener)


    def clear(self) -> None:
        self._clear_browser()
        self._clear_zeroconf()
        self._clear_listener()


    def _clear_browser(self):
        if self.browser:
            self.browser.cancel()
            self.browser = None


    def _clear_zeroconf(self):
        if self.zeroconf:
            self.zeroconf.close()
            self.zeroconf = None


    def _clear_listener(self):
        if self.listener:
            self.listener.is_service_added = False
            self.listener.data = None