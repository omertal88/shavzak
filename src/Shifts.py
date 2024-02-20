from typing import List, Dict
import datetime
from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget

from src.Common import Weekday
from Ui.ShiftDialog import Ui_ShiftDialog

@dataclass(init=True)
class Shift:
    uid : int
    nickname : str
    position_uid : int
    days : List[Weekday]
    start_time : datetime.time
    duration : datetime.timedelta
    valid_from : datetime.datetime
    valid_until : datetime.datetime
    single_shot : bool

    def make(ui : Ui_ShiftDialog, positionsDict : Dict[int, int]):
        shift = Shift(
            uid = int(ui.uidEdit.text()),
            nickname = ui.nicknameEdit.text(),
            position_uid = positionsDict[ui.positionCombo.currentIndex()],
            days = (
                Weekday.SUNDAY     * ui.sundayCheck.isChecked()     |
                Weekday.MONDAY     * ui.mondayCheck.isChecked()     |
                Weekday.TUESDAY    * ui.tuesdayCheck.isChecked()    |
                Weekday.WEDNESDAY  * ui.wednesdayCheck.isChecked()  |
                Weekday.THURSDAY   * ui.thursdayCheck.isChecked()   |
                Weekday.FRIDAY     * ui.fridayCheck.isChecked()     |
                Weekday.SATURDAY   * ui.saturdayCheck.isChecked()
            ),
            start_time = datetime.time(ui.fromTime.time().hour(), ui.fromTime.time().minute()),
            duration = datetime.timedelta(int(ui.durationHoursEdit.text()), int(ui.durationMinutesEdit.text())),
            valid_from = datetime.datetime(
                *[getattr(ui.validFromDatetime.date(), x)() for x in ("year", "month", "day")],
                *[getattr(ui.validFromDatetime.time(), x)() for x in ("hour", "minute")]
            ),
            valid_until = datetime.datetime(
                *[getattr(ui.validUntilDatetime.date(), x)() for x in ("year", "month", "day")],
                *[getattr(ui.validUntilDatetime.time(), x)() for x in ("hour", "minute")]
            ),
            single_shot=False
        )
        
        return shift
class ShiftDialog(QDialog):
    
    def __init__(self, parent : QWidget):
        
        super().__init__(parent)
        
        self.ui = Ui_ShiftDialog()
        self.ui.setupUi(self)
