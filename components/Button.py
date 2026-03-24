from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import QSize

class CustomButton(QPushButton):
    def __init__(self, text="Button", variant="primary", parent=None):
        super().__init__(text,parent)
        self.setProperty("variant", variant)
        self.style().unpolish(self)
        self.style().polish(self)
        self.setMinimumSize(QSize(120, 40))
        self.update()