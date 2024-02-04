from typing import Tuple, Union
from PyQt5.QtWidgets import QMainWindow, QDialog, QListWidgetItem
from PyQt5.QtWidgets import QAction
from PyQt5.QtCore import QModelIndex
from ui.ShavzakWindow import Ui_Shavzak

from src.Common import DialogReturnCode
from src.Manpower import SoldierDialog, Soldier, Absence
from src.ManpowerModel import ManpowerModel
from src.PositionsModel import PositionsModel
from src.ShiftsModel import ShiftsModel
from src.Positions import PositionDialog, Position
from src.Shifts import ShiftDialog, Shift

class ShavzakWindow(QMainWindow):
    
    def __init__(self, ):
        
        super().__init__()
        
        self.ui = Ui_Shavzak()
        self.ui.setupUi(self)
        
        self.currentPositionUid = 1
        self.currentShiftUid = 1
        
        self.manpowerModel = ManpowerModel()
        self.positionsModel = PositionsModel()
        self.shiftsModel = ShiftsModel(self.positionsModel)
        
        self.ui.manpowerView.setModel(self.manpowerModel)
        self.ui.positionsView.setModel(self.positionsModel)
        self.ui.shiftsView.setModel(self.shiftsModel)
        
        self.ui.manpowerView.selectionModel().currentRowChanged.connect(self.soldierSelectionChanged)
        self.ui.positionsView.selectionModel().currentRowChanged.connect(self.positionSelectionChanged)
        self.ui.shiftsView.selectionModel().currentRowChanged.connect(self.shiftSelectionChanged)
        
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

    def openGenericDialog(self, dialog : QDialog) -> DialogReturnCode:
        dialog.show()
        return DialogReturnCode(dialog.exec_())
        
    def addSoldier(self):
        dialog = SoldierDialog(self)
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            soldier = Soldier.make(dialog.ui)
            self.manpowerModel.add(soldier)
            
    def removeSoldier(self):
        for soldier in self.ui.manpowerView.selectionModel().selectedRows():
            self.manpowerModel.remove(self.manpowerModel.soldiers[soldier.row()])
    
    def editSoldier(self, index : QModelIndex):
        soldier = self.manpowerModel.soldiers[index.row()]
        dialog = SoldierDialog(self, soldier)
        retval = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            newSoldier = Soldier.make(dialog.ui)
            self.manpowerModel.update(newSoldier)
    
    def addPosition(self):
        dialog = PositionDialog(self)
        dialog.ui.uidEdit.setText(str(self.currentPositionUid))
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            self.currentPositionUid += 1
            position = Position.make(dialog.ui)
            self.positionsModel.add(position)

    def removePosition(self):
        for position in self.ui.positionsView.selectionModel().selectedRows():
            self.positionsModel.remove(self.positionsModel.positions[position.row()])

    def editPosition(self, index : QModelIndex):
        position = self.positionsModel.positions[index.row()]
        dialog = PositionDialog(self, position)
        retval = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            newPosition = Position.make(dialog.ui)
            self.positionsModel.update(newPosition)
        
    def addShift(self):
        dialog = ShiftDialog(self)
        dialog.ui.uidEdit.setText(str(self.currentShiftUid))
        dialog.ui.positionCombo.addItems([x.name for x in self.positionsModel.positions])
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            self.currentShiftUid += 1
            shift = Shift.make(dialog.ui, [x.uid for x in self.positionsModel.positions])
            self.shiftsModel.add(shift)

    def removeShift(self):
        pass
    
    def editShift(self):
        pass
    
    def soldierSelectionChanged(self, current : QModelIndex, previous : QModelIndex):
        self.ui.removeSoldierButton.setEnabled(current.row() != -1)
        
    def positionSelectionChanged(self, current : QModelIndex, previous : QModelIndex):
        self.ui.removePositionButton.setEnabled(current.row() != -1)
        self.ui.addShiftButton.setEnabled(current.row() != -1)
    
    def shiftSelectionChanged(self, current : QModelIndex, previous : QModelIndex):
        self.ui.removeShiftButton.setEnabled(current.row() != -1)
