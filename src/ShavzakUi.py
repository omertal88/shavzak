from typing import Tuple, Union
from PyQt5.QtWidgets import QMainWindow, QDialog, QListWidgetItem
from PyQt5.QtWidgets import QAction
from ui.ShavzakWindow import Ui_Shavzak

from src.Common import DialogReturnCode
from src.Manpower import SoldierDialog, Soldier, Absence
from src.Positions import PositionDialog, Position

class ShavzakWindow(QMainWindow):
    
    def __init__(self, ):
        
        super().__init__()
        
        self.ui = Ui_Shavzak()
        self.ui.setupUi(self)
        
        self.soldiers = list()
        self.positions = list()
        
        self.exitAction = QAction(self)
        self.exitAction.setShortcut("Esc")
        self.exitAction.triggered.connect(self.close)
        self.addAction(self.exitAction)

    def openGenericDialog(self, dialog : QDialog) -> DialogReturnCode:
        dialog.show()
        return DialogReturnCode(dialog.exec_())
        
    def addNewSoldier(self):
        dialog = SoldierDialog(self)
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        
        if retval == DialogReturnCode.OK:
            soldier = Soldier.makeSoldier(dialog.ui)
            newSoldierListItem = QListWidgetItem(self.ui.manpowerList)
            newSoldierListItem.setText("%s (%s)" % (soldier.name, soldier.platoon))
            
            self.soldiers.append(soldier)
        
    def removeSoldier(self):
        self.ui.manpowerList.takeItem(self.ui.manpowerList.currentRow())
    
    def editSoldier(self):
        pass
    def addNewPosition(self):
        dialog = PositionDialog(self)
        retval : DialogReturnCode = self.openGenericDialog(dialog)
        # TODO: Continue tomorrow :)

    def removePosition(self):
        pass
    def editPosition(self):
        pass
    def addNewShift(self):
        pass
    def removeShift(self):
        pass
    def editShift(self):
        pass
    
    def selectionChanged(self):
        self.ui.removeSoldierButton.setEnabled(self.ui.manpowerList.currentItem() is not None)
        self.ui.removePositionButton.setEnabled(self.ui.positionsList.currentItem() is not None)
        self.ui.removeShiftButton.setEnabled(self.ui.positionsList.currentItem() is not None)