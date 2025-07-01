from pathlib import Path
import json
import sys

from PySide6.QtCore import QObject

from src.tools import DebugEmitter

class Data(QObject):
    def __init__(self, parent=None, path=None, file_name=None):
        super().__init__(parent)

        if getattr(sys, 'frozen', False):
            base_path = Path(sys.executable)
        else:
            base_path = Path(path).resolve()

        self.save_path = base_path.parent
        self.debug = DebugEmitter()

    def save_to_json(self, file_name, data):
        path = self.save_path / (file_name + ".json")
        try:
            with path.open('w') as file:
                json.dump(data, file, indent=2)
        except Exception as e:
            self.debug.send(f"Failed to save params to json file: {e}")


    def load_from_json(self, file_name):
        path = self.save_path / (file_name + ".json")
        try:
            with path.open('r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError as e:
            self.debug.send(f"Failed to load params from json file: {e}")
            return None
