from PyQt5.QtWidgets import QWidget
from ui.RolesWidget import Ui_RolesWidget

class RolesWidget(QWidget, Ui_RolesWidget):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.setupUi(self)
        
        self.setFocusProxy(self.officerCheck)
