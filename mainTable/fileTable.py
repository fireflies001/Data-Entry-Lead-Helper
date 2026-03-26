from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
import json
from pathlib import Path
from datetime import datetime
class FileTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_session_id = None
        self.itemClicked.connect(self.copy_cell_text)

    def set_session_id(self, session_id):
        self.current_session_id = session_id

    def copy_cell_text(self, item):
        GLOBAL_CURRENT_FUNCTION = "copy_cell_text()"
        try:
            if item.column() in (0, 1):  # Name or Type
                QApplication.clipboard().setText(item.text())
            elif item.column() == 2:
                clipboard_text = QApplication.clipboard().text()
                if clipboard_text:
                    item.setText(clipboard_text)
                    self.save_data_on_edit()
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
        previous_address = None

        for row in range(self.rowCount()):
            address_item = self.item(row, 1)
            item = self.item(row, 2)
            if not address_item or not item:
                continue

            address = address_item.text().strip()
            number = item.text().strip()

            if address == previous_address and values:
                values[-1] += " " + number
            else:
                values.append(number)

            previous_address = address
                
        QApplication.clipboard().setText("\n".join(values))

    def save_data_on_edit(self):
        data = []
        autosave_dir = Path("autosaves")
        autosave_dir.mkdir(exist_ok=True)
        now = datetime.now().strftime("%Y-%m-%d")
        for row in range(self.rowCount()):
            data_row = {}
            for col in range(self.columnCount()):
                header_item = self.horizontalHeaderItem(col)
                item = self.item(row, col)
                data_row[header_item.text()] = item.text() if item else ""
            data.append(data_row)
        output_path = autosave_dir / f"table_autosave_{self.current_session_id}.json"

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
