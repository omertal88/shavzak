import os
import sys

from datetime import timedelta
from os.path import dirname, abspath
from PyQt5.QtWidgets import QMainWindow, QDialog, QAction, QInputDialog, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtCore import QModelIndex, QDateTime
from Ui.ShavzakWindow import Ui_Shavzak

from src.Common import DateTimeTools, TimeInterval
from src.Csv import importFromCsv, exportToCsv
from src.Xlsx import exportToXlsx
from src.Manpower import SoldierDialog, Soldier, Absence
from src.ManpowerModel import ManpowerModel
from src.PositionsModel import PositionsModel
from src.ShiftsModel import ShiftsModel
from src.Positions import PositionDialog, Position
from src.Shifts import ShiftDialog, Shift
from src.Calendar import Calendar
from src.Permutation import generatePermutations
from src.Serialization import SerializedData

class ShavzakWindow(QMainWindow):
    
    def __init__(self, ):
        
        super().__init__()
        
        self.ui = Ui_Shavzak()
        self.ui.setupUi(self)
        
        self.currentPositionUid = 1
        
        nextHourDateTime = DateTimeTools.getCurrentDateWithNextHour()
        self.ui.fromDateTime.setDateTime(nextHourDateTime)
        self.ui.untilDateTime.setDateTime(nextHourDateTime.addDays(1))
        
        self.manpowerModel = ManpowerModel()
        self.positionsModel = PositionsModel()
        self.shiftsModel = ShiftsModel(self.positionsModel)
        
        self.ui.manpowerView.setModel(self.manpowerModel)
        self.ui.positionsView.setModel(self.positionsModel)
        self.ui.shiftsView.setModel(self.shiftsModel)
        
        self.ui.manpowerView.selectionModel().currentRowChanged.connect(self.soldierSelectionChanged)
        self.ui.positionsView.selectionModel().currentRowChanged.connect(self.positionSelectionChanged)
        self.ui.shiftsView.selectionModel().currentRowChanged.connect(self.shiftSelectionChanged)
        
        self.ui.manpowerView.setColumnWidth(0, 130)
        self.ui.manpowerView.setColumnWidth(1, 50)
        self.ui.manpowerView.horizontalHeader().setStretchLastSection(True)
        
        self.ui.positionsView.setColumnWidth(0, 100)
        self.ui.positionsView.setColumnWidth(1, 40)
        self.ui.positionsView.setColumnWidth(2, 40)
        self.ui.positionsView.horizontalHeader().setStretchLastSection(True)
        
        self.ui.shiftsView.setColumnWidth(0, 140)
        self.ui.shiftsView.horizontalHeader().setStretchLastSection(True)
        
        self.exitAction = QAction(self)
        self.exitAction.setShortcut("Esc")
        self.exitAction.triggered.connect(self.promptExit)
        self.addAction(self.exitAction)

        self.calendar = Calendar(self, self.manpowerModel.soldiers, self.positionsModel.positions)
        self.calendar.hide()
        

    ##============================================================================##
    
    def openGenericDialog(self, dialog : QDialog) -> QDialog.DialogCode:
        dialog.show()
        return dialog.exec_()
    
    ##============================================================================##
        
    def addSoldier(self):
        dialog = SoldierDialog(self, self.positionsModel.positions)
        retval : QDialog.DialogCode = self.openGenericDialog(dialog)
        
        if retval == QDialog.Accepted:
            soldier = Soldier.make(dialog.ui)
            self.manpowerModel.add(soldier)
    
    ##============================================================================##
    
    def removeSoldier(self):
        for soldier in self.ui.manpowerView.selectionModel().selectedRows():
            self.manpowerModel.remove(self.manpowerModel.soldiers[soldier.row()])
    
    ##============================================================================##
    
    def editSoldier(self, index : QModelIndex):
        soldier = self.manpowerModel.soldiers[index.row()]
        dialog = SoldierDialog(self, self.positionsModel.positions, soldier)
        retval = self.openGenericDialog(dialog)
        
        if retval == QDialog.Accepted:
            newSoldier = Soldier.make(dialog.ui)
            self.manpowerModel.update(newSoldier)
    
    ##============================================================================##
    
    def addPosition(self):
        dialog = PositionDialog(self)
        dialog.ui.uidEdit.setText(str(self.currentPositionUid))
        retval : QDialog.DialogCode = self.openGenericDialog(dialog)
        
        if retval == QDialog.Accepted:
            self.currentPositionUid += 1
            position = Position.make(dialog.ui)
            self.positionsModel.add(position)
    
    ##============================================================================##
    
    def removePosition(self):
        for position in self.ui.positionsView.selectionModel().selectedRows():
            self.positionsModel.remove(self.positionsModel.positions[position.row()])
    
    ##============================================================================##
    
    def editPosition(self, index : QModelIndex):
        position = self.positionsModel.positions[index.row()]
        dialog = PositionDialog(self, position)
        retval = self.openGenericDialog(dialog)
        
        if retval == QDialog.Accepted:
            newPosition = Position.make(dialog.ui)
            self.positionsModel.positions[index.row()].update(newPosition)
    
    ##============================================================================##
    
    def addShift(self):
        dialog = ShiftDialog(self)
        dialog.ui.positionCombo.addItems([x.name for x in self.positionsModel.positions])
        dialog.ui.positionCombo.setCurrentText(self.positionsModel.positions[self.ui.positionsView.selectedIndexes()[0].row()].name)
        dialog.ui.validFromDatetime = DateTimeTools.getCurrentDateWithHour()
        dialog.ui.validUntilDatetime = DateTimeTools.getCurrentDateWithHour().addDays(7)

        for position in self.positionsModel.positions:
            # TODO: The combobox is not updated if the position is changed in the dialog.
            if position != self.positionsModel.positions[self.ui.positionsView.selectedIndexes()[0].row()]:
                dialog.ui.stickToShiftCombo.addItem(position.name, position)
            
        retval : QDialog.DialogCode = self.openGenericDialog(dialog)
        
        if retval == QDialog.Accepted:
            if dialog.ui.splitShiftCheck.isChecked():
                startTime = dialog.ui.fromTime.time().toPyTime()
                shiftDuration = timedelta(hours = dialog.ui.durationHourSpin.value(),
                                          minutes = dialog.ui.durationMinuteSpin.value()) / dialog.ui.splitShiftSpin.value()
                
                for i in range(dialog.ui.splitShiftSpin.value()):
                    
                    carryTheOne = 0
                    shiftTimeMinutes = int(startTime.minute + i * shiftDuration.total_seconds() / 60 % 60)
                    if shiftTimeMinutes >= 60:
                        shiftTimeMinutes %= 60
                        carryTheOne = 1
                    shiftTimeHours = int((startTime.hour + i * shiftDuration.total_seconds() / 60 / 60 + carryTheOne) % 24)
                    dialog.ui.nicknameEdit.setText("%02d:%02d" % (shiftTimeHours, shiftTimeMinutes))
                    dialog.ui.fromTime.setTime(QTime(shiftTimeHours, shiftTimeMinutes))
                    dialog.ui.durationHourSpin.setValue(shiftDuration.total_seconds() / 60 / 60)
                    dialog.ui.durationMinuteSpin.setValue(shiftDuration.total_seconds() / 60 % 60)
                    
                    shift = Shift.make(dialog.ui, self.positionsModel.positions)
                    self.shiftsModel.add(shift)
            else:
                shift = Shift.make(dialog.ui, self.positionsModel.positions)
                self.shiftsModel.add(shift)
    
    ##============================================================================##
    
    def removeShift(self):
        for shift in self.ui.shiftsView.selectionModel().selectedRows():
            self.shiftsModel.remove(self.shiftsModel.shifts[shift.row()])
    
    ##============================================================================##
    
    def editShift(self, index : QModelIndex):
        shift = self.shiftsModel.shifts[index.row()]
        dialog = ShiftDialog(self, shift)
        dialog.ui.positionCombo.addItems([x.name for x in self.positionsModel.positions])
        dialog.ui.positionCombo.setCurrentText(next(position.name for position in self.positionsModel.positions if position is shift.position))
        
        for position in self.positionsModel.positions:
            # TODO: The combobox is not updated if the position is changed in the dialog.
            if position != self.positionsModel.positions[self.ui.positionsView.selectedIndexes()[0].row()]:
                dialog.ui.stickToShiftCombo.addItem(position.name, position)
                
            if shift.stick_to_position == position:
                dialog.ui.stickToShiftCombo.setCurrentIndex(dialog.ui.stickToShiftCombo.count() - 1)

        retval = self.openGenericDialog(dialog)
        
        if retval == QDialog.Accepted:
            newshift = Shift.make(dialog.ui, self.positionsModel.positions)
            self.shiftsModel.shifts[index.row()].update(newshift)
    
    ##============================================================================##
    
    def soldierSelectionChanged(self, current : QModelIndex, previous : QModelIndex):
        self.ui.removeSoldierButton.setEnabled(current.row() != -1)
    
    ##============================================================================##
    
    def positionSelectionChanged(self, current : QModelIndex, previous : QModelIndex):
        self.ui.removePositionButton.setEnabled(current.row() != -1)
        self.ui.addShiftButton.setEnabled(current.row() != -1)
    
    ##============================================================================##
    
    def shiftSelectionChanged(self, current : QModelIndex, previous : QModelIndex):
        self.ui.removeShiftButton.setEnabled(current.row() != -1)
    
    ##============================================================================##
    
    def openCalendar(self):
        self.calendar.show()
    
    ##============================================================================##
    
    def calculatePermutations(self):
        
        permutations = generatePermutations(self.calendar.schedule, TimeInterval(self.ui.fromDateTime.dateTime().toPyDateTime(),
                                                                                 self.ui.untilDateTime.dateTime().toPyDateTime()),
                                            self.manpowerModel.soldiers,
                                            self.shiftsModel.shifts, maxIterations = 10)
        
        if permutations:
            QMessageBox.information(self, "פרמוטטור", "הפעולה הסתיימה בהצלחה.", QMessageBox.Ok)
            
            for assignment in permutations[0].assignments:
                self.calendar.schedule.add(assignment)
            
            print("std = %.4f" % permutations[0].restAssignmentRatioStd)
            # for soldier in self.manpowerModel.soldiers:
            #     print("%s -> %d assignments (%.1f hours)" % (soldier.name, len([assignment for assignment in permutations[0].schedule.assignments if soldier in assignment.manpower]),
            #                                                              sum([assignment.interval.duration().total_seconds() / 3600 for assignment in permutations[0].schedule.assignments if soldier in assignment.manpower])))
            
        else:
            QMessageBox.critical(self, "פרמוטטור", "הפעולה נכשלה.", QMessageBox.Ok)
            
        
    ##============================================================================##
    
    def importData(self):
        path, _ = QFileDialog.getOpenFileName(self, "ייבא נתונים", directory = dirname(abspath(sys.argv[0])), filter = "*.dat")
        if not path:
            return
        
        if os.path.exists(path):
            data : SerializedData = SerializedData.load(path)
            self.manpowerModel.clear()
            self.positionsModel.clear()
            self.shiftsModel.clear()
            self.calendar.clear()
            
            self.calendar.schedule = data.schedule
            
            self.currentPositionUid = 1
            
            for soldier in data.soldiers:
                self.manpowerModel.add(soldier)
            for position in data.positions:
                self.positionsModel.add(position)
                self.currentPositionUid += 1
            for shift in data.shifts:
                self.shiftsModel.add(shift)
    
    ##============================================================================##
    
    def exportData(self):
        path, _ = QFileDialog.getSaveFileName(self, "ייצא נתונים", directory = dirname(abspath(sys.argv[0])), filter = "*.dat")
        if not path:
            return
        
        data : SerializedData = SerializedData(
            soldiers = self.manpowerModel.soldiers,
            positions = self.positionsModel.positions,
            shifts = self.shiftsModel.shifts,
            schedule = self.calendar.schedule
        )
        data.dump(path)
    
    ##============================================================================##
    
    def importFromCsv(self):
        path, _ = QFileDialog.getOpenFileName(self, "יבוא כוח-אדם", directory = dirname(abspath(sys.argv[0])), filter = "*.csv")
        if not path:
            return
        
        if os.path.exists(path):
            soldiers = importFromCsv(path)
            for soldier in soldiers:
                self.manpowerModel.add(soldier)
    
    ##===========================================================================##
    
    def exportToCsv(self):
        path, _ = QFileDialog.getSaveFileName(self, "יצא כוח-אדם", directory = dirname(abspath(sys.argv[0])), filter = "*.csv")
        
        if not path:
            return
        
        soldiers = self.manpowerModel.soldiers
        exportToCsv(path, soldiers)
    
    ##============================================================================##
    
    def exportToXlsx(self):
        path, _ = QFileDialog.getSaveFileName(self, "ייצוא לאקסל", directory = dirname(abspath(sys.argv[0])), filter = "*.xlsx")
        
        if not path:
            return
        
        exportToXlsx(path, self.calendar.schedule, TimeInterval(self.ui.fromDateTime.dateTime().toPyDateTime(),
                                                                self.ui.untilDateTime.dateTime().toPyDateTime()))
        
    ##============================================================================##
    
    def promptExit(self):
        ret = QMessageBox.question(self, "יציאה", "האם אתה בטוח שברצונך לסגור את הכלי?\nשינויים שלא נשמרו ימחקו", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.close()
