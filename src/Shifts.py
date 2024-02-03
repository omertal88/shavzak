from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget

from ui.ShiftDialog import Ui_ShiftDialog

class ShiftDialog(QDialog):
    
    def __init__(self, parent : QWidget):
        
        super().__init__(parent)
        
        self.ui = Ui_ShiftDialog()
        self.ui.setupUi(self)

@dataclass(init=True)
class Shift:
    id : int
    position : int
    needed_roles : int # bit field (Role)
    properties : int # bit field (PositionProperty)
