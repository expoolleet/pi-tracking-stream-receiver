from pathlib import Path
import json
import sys

from PySide6.QtCore import QObject

class Data(QObject):
    def __init__(self, parent=None, save_path=None):
        super().__init__(parent)

        if getattr(sys, 'frozen', False):
            base_path = Path(sys.executable)
        else:
            base_path = Path(__file__).resolve().parent

        self.save_path = base_path.parent



    def to_json(self, file_name, data):
        path = self.save_path / (file_name + ".json")
        with path.open('w') as file:
            json.dump(data, file, indent=2)

    def from_json(self, file_name):
        path = self.save_path / (file_name + ".json")
        try:
            with path.open('r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return None
