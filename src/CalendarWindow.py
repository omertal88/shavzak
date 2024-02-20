from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate
from Ui.Calendar import Ui_Calendar

class CalendarWindow(QMainWindow):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.ui = Ui_Calendar()
        self.ui.setupUi(self)

    def selectNewDate(date : QDate):
        pass
