from datetime import datetime
from dataclasses import dataclass
from Ui.AbsenceDialog import Ui_AbsenceDialog
from src.Common import DateTimeTools
from PyQt5.QtWidgets import QDialog

@dataclass(init=True)
class Absence:
    uid        : int
    from_time  : datetime
    until_time : datetime
    comment    : str
    
    @staticmethod
    def make(ui : Ui_AbsenceDialog):
        absence = Absence(
            uid = int(ui.uidEdit.text()),
            from_time = DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.fromDateTime.dateTime()),
            until_time = DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.untilDateTime.dateTime()),
            comment = ui.commentEdit.text()
        )
        return absence

class AbsenceDialog(QDialog):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.ui = Ui_AbsenceDialog()
        self.ui.setupUi(self)
        
        self.ui.fromDateTime.setDateTime(DateTimeTools.getCurrentDateWithHour())
        self.ui.untilDateTime.setDateTime(DateTimeTools.getCurrentDateWithHour().addDays(1))
