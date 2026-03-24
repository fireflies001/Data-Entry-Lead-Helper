import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
from pages.settings.settings_page import SettingsPage
from pages.table.table_page import TablePage


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(relative_path)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lead Helper")
        self.resize(600, 600)
        self.stack = QStackedWidget()
        self.settings_page = SettingsPage(self.show_home, self.handleFileUpload)
        self.home_page = TablePage()
        self.stack.addWidget(self.settings_page)
        self.stack.addWidget(self.home_page)
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.stack)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setLayout(layout)
    def handleFileUpload(self, rows):
        self.home_page.load_data(rows)
        self.show_home()

    def show_home(self):
        self.stack.setCurrentWidget(self.home_page)

    def show_settings(self):
        self.stack.setCurrentWidget(self.settings_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(resource_path("style/main.qss").read_text(encoding="utf-8"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
