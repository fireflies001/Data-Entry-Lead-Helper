from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
class FileTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.itemClicked.connect(self.copy_cell_text)

    def copy_cell_text(self, item):
        GLOBAL_CURRENT_FUNCTION = "copy_cell_text()"
        try:
            if item.column() in (0, 1):  # Name or Type
                QApplication.clipboard().setText(item.text())
            elif item.column() == 2:
                clipboard_text = QApplication.clipboard().text()
                if clipboard_text:
                    item.setText(clipboard_text)
        except Exception as e:
            print(f"Error at {GLOBAL_CURRENT_FUNCTION} ", e)

    def process_data(self, rows):
        GLOBAL_CURRENT_FUNCTION = "process_data()"
        lastalgo = "0"
        try:
            if not rows:
                lastalgo = "1"
                self.setRowCount(0)
                self.setColumnCount(0)
                return
            self.setColumnCount(3)
            self.setHorizontalHeaderLabels(["Name","Address","Number"])
            self.setRowCount(len(rows))
            lastalgo = "2"
            for row, rowData in enumerate(rows):
                for c, value in enumerate(rowData):
                    item = QTableWidgetItem(str(value))

                    if c in (0,1):
                        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.setItem(row,c,item)
        except Exception as e:
            print(f"Error at {GLOBAL_CURRENT_FUNCTION} - {lastalgo} ", e)
    def copy_numbers_from_table(self):
        values = []

        for row in range(self.rowCount()):
            item = self.item(row, 2)
            if item and item.text().strip():
                values.append(item.text().strip())
                
        QApplication.clipboard().setText("\n".join(values))