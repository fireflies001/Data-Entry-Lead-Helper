from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from components.Button import CustomButton
from mainTable.fileTable import FileTable
class TablePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Home Page"))
        btn_copy_number_rows = CustomButton("Copy numbers", "secodary")
        self.table = FileTable()
        btn_copy_number_rows.clicked.connect(self.table.copy_numbers_from_table)
        layout.addWidget(self.table)
        layout.addWidget(btn_copy_number_rows)

    def normalize(self, text):
        return " ".join(text.replace("\xa0", " ").split()).lower()
    
    def build_full_row(self, row):
        return self.normalize(
            f"{row.get('Mailing Address', '')} "
            f"{row.get('Mailing Unit #', '')} "
            f"{row.get('Mailing City', '')} "
            f"{row.get('Mailing State', '')} "
            f"{row.get('Mailing Zip', '')}"
        )
    def load_data(self, rows):
        GLOBAL_CURRENT_FUNCTION = "load_data()"
        lastalgo = "0"
        try:
            data = []
            for r, row_data in enumerate(rows):
                address_norm = self.build_full_row(row_data)
                if len(row_data.get('Owner 2 First Name')) and len(row_data.get('Owner 2 Last Name')):
                    for x in range(2):
                        data.append((f"{row_data.get(f'Owner {x + 1} First Name')} " f"{row_data.get(f'Owner {x + 1} Last Name')}", 
                                     address_norm, ''))
                else:
                    data.append((f"{row_data.get('Owner 1 First Name')} " f"{row_data.get('Owner 1 Last Name')}", 
                                     address_norm, ''))
            self.table.process_data(data)
        except Exception as e:
            print(f"Error at {GLOBAL_CURRENT_FUNCTION} - {lastalgo} ", e)
            
