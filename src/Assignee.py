from typing import List
from PyQt5.QtWidgets import QDialog
from Ui.AssigneeDialog import Ui_AssigneeDialog
from src.Manpower import Soldier

class AssigneeDialog(QDialog):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.ui = Ui_AssigneeDialog()
        self.ui.setupUi(self)
