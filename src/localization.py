from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QObject

import json
from pathlib import Path

from src.tools import get_base_path

base_path = get_base_path(str(Path(__file__).parent))

RU_STRINGS = "ru"
EN_STRINGS = "en"

def init_icons() -> dict:
    import resources.icons_rc
    ru_icon = QIcon()
    ru_icon.addFile(u":/icons/ru_icon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    en_icon = QIcon()
    en_icon.addFile(u":/icons/en_icon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    return { RU_STRINGS: ru_icon, EN_STRINGS: en_icon }

class Localization(QObject):
    def __init__(self, parent=None, lang=EN_STRINGS):
        super().__init__(parent)
        self.ui = parent.ui if parent and hasattr(parent, "ui") else None
        self.icons = init_icons()
        self._strings = {}
        self.language = lang
        self.ru_lang_strings = {}
        self.en_lang_strings = {}

    def load_strings(self) -> None:
       try:
           with open(base_path / f"resources/lang/{RU_STRINGS}.json", encoding="utf-8-sig") as f:
               self.ru_lang_strings= json.load(f)
           with open(base_path / f"resources/lang/{EN_STRINGS}.json", encoding="utf-8-sig") as f:
               self.en_lang_strings= json.load(f)
       except Exception as e:
           print(f"Error loading language strings: {e}")

    def set_language(self, lang: str) -> None:
        self.language = lang

    def tr(self, key: str) -> str:
        if self.language == RU_STRINGS:
            return self.ru_lang_strings.get(key, key)
        else:
            return self.en_lang_strings.get(key, key)

    def set_localisation(self) -> None:
        if not self.ui:
            raise Exception("UI is not initialized!")

        if hasattr(self.ui, "language_tool_button"):
            self.ui.language_tool_button.setIcon(self.icons[self.language])

        if self.language == RU_STRINGS:
            strings = self.ru_lang_strings
        else:
            strings = self.en_lang_strings

        for attr_name, string in strings.items():
            if hasattr(self.ui, attr_name):
                attr = getattr(self.ui, attr_name)
                if hasattr(attr, "setText"):
                    attr.setText(string)
                elif hasattr(attr, "setTitle"):
                    attr.setTitle(string)
                else:
                    if "tab" in attr_name:
                        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(attr), string)
                    else:
                        print(f"Unknown attribute type: {attr}")