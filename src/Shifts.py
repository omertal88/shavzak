from typing import List, Union
import datetime
from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

from src.Common import Weekday, DateTimeTools
from src.Positions import Position
from Ui.ShiftDialog import Ui_ShiftDialog

@dataclass(init=True)
class Shift:
    nickname : str
    position : Position
    days : int
    start_time : datetime.time
    duration : datetime.timedelta
    valid_from : datetime.datetime
    valid_until : Union[datetime.datetime,None]
    stick_to_position : Union[Position, None] = None

    def make(ui : Ui_ShiftDialog, positions : List[Position]):
        shift = Shift(
            nickname = ui.nicknameEdit.text(),
            position = positions[ui.positionCombo.currentIndex()],
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
            duration = datetime.timedelta(hours = ui.durationHourSpin.value(), minutes = ui.durationMinuteSpin.value()),
            valid_from = DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.validFromDatetime),
            valid_until = DateTimeTools.qDateTimeToDateTimeNoSeconds(ui.validUntilDatetime) if ui.validUntilCheck.isChecked() else None,
            stick_to_position = ui.stickToShiftCombo.currentData(Qt.UserRole)
        )
        
        return shift
    
    def update(self, other : "Shift"):
        self.nickname = other.nickname
        self.position = other.position
        self.days = other.days
        self.start_time = other.start_time
        self.duration = other.duration
        print(other.duration)
        self.valid_from = other.valid_from
        self.valid_until = other.valid_until

##============================================================================##

class ShiftDialog(QDialog):
    
    def __init__(self, parent : QWidget, shift : Shift = None):
        
        super().__init__(parent)
        
        self.ui = Ui_ShiftDialog()
        self.ui.setupUi(self)
        
        self.ui.validFromDatetime.setDateTime(DateTimeTools.getCurrentDateWithHour())
        self.ui.validUntilDatetime.setDateTime(DateTimeTools.getCurrentDateWithHour())

        if shift is not None:
            self.ui.nicknameEdit.setText(shift.nickname)
            self.ui.sundayCheck.setChecked(shift.days & Weekday.SUNDAY)
            self.ui.mondayCheck.setChecked(shift.days & Weekday.MONDAY)
            self.ui.tuesdayCheck.setChecked(shift.days & Weekday.TUESDAY)
            self.ui.wednesdayCheck.setChecked(shift.days & Weekday.WEDNESDAY)
            self.ui.thursdayCheck.setChecked(shift.days & Weekday.THURSDAY)
            self.ui.fridayCheck.setChecked(shift.days & Weekday.FRIDAY)
            self.ui.saturdayCheck.setChecked(shift.days & Weekday.SATURDAY)
            
            self.ui.fromTime.setTime(shift.start_time)
            self.ui.durationHourSpin.setValue(int(shift.duration.total_seconds() / 3600))
            self.ui.durationMinuteSpin.setValue(int(shift.duration.total_seconds() % 3600 / 60))
            self.ui.validFromDatetime.setDateTime(shift.valid_from)
            if shift.valid_until is not None:
                self.ui.validUntilCheck.setChecked(True)
                self.ui.validUntilDatetime.setDateTime(shift.valid_until)
            else:
                self.ui.validUntilCheck.setChecked(False)
            self.ui.splitShiftCheck.setDisabled(True)
            self.ui.splitShiftSpin.setDisabled(True)
            
            # self.ui.check
    
    ##============================================================================##
    
    def done(self, ret : QDialog.DialogCode):
        
        if (ret == QDialog.Accepted):
            
            if self.ui.splitShiftCheck.isChecked():
                
                if (self.ui.durationHourSpin.value() > 24) or (self.ui.durationHourSpin.value() == 24 and self.ui.durationMinuteSpin.value() > 0):
                    
                    QMessageBox.critical(self, "הוספת משמרת", "לא ניתן לפצל משמרת אשר ארוכה יותר מיממה", QMessageBox.Ok)
                    return

                splittedShiftDuration = datetime.timedelta(hours = self.ui.durationHourSpin.value(), minutes = self.ui.durationMinuteSpin.value()) / self.ui.splitShiftSpin.value()
                lastShiftStartHour = (self.ui.fromTime.time().minute() + (splittedShiftDuration * (self.ui.splitShiftSpin.value() - 1)).total_seconds() / 60) / 60 + self.ui.fromTime.time().hour()
                
                if lastShiftStartHour >= 24: # Exceeds to next day
                    QMessageBox.critical(self, "הוספת משמרת", "לא ניתן לפצל משמרת כאשר אחד המופעים מתחיל ביום הבא", QMessageBox.Ok)
                    return
                
        return super().done(ret)
