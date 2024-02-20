import os
import sys

from os.path import dirname, abspath
from PyQt5.QtWidgets import QMainWindow, QDialog, QAction, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QModelIndex, QDateTime
from Ui.ShavzakWindow import Ui_Shavzak

from src.Common import DialogReturnCode, DateTimeTools
from src.CsvImporter import importFromCsv
from src.Manpower import SoldierDialog, Soldier, Absence
from src.ManpowerModel import ManpowerModel
from src.PositionsModel import PositionsModel
from src.ShiftsModel import ShiftsModel
from src.Positions import PositionDialog, Position
from src.Shifts import ShiftDialog, Shift
from src.Serialization import SerializedData

class ShavzakWindow(QMainWindow):
    
    def __init__(self, ):
        
        super().__init__()
        
        self.ui = Ui_Shavzak()
        self.ui.setupUi(self)
        
        self.currentPositionUid = 1
        self.currentShiftUid = 1
        
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
        self.ui.manpowerView.setColumnWidth(1, 60)
        self.ui.manpowerView.horizontalHeader().setStretchLastSection(True)
        
        self.ui.positionsView.setColumnWidth(0, 100)
        self.ui.positionsView.setColumnWidth(1, 40)
        self.ui.positionsView.setColumnWidth(2, 40)
        self.ui.positionsView.horizontalHeader().setStretchLastSection(True)
        
        self.ui.shiftsView.setColumnWidth(0, 100)
        self.ui.shiftsView.setColumnWidth(1, 40)
        self.ui.shiftsView.setColumnWidth(2, 40)
        self.ui.shiftsView.horizontalHeader().setStretchLastSection(True)
        
        self.exitAction = QAction(self)
        self.exitAction.setShortcut("Esc")
        self.exitAction.triggered.connect(self.close)
        self.addAction(self.exitAction)
    
    ##============================================================================##
    
    def openGenericDialog(self, dialog : QDialog) -> DialogReturnCode:
        dialog.show()
        return DialogReturnCode(dialog.exec_())
    
    ##============================================================================##
        
    def addSoldier(self):
        dialog = SoldierDialog(self)
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            soldier = Soldier.make(dialog.ui)
            self.manpowerModel.add(soldier)
    
    ##============================================================================##
    
    def removeSoldier(self):
        for soldier in self.ui.manpowerView.selectionModel().selectedRows():
            self.manpowerModel.remove(self.manpowerModel.soldiers[soldier.row()])
    
    ##============================================================================##
    
    def editSoldier(self, index : QModelIndex):
        soldier = self.manpowerModel.soldiers[index.row()]
        dialog = SoldierDialog(self, soldier)
        retval = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            newSoldier = Soldier.make(dialog.ui)
            self.manpowerModel.update(newSoldier)
    
    ##============================================================================##
    
    def addPosition(self):
        dialog = PositionDialog(self)
        dialog.ui.uidEdit.setText(str(self.currentPositionUid))
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
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
        
        if retval == DialogReturnCode.OK:
            newPosition = Position.make(dialog.ui)
            self.positionsModel.update(newPosition)
    
    ##============================================================================##
    
    def addShift(self):
        dialog = ShiftDialog(self)
        dialog.ui.uidEdit.setText(str(self.currentShiftUid))
        dialog.ui.positionCombo.addItems([x.name for x in self.positionsModel.positions])
        dialog.ui.positionCombo.setCurrentText(self.positionsModel.positions[self.ui.positionsView.selectedIndexes()[0].row()].name)
        dialog.ui.validFromDatetime = DateTimeTools.getCurrentDateWithHour()
        dialog.ui.validUntilDatetime = DateTimeTools.getCurrentDateWithHour().addDays(7)
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            self.currentShiftUid += 1
            shift = Shift.make(dialog.ui, [x.uid for x in self.positionsModel.positions])
            self.shiftsModel.add(shift)
    
    ##============================================================================##
    
    def removeShift(self):
        pass
    
    ##============================================================================##
    
    def editShift(self):
        pass
    
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
    
    def importData(self):
        path, accepted = QInputDialog.getText(self, "ייבא נתונים", "אנא הכנס נתיב לקובץ השמור", text = "%s" % os.path.join(dirname(abspath(sys.argv[0])), "shavzak.dat"))
        if not accepted:
            return
        
        if os.path.exists(path):
            data : SerializedData = SerializedData.load(path)
            self.manpowerModel.clear()
            self.positionsModel.clear()
            self.shiftsModel.clear()
            
            self.currentPositionUid = 1
            self.currentShiftUid = 1
            
            for soldier in data.soldiers:
                self.manpowerModel.add(soldier)
            for position in data.positions:
                self.positionsModel.add(position)
                self.currentPositionUid += 1
            for shift in data.shifts:
                self.shiftsModel.add(shift)
                self.currentShiftUid += 1
    
    ##============================================================================##
    
    def exportData(self):
        path, accepted = QInputDialog.getText(self, "ייצא נתונים", "אנא הכנס נתיב לשמירת הקובץ", text = "%s" % os.path.join(dirname(abspath(sys.argv[0])), "shavzak.dat"))
        if not accepted:
            return
        
        data : SerializedData = SerializedData(
            soldiers = self.manpowerModel.soldiers,
            positions = self.positionsModel.positions,
            shifts = self.shiftsModel.shifts
        )
        data.dump(path)
    
    ##============================================================================##
    
    def importFromCsv(self):
        path, accepted = QInputDialog.getText(self, "ייבא נתונים", "אנא הכנס נתיב לקובץ הידני", text = "%s" % os.path.join(dirname(abspath(sys.argv[0])), "soldiers.csv"))
        if not accepted:
            return
        
        if os.path.exists(path):
            soldiers = importFromCsv(path)
            for soldier in soldiers:
                self.manpowerModel.add(soldier)