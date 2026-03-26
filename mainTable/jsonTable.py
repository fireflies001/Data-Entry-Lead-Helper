from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt


class JsonTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalHeader().setStretchLastSection(True)
        self.current_session_id = None
        
    def process_data(self, rows):
        GLOBAL_CURRENT_FUNCTION = "process_data()"
        lastalgo = "0"
        try:
            if not rows:
                lastalgo = "1"
                self.setRowCount(0)
                self.setColumnCount(0)
                return
            self.setColumnCount(1)
            self.setHorizontalHeaderLabels(["File Name"])
            self.setRowCount(len(rows))
            lastalgo = "2"
            for row, file_name in enumerate(rows):
                item = QTableWidgetItem(str(file_name))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.setItem(row, 0, item)
        except Exception as e:
            print(f"Error at {GLOBAL_CURRENT_FUNCTION} - {lastalgo} ", e)
