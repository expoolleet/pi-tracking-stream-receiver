from pathlib import Path
import json

from PySide6.QtCore import QObject

class Data(QObject):
    def __init__(self, parent=None, save_path=None):
        super().__init__(parent)

        self.save_path = Path(save_path).parent

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
