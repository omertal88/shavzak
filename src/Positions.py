from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget

from ui.PositionDialog import Ui_NewPositionDialog

class PositionDialog(QDialog):
    
    def __init__(self, parent : QWidget):
        
        super().__init__(parent)
        
        self.ui = Ui_NewPositionDialog()
        self.ui.setupUi(self)

@dataclass(init=True)
class Position:
    name : str
    needed_manpower : int
    needed_roles : int # bit field (Role)
    properties : int # bit field (PositionProperty)
