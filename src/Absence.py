from datetime import datetime
from dataclasses import dataclass
from Ui.AbsenceDialog import Ui_AbsenceDialog
from src.Common import DateTimeTools, TimeInterval
from PyQt5.QtWidgets import QDialog

@dataclass(init=True)
class Absence:
    interval   : TimeInterval
    comment    : str
    
    @staticmethod
    def make(ui : Ui_AbsenceDialog):
        absence = Absence(
            interval = TimeInterval(
                DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.fromDateTime.dateTime()),
                DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.untilDateTime.dateTime())
            ),
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
