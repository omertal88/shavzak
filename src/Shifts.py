from typing import List
import datetime
from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget

from src.Common import Weekday
from ui.ShiftDialog import Ui_ShiftDialog

class ShiftDialog(QDialog):
    
    def __init__(self, parent : QWidget):
        
        super().__init__(parent)
        
        self.ui = Ui_ShiftDialog()
        self.ui.setupUi(self)

@dataclass(init=True)
class Shift:
    uid : int
    name : str
    position_uid : int
    days : List[Weekday]
    start_time : datetime.time
    duration : datetime.timedelta
    valid_from : datetime.datetime
    valid_until : datetime.datetime
    single_shot : bool

    # def make(ui : Ui_ShiftDialog):
        # 