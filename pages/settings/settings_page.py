from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QProgressBar, QLabel
from components.Button import CustomButton
from PySide6.QtCore import QTimer, Qt
from pathlib import Path
from mainTable.jsonTable import JsonTable
import csv
class SettingsPage(QWidget):
    def __init__(self, go_home, on_data_uploaded):
        super().__init__()
        self.current_session_id = ""
        layout = QVBoxLayout(self)
        self.on_data_uploaded = on_data_uploaded
        self.upload_btn = CustomButton("Upload File", "secondary")
        self.upload_btn.clicked.connect(self.upload_csv)
        self.session_text = QLabel("")
        self.session_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.table = JsonTable()
        self.autosaves_files()
        layout.addWidget(self.session_text)
        layout.addWidget(self.table)
        layout.addWidget(self.upload_btn)
        self.btn = CustomButton("go home", "primary")
        self.btn.clicked.connect(go_home)
        self.btn.hide()
        layout.addWidget(self.btn)
        self.progress = QProgressBar()
        self.progress.setRange(0,0)
        self.progress.hide()
        layout.addWidget(self.progress)

    def upload_csv(self):
        GLOBAL_CURRENT_FUNCTION = "process_data()"
        lastalgo = "0"
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "select CSV File", "", "CSV Files (*.csv)")
            if not file_path:
                return
            self.progress.show()
            self.upload_btn.setEnabled(False)
            QTimer.singleShot(50, lambda: self.process_csv_to_data(file_path))
        except Exception as e:
            print(f"Error at {GLOBAL_CURRENT_FUNCTION} - {lastalgo} ", e)

    def process_csv_to_data(self, file_path):
        GLOBAL_CURRENT_FUNCTION = "process_data()"
        lastalgo = "0"
        try:
            with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            self.on_data_uploaded(rows)
        except Exception as e:
            print(f"Error at {GLOBAL_CURRENT_FUNCTION} - {lastalgo} ", e)
        finally:
            self.progress.hide()
            self.upload_btn.setEnabled(True)

    def autosaves_files(self):
        data = []
        autosave_dir = Path("autosaves")
        json_files = list(autosave_dir.glob("*.json")) if autosave_dir.exists() else []
        file_names = [path.name for path in json_files]

        self.table.process_data(file_names) 
    
    def set_session_id(self, session_id):
        self.current_session_id = session_id
        self.session_text.setText(self.current_session_id)
