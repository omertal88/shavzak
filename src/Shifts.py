from typing import List, Dict
import datetime
from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt

from src.Common import Weekday, DateTimeTools
from Ui.ShiftDialog import Ui_ShiftDialog

@dataclass(init=True)
class Shift:
    uid : int
    nickname : str
    position_uid : int
    days : int
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
            duration = datetime.timedelta(hours = int(ui.durationHoursEdit.text()), minutes = int(ui.durationMinutesEdit.text())),
            valid_from = DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.validFromDatetime),
            valid_until = DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.validUntilDatetime),
            single_shot=False
        )
        
        return shift
class ShiftDialog(QDialog):
    
    def __init__(self, parent : QWidget, shift : Shift = None):
        
        super().__init__(parent)
        
        self.ui = Ui_ShiftDialog()
        self.ui.setupUi(self)
        
        self.ui.validFromDatetime.setDateTime(DateTimeTools.getCurrentDateWithHour())
        self.ui.validUntilDatetime.setDateTime(DateTimeTools.getCurrentDateWithHour())

        if shift is not None:
            self.ui.uidEdit.setText(str(shift.uid))
            self.ui.nicknameEdit.setText(shift.nickname)
            self.ui.sundayCheck.setChecked(shift.days & Weekday.SUNDAY)
            self.ui.mondayCheck.setChecked(shift.days & Weekday.MONDAY)
            self.ui.tuesdayCheck.setChecked(shift.days & Weekday.TUESDAY)
            self.ui.wednesdayCheck.setChecked(shift.days & Weekday.WEDNESDAY)
            self.ui.thursdayCheck.setChecked(shift.days & Weekday.THURSDAY)
            self.ui.fridayCheck.setChecked(shift.days & Weekday.FRIDAY)
            self.ui.saturdayCheck.setChecked(shift.days & Weekday.SATURDAY)
            
            self.ui.fromTime.setTime(shift.start_time)
            self.ui.durationHoursEdit.setText(str(int(shift.duration.seconds / 3600)))
            self.ui.durationMinutesEdit.setText(str(int(shift.duration.seconds % 3600 / 60)))
            self.ui.validFromDatetime.setDateTime(shift.valid_from)
            self.ui.validUntilDatetime.setDateTime(shift.valid_until)
            
            # self.ui.check