from typing import List, Tuple, Union
from functools import reduce
from abc import ABC, abstractclassmethod, abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidgetItem

from Ui.AssignmentDialog import Ui_AssignmentDialog
from src.Common import SoldierProperty, TimeInterval, hasProperty
from src.Manpower import Soldier
from src.Positions import Position
from src.Shifts import Shift
from src.Assignee import AssigneeDialog

ValidationResult = Union[str, None]
class AssignmentValidationTest(ABC):
    @abstractclassmethod
    def test(assignment : "Assignment") -> ValidationResult: ...

##============================================================================##
    
class AssignmentManpowerCountTest(AssignmentValidationTest):
    def test(assignment : "Assignment") -> ValidationResult:
        return len(assignment.manpower) == assignment.position.needed_manpower

##============================================================================##
class AssignmentManpowerRolesTest(AssignmentValidationTest):
    def test(assignment : "Assignment") -> ValidationResult:
        assignedRoles = [soldier.roles for soldier in assignment.manpower]
        return (reduce(lambda x, y: x | y, assignedRoles, 0) & assignment.position.needed_roles) == assignment.position.needed_roles

##============================================================================##

class AssignmentManualAssignTest(AssignmentValidationTest):
    def test(assignment : "Assignment") -> ValidationResult:
        return len([soldier for soldier in assignment.manpower if hasProperty(soldier.properties, SoldierProperty.MANUAL_ASSIGN)]) == 0

class AssignmentIntervalTest(AssignmentValidationTest):
    def test(assignment : "Assignment") -> ValidationResult:
        return assignment.interval.duration() > timedelta()
    
@dataclass(init = True)
class Assignment:
    interval   : TimeInterval
    position   : Position
    shift      : Union[Shift, None]
    manpower   : List[Soldier]

    @staticmethod
    def make(ui : Ui_AssignmentDialog):
        assignment = Assignment(interval   = TimeInterval(ui.startDatetime.dateTime().toPyDateTime(), ui.endDatetime.dateTime().toPyDateTime()),
                                position   = ui.positionCombo.currentData(Qt.UserRole),
                                shift      = None,
                                manpower   = [ui.soldiersListWidget.item(idx).data(Qt.UserRole) for idx in range(ui.soldiersListWidget.count())]
        )
        return assignment
    
    ##============================================================================##
    
    def update(self, newAssignment : "Assignment"):
        self.interval = newAssignment.interval
        self.position = newAssignment.position
        self.shift    = newAssignment.shift
        self.manpower = newAssignment.manpower
    
    ##============================================================================##
    
    def isManned(self):
        return len(self.manpower)
    
    ##============================================================================##
    
    def isInvalid(self) -> Tuple[bool, List[str]]:
        """ Returns the a list of failed criteria when present """
        failedTests = []
        isCritical = False
        if (not AssignmentManpowerCountTest.test(self)):
            failedTests.append("סדק דרוש לא שווה לסדק ששובץ.")
        if (not AssignmentManpowerRolesTest.test(self)):
            failedTests.append("תפקידים דרושים לא מתקיימים עם הכוח ששובץ.")
        if (not AssignmentManualAssignTest.test(self)):
            failedTests.append("חיילים בכוח מסומנים כשיבוץ ידני בלבד.")
        if (not AssignmentIntervalTest.test(self)):
            isCritical = True
            failedTests.append("זמן סיום איננו אחרי זמן ההתחלה.")
        
        return isCritical, failedTests

##============================================================================##

class AssignmentDialog(QDialog):
    
    def __init__(self, parent, soldiers : List[Soldier]):
        
        super().__init__(parent)
        self.ui = Ui_AssignmentDialog()
        self.ui.setupUi(self)
        
        self.soldiers = soldiers

    def addAssignee(self):
        dialog = AssigneeDialog(self)
        
        assignedSoldiers = []
        for row in range(self.ui.soldiersListWidget.count()):
            soldier = self.ui.soldiersListWidget.item(row).data(Qt.UserRole)
            assignedSoldiers.append(soldier)
        
        # Populate soldiers list
        for soldier in self.soldiers:
            if soldier in assignedSoldiers: continue
            soldierItem = QListWidgetItem("%s (%s)" % (soldier.name, soldier.platoon), dialog.ui.soldiersListWidget)
            soldierItem.setData(Qt.UserRole, soldier)
            dialog.ui.soldiersListWidget.addItem(soldierItem)

        dialog.show()
        if dialog.exec_() != QDialog.Accepted:
            return

        items = dialog.ui.soldiersListWidget.selectedItems()
        if not items:
            return

        for item in items:
            selectedSoldier : Soldier = item.data(Qt.UserRole)
            soldierItem = QListWidgetItem("%s (%s)" % (selectedSoldier.name, selectedSoldier.platoon), self.ui.soldiersListWidget)
            soldierItem.setData(Qt.UserRole, selectedSoldier)
            self.ui.soldiersListWidget.addItem(soldierItem)
    
    def removeAssignee(self):
        self.ui.soldiersListWidget.takeItem(self.ui.soldiersListWidget.selectedIndexes()[0].row())