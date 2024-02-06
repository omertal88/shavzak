from typing import List
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt, QDate, QModelIndex
from Ui.Calendar import Ui_Calendar
from src.Common import DateTimeTools
from src.Manpower import Soldier
from src.Positions import Position
from src.Assignment import Assignment, AssignmentDialog
from src.AssignmentsModel import AssignmentsModel
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
        self.ui.assignmentsView.setColumnWidth(0, 100)
        self.ui.assignmentsView.setColumnWidth(1, 50)
        
        self.ui.assignmentsView.selectionModel().currentRowChanged.connect(self.selectNewAssignment)
    
    ##============================================================================##
    
    def reloadSelectedDate(self):
        
        self.assignmentsModel.clear()
        for assignment in self.schedule.assignments:
            if assignment.start_time.date() == self.ui.calendarWidget.selectedDate().toPyDate():
                self.assignmentsModel.add(assignment)
    
    ##============================================================================##
    
    def addAssignment(self):
        # Open assignment dialog
        dialog = AssignmentDialog(self, self.soldiers)
        
        # Populate positions:
        for position in self.positions:
            dialog.ui.positionCombo.addItem(position.name, position)
        
        dialog.ui.startDatetime.setDateTime(DateTimeTools.getCurrentDateWithNextHour())
        dialog.ui.endDatetime.setDateTime(DateTimeTools.getCurrentDateWithNextHour())
        
        dialog.show()
        if dialog.exec_() == QDialog.Rejected:
            return
        
        assignment = Assignment(uid = self.currentAssignmentUid,
                                start_time = dialog.ui.startDatetime.dateTime().toPyDateTime(),
                                end_time   = dialog.ui.endDatetime.dateTime().toPyDateTime(),
                                position   = dialog.ui.positionCombo.currentData(Qt.UserRole),
                                manpower   = [dialog.ui.soldiersListWidget.item(idx).data(Qt.UserRole) for idx in range(dialog.ui.soldiersListWidget.count())]
        )
        self.currentAssignmentUid += 1
        
        self.schedule.add(assignment)
        self.reloadSelectedDate()
    
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
        
        dialog.ui.startDatetime.setDateTime(assignment.start_time)
        dialog.ui.endDatetime.setDateTime(assignment.end_time)
        
        dialog.show()
        if dialog.exec_() == QDialog.Rejected:
            return
        
        self.assignmentsModel.update(assignment)

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