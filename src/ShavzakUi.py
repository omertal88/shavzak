from typing import Tuple, Union
from PyQt5.QtWidgets import QMainWindow, QDialog, QListWidgetItem
from PyQt5.QtWidgets import QAction
from ui.ShavzakWindow import Ui_Shavzak
from ui.SoldierDialog import Ui_SoldierDialog
from ui.PositionDialog import Ui_NewPositionDialog
from ui.ShiftDialog import Ui_ShiftDialog

from src.Common import DialogReturnCode
from src.Manpower import SoldierDialog, Soldier, Absence

class ShavzakWindow(QMainWindow):
    
    def __init__(self, ):
        
        super().__init__()
        
        self.ui = Ui_Shavzak()
        self.ui.setupUi(self)
        
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
        
        
    def removeSoldier(self):
        pass
    
    def editSoldier(self):
        pass
    def addNewPosition(self):
        pass
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
        self.ui.removeSoldierButton.setEnabled(len(self.ui.manpowerList.selectedItems))
        self.ui.removePositionButton.setEnabled(len(self.ui.positionsList.selectedItems))
        self.ui.removeShiftButton.setEnabled(len(self.ui.shiftsList.selectedItems))