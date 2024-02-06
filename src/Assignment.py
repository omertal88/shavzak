from typing import List
from dataclasses import dataclass
from datetime import datetime, timedelta
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidgetItem

from Ui.AssignmentDialog import Ui_AssignmentDialog
from src.Manpower import Soldier
from src.Positions import Position
from src.Assignee import AssigneeDialog

@dataclass(init = True)
class Assignment:
    uid        : int
    start_time : datetime
    end_time   : datetime
    position   : Position
    manpower   : List[Soldier]

##============================================================================##

class AssignmentDialog(QDialog):
    
    def __init__(self, parent, soldiers : List[Soldier]):
        
        super().__init__(parent)
        self.ui = Ui_AssignmentDialog()
        self.ui.setupUi(self)
        
        self.soldiers = soldiers

    def addAssignee(self):
        dialog = AssigneeDialog(self)
        
        # Populate soldiers list
        for soldier in self.soldiers:
            soldierItem = QListWidgetItem("%s (%s)" % (soldier.name, soldier.platoon), dialog.ui.soldiersListWidget)
            soldierItem.setData(Qt.UserRole, soldier)
            dialog.ui.soldiersListWidget.addItem(soldierItem)

        dialog.show()
        if dialog.exec_() != QDialog.Accepted:
            return

        items = dialog.ui.soldiersListWidget.selectedItems()
        if not items:
            return

        selectedSoldier : Soldier = items[0].data(Qt.UserRole)
        soldierItem = QListWidgetItem("%s (%s)" % (selectedSoldier.name, selectedSoldier.platoon), self.ui.soldiersListWidget)
        soldierItem.setData(Qt.UserRole, selectedSoldier)
        self.ui.soldiersListWidget.addItem(soldierItem)
    
    def removeAssignee(self):
        self.ui.soldiersListWidget.takeItem(self.ui.soldiersListWidget.selectedIndexes()[0].row())