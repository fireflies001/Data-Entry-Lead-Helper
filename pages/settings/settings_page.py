from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QProgressBar
from components.Button import CustomButton
from PySide6.QtCore import QTimer
import csv
class SettingsPage(QWidget):
    def __init__(self, go_home, on_data_uploaded):
        super().__init__()
        layout = QVBoxLayout(self)
        self.on_data_uploaded = on_data_uploaded
        self.upload_btn = CustomButton("Upload File", "secondary")
        self.upload_btn.clicked.connect(self.upload_csv)
        layout.addWidget(self.upload_btn)
        self.btn = CustomButton("go home", "primary")
        self.btn.clicked.connect(go_home)
        self.btn.hide()
        layout.addWidget(self.btn)
        self.progress = QProgressBar()
        self.progress.setRange(0,0)
        self.progress.hide()

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