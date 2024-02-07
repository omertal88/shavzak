from typing import List
from datetime import timedelta
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QListWidgetItem
from PyQt5.QtCore import Qt, QDate, QModelIndex, QDateTime, QTime
from Ui.Calendar import Ui_Calendar
from src.Common import TimeInterval
from src.Manpower import Soldier
from src.Positions import Position
from src.Assignment import Assignment, AssignmentDialog
from src.AssignmentsModel import AssignmentsModel, Column
from src.Schedule import Schedule

class CalendarWindow(QMainWindow):
    
    def __init__(self, parent, soldiers, positions):
        
        super().__init__(parent)
        self.ui = Ui_Calendar()
        self.ui.setupUi(self)
        
        self.ui.calendarWidget.setSelectedDate(QDate.currentDate())
        self.ui.calendarWidget.showToday()
        
        self.soldiers  : List[Soldier] = soldiers
        self.positions : List[Position] = positions

        self.currentAssignmentUid = 1
        self.schedule = Schedule()
        
        self.assignmentsModel = AssignmentsModel(positions)
        self.ui.assignmentsView.setModel(self.assignmentsModel)
        self.ui.assignmentsView.setColumnWidth(Column.START_TIME, 120)
        self.ui.assignmentsView.setColumnWidth(Column.END_TIME, 120)
        self.ui.assignmentsView.horizontalHeader().setStretchLastSection(True)
        
        self.ui.assignmentsView.selectionModel().currentRowChanged.connect(self.selectNewAssignment)
    
    ##============================================================================##
    
    def reloadSelectedDate(self):
        
        self.assignmentsModel.clear()
        selectedDayInterval = TimeInterval(QDateTime(self.ui.calendarWidget.selectedDate(), QTime()).toPyDateTime(),
                                           QDateTime(self.ui.calendarWidget.selectedDate(), QTime()).toPyDateTime() + timedelta(days=1))
        for assignment in self.schedule.assignments:
            if assignment.interval.intersects(selectedDayInterval):
                self.assignmentsModel.add(assignment)
        
    ##============================================================================##
    
    def addAssignment(self):
        # Open assignment dialog
        dialog = AssignmentDialog(self, self.soldiers)
        
        # Populate positions:
        for position in self.positions:
            dialog.ui.positionCombo.addItem(position.name, position)
        
        dialog.ui.startDatetime.setDateTime(QDateTime(self.ui.calendarWidget.selectedDate(), QTime()))
        dialog.ui.endDatetime.setDateTime(QDateTime(self.ui.calendarWidget.selectedDate(), QTime()))
        
        dialog.show()
        if dialog.exec_() == QDialog.Rejected:
            return
        
        assignment = Assignment.make(dialog.ui)
        
        if not self.validateAssignment(assignment):
            return
            
        self.currentAssignmentUid += 1
        
        self.schedule.add(assignment)
        self.reloadSelectedDate()
    
    ##============================================================================##
    
    def validateAssignment(self, assignment : Assignment) -> bool:
        
        criticalFailure, failedTests = assignment.isInvalid()
        if failedTests:
            if criticalFailure:
                QMessageBox.critical(self, "הוספת משימה", "אזהרת שיבוץ:\n%s" % "\n".join(failedTests), QMessageBox.Ok)
                return False
            
            response = QMessageBox.warning(self, "הוספת משימה", "אזהרת שיבוץ:\n%s\n\nאשר כדי להמשיך בכל זאת" % "\n".join(failedTests), QMessageBox.Ok | QMessageBox.Cancel)
            if response == QMessageBox.Cancel:
                return False
        
        return True
        
    ##============================================================================##
    
    def removeAssignment(self):
        
        rows = self.ui.assignmentsView.selectedIndexes()
        
        if not rows:
            return
        
        row = rows[0].row()
        self.assignmentsModel.removeRows(QModelIndex(), row, row)
        self.schedule.assignments.pop(row)
        
    ##============================================================================##
    
    def editAssignment(self, index : QModelIndex):
        
        assignment = self.assignmentsModel.assignments[index.row()]
        
        dialog = AssignmentDialog(self, self.soldiers)
        
        # Populate positions:
        for position in self.positions:
            dialog.ui.positionCombo.addItem(position.name, position)
        
        dialog.ui.positionCombo.setCurrentText(assignment.position.name)
        
        dialog.ui.startDatetime.setDateTime(assignment.interval.start_time)
        dialog.ui.endDatetime.setDateTime(assignment.interval.end_time)
        
        for soldier in assignment.manpower:
            soldierItem = QListWidgetItem("%s (%s)" % (soldier.name, soldier.platoon), dialog.ui.soldiersListWidget)
            soldierItem.setData(Qt.UserRole, soldier)
            dialog.ui.soldiersListWidget.addItem(soldierItem)
        
        dialog.show()
        if dialog.exec_() == QDialog.Rejected:
            return

        newAssignment = Assignment.make(dialog.ui)
        if not self.validateAssignment(newAssignment):
            return
        
        assignment.update(newAssignment)
        self.reloadSelectedDate()

    ##============================================================================##
    
    def selectNewAssignment(self, current : QModelIndex, previous : QModelIndex):
        assignment = self.assignmentsModel.assignments[current.row()]
        self.ui.manpowerListWidget.clear()
        self.ui.manpowerListWidget.addItems(["%s (%s)" % (soldier.name, soldier.platoon) for soldier in assignment.manpower])
    
    ##============================================================================##
    
    def showEvent(self, event):
        
        self.reloadSelectedDate()
        return super().showEvent(event)
        
    def clear(self):
        self.schedule.clear()