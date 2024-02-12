from typing import List, Union, Tuple, TYPE_CHECKING
from dataclasses import dataclass
from datetime import timedelta

from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QIntValidator
from Ui.SoldierDialog import Ui_SoldierDialog
from src.Absence import Absence, AbsenceDialog
from src.AbsencesModel import AbsencesModel
from src.Common import Role, SoldierProperty, PositionProperty, TimeInterval, hasProperty
if TYPE_CHECKING:
    from src.Assignment import Assignment
    from src.Schedule import Schedule

##============================================================================##

@dataclass(init=True)
class Soldier:
    pn : str
    name : str
    platoon : str
    telephone : str = ""
    roles : int = 0
    comment: str = ""
    absences : List[Absence] = None
    properties : int = 0
    
    ##============================================================================##
    
    @staticmethod
    def make(ui : Ui_SoldierDialog):
        soldier = Soldier(
            pn = ui.pnEdit.text(),
            name = ui.soldierNameEdit.text(),
            platoon = ui.platoonCombo.currentText(),
            telephone = ui.telephoneEdit.text(),
            roles = (Role.COMPANY_COMMANDER.value  * ui.rolesWidget.companyCommanderCheck.isChecked()     |
                     Role.PLATOON_COMMANDER.value  * ui.rolesWidget.platoonCommanderCheck.isChecked()     |
                     Role.SQUAD_COMMANDER.value    * ui.rolesWidget.squadCommanderCheck.isChecked()       |
                     Role.SHARPSHOOTER.value       * ui.rolesWidget.sharpshooterCheck.isChecked()         |
                     Role.GRENADE_LAUNCHER.value   * ui.rolesWidget.grenadeLauncherCheck.isChecked()      |
                     Role.MEDIC.value              * ui.rolesWidget.medicCheck.isChecked()                |
                     Role.SNIPER.value             * ui.rolesWidget.sniperCheck.isChecked()               |
                     Role.SIGNALLER.value          * ui.rolesWidget.signallerCheck.isChecked()            |
                     Role.HALAMIST.value           * ui.rolesWidget.hamalistCheck.isChecked()             |
                     Role.HAMAL_RUNNER.value       * ui.rolesWidget.hamalRunnerCheck.isChecked()          |
                     Role.DRIVER.value             * ui.rolesWidget.driverCheck.isChecked()),
            comment = ui.commentEdit.text(),
            absences = ui.absencesView.model().absences,
            properties = (SoldierProperty.MANUAL_ASSIGN.value    * ui.manualAssignCheck.isChecked())
        ) # No need to avoid exceptions because we use validator
        
        return soldier
    
    ##============================================================================##
    
    def update(self, other : "Soldier"):
        self.pn = other.pn
        self.name = other.name
        self.platoon = other.platoon
        self.telephone = other.telephone
        self.roles = other.roles
        self.comment = other.comment
        self.absences = other.absences
        self.properties = other.properties
        
    ##============================================================================##
    
    @staticmethod
    def makeFromCsv(pn : int, name : str, platoon : str, roles : int, telephone : str, properties : int, comment : str):
        
        soldier = Soldier(
            pn = pn,
            name = name,
            platoon = platoon,
            roles = roles,
            telephone = telephone,
            properties = properties,
            comment = comment,
            absences=[]
        )
        return soldier
    
    ##============================================================================##
    
    def isOnShift(self, interval : TimeInterval, schedule : "Schedule"):
        
        for assignment in reversed(schedule.assignments):
            if self in assignment.manpower:
                if interval.intersects(assignment.interval):
                    return True
        
        return False
    
    ##============================================================================##
    
    def isAbsent(self, timeInterval : TimeInterval):
        
        for absence in self.absences:
            if timeInterval.intersects(absence.interval):
                return True
        
        # No intersection found.
        return False
    
    ##============================================================================##
    
    def isAvailable(self, interval : TimeInterval, schedule : "Schedule"):
        
        if hasProperty(self.properties, SoldierProperty.MANUAL_ASSIGN) or self.isAbsent(interval) or self.isOnShift(interval, schedule):
            return False
        
        return True
    
    ##============================================================================##
    
    def getRestTimestForInterval(self, interval : TimeInterval, schedule : "Schedule") -> Tuple[Union[timedelta, None],Union[timedelta, None]]:
        
        restBeforeInterval = restAfterInterval = None
        soldierAssignments = [assignment for assignment in schedule.assignments if self in assignment.manpower]
        
        for assignment in soldierAssignments:
            assignmentRestTimeBefore = assignment.interval.start_time - interval.end_time # Rest time between end of `interval` and start of assignment
            assignmentRestTimeAfter = interval.start_time - assignment.interval.end_time # Rest time between end of assignment and start of `interval`
            
            if assignmentRestTimeAfter > timedelta() and (restBeforeInterval is None or assignmentRestTimeAfter < restBeforeInterval):
                restBeforeInterval = assignmentRestTimeAfter
            if assignmentRestTimeBefore > timedelta() and (restAfterInterval is None or assignmentRestTimeBefore < restAfterInterval):
                restAfterInterval = assignmentRestTimeBefore
        
        return restBeforeInterval, restAfterInterval
    
    ##============================================================================##
    
    def calculateRestToAssignmentRatio(self, schedule : "Schedule", interval : TimeInterval) -> float: 
        
        assignments : List[Assignment] = []
        
        for assignment in schedule.assignments:

            # TODO: Go back to this criteria
            if self in assignment.manpower and \
              interval.contains(assignment.interval.start_time, include_start_point = True): # and
            #   not assignment.position.properties & PositionProperty.SPACING_NEEDED:
                
                assignments.append(assignment)
    
        if not len(assignments):
            # In case of just 1 assignment we don't know the rest duration
            return float('inf')
        
        assignments.sort(key = lambda x: x.interval.start_time)  # Should be sorted already but just in case
        
        # Correction in order to make sure that `interval` begins with an assignment
        interval.start_time = assignments[0].interval.start_time
        
        totalAssignmentTime : timedelta = sum([assignment.interval.duration() for assignment in assignments], timedelta())
        totalRestTime       : timedelta = interval.duration() - totalAssignmentTime

        return float(totalRestTime.total_seconds()) / float(totalAssignmentTime.total_seconds())
    
##============================================================================##

class SoldierDialog(QDialog):
    
    def __init__(self, parent : QWidget, soldier : Soldier = None):
        
        super().__init__(parent)
        
        self.ui = Ui_SoldierDialog()
        self.ui.setupUi(self)
        
        self.currentAbsenceUid : int = 1
        
        self.absencesModel = AbsencesModel()
        self.ui.absencesView.setModel(self.absencesModel)
        self.ui.absencesView.setColumnWidth(0, 130)
        self.ui.absencesView.setColumnWidth(1, 130)
        self.ui.absencesView.setColumnWidth(2, 200)
        self.ui.absencesView.horizontalHeader().setStretchLastSection(True)
                        
        # PN Validator
        pnValidator = QIntValidator(self.ui.pnEdit)
        pnValidator.setBottom(0)
        self.ui.pnEdit.setValidator(pnValidator)
        
        if soldier is not None:
            self.ui.pnEdit.setText(soldier.pn)
            self.ui.soldierNameEdit.setText(soldier.name)
            self.ui.platoonCombo.setCurrentText(soldier.platoon)
            self.ui.telephoneEdit.setText(soldier.telephone)
            self.ui.commentEdit.setText(soldier.comment)

            self.ui.rolesWidget.companyCommanderCheck.setChecked(soldier.roles & Role.COMPANY_COMMANDER)
            self.ui.rolesWidget.platoonCommanderCheck.setChecked(soldier.roles & Role.PLATOON_COMMANDER)
            self.ui.rolesWidget.squadCommanderCheck.setChecked(soldier.roles & Role.SQUAD_COMMANDER)
            self.ui.rolesWidget.sharpshooterCheck.setChecked(soldier.roles & Role.SHARPSHOOTER)
            self.ui.rolesWidget.grenadeLauncherCheck.setChecked(soldier.roles & Role.GRENADE_LAUNCHER)
            self.ui.rolesWidget.medicCheck.setChecked(soldier.roles & Role.MEDIC)
            self.ui.rolesWidget.sniperCheck.setChecked(soldier.roles & Role.SNIPER)
            self.ui.rolesWidget.signallerCheck.setChecked(soldier.roles & Role.SIGNALLER)
            self.ui.rolesWidget.hamalistCheck.setChecked(soldier.roles & Role.HALAMIST)
            self.ui.rolesWidget.hamalRunnerCheck.setChecked(soldier.roles & Role.HAMAL_RUNNER)
            self.ui.rolesWidget.driverCheck.setChecked(soldier.roles & Role.DRIVER)
            
            self.ui.manualAssignCheck.setChecked(soldier.properties & SoldierProperty.MANUAL_ASSIGN)
            
            currentAbsenceUid = 1
            for absence in soldier.absences:
                if currentAbsenceUid <= absence.uid:
                    currentAbsenceUid = absence.uid + 1
                self.absencesModel.add(absence)
            
            self.currentAbsenceUid = currentAbsenceUid

    ##============================================================================##
    
    def addAbsence(self):
        dialog = AbsenceDialog(self)
        dialog.ui.uidEdit.setText(str(self.currentAbsenceUid))
        dialog.show()
        if dialog.exec_() == QDialog.Accepted:
            self.currentAbsenceUid += 1
            absence = Absence.make(dialog.ui)
            self.absencesModel.add(absence)
    
    ##============================================================================##
    
    def removeAbsence(self):
        if len(self.ui.absencesView.selectedIndexes()):
            absence = self.absencesModel.absences[self.ui.absencesView.selectedIndexes()[0].row()]
            self.absencesModel.remove(absence)
