from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from components.Button import CustomButton
from PySide6.QtCore import Qt
from mainTable.fileTable import FileTable
class TablePage(QWidget):
    def __init__(self):
        super().__init__()
        self.current_session_id = None
        layout = QVBoxLayout(self)
        self.session_text = QLabel("")
        self.session_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.session_text)
        layout.addWidget(QLabel("Home Page"))
        btn_copy_number_rows = CustomButton("Copy numbers", "secondary")
        self.table = FileTable()
        btn_copy_number_rows.clicked.connect(self.table.copy_numbers_from_table)
        layout.addWidget(self.table)
        layout.addWidget(btn_copy_number_rows)

    def normalize_text(self, text):
        return " ".join(text.replace("\xa0", " ").split()).lower()
    
    def build_address(self, row):
        return self.normalize_text(
            f"{row.get('Mailing Address', '')} "
            f"{row.get('Mailing Unit #', '')} "
            f"{row.get('Mailing City', '')} "
            f"{row.get('Mailing State', '')} "
            f"{row.get('Mailing Zip', '')}"
        )
    def set_session_id(self, session_id):
        self.current_session_id = session_id
        self.session_text.setText(self.current_session_id)
        self.table.set_session_id(session_id)
        
    def load_data(self, rows):
        GLOBAL_CURRENT_FUNCTION = "load_data()"
        lastalgo = "0"
        
        try:
            lastalgo = "1"
            data = []
            for r, row_data in enumerate(rows):
                lastalgo = "2"
                address_norm = self.build_address(row_data)
                if len(row_data.get('Owner 2 First Name')) and len(row_data.get('Owner 2 Last Name')):
                    lastalgo = "3"
                    for x in range(2):
                        lastalgo = "4"
                        data.append((f"{row_data.get(f'Owner {x + 1} First Name')} " f"{row_data.get(f'Owner {x + 1} Last Name')}", 
                                     address_norm, ''))
                else:
                    lastalgo = "5"
                    data.append((f"{row_data.get('Owner 1 First Name')} " f"{row_data.get('Owner 1 Last Name')}", 
                                     address_norm, ''))
            self.table.process_data(data)
        except Exception as e:
            print(f"Error at {GLOBAL_CURRENT_FUNCTION} - {lastalgo} ", e)
            
