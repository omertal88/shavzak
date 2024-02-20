from typing import List
from dataclasses import dataclass
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QIntValidator
from ui.SoldierDialog import Ui_SoldierDialog
from src.Common import Role

@dataclass(init=True)
class Absence:
    from_time  : datetime
    until_time : datetime

@dataclass(init=True)
class Soldier:
    pn : int
    name : str
    platoon : str
    telephone : str
    roles : int
    absences : List[Absence]
    
    @staticmethod
    def make(ui : Ui_SoldierDialog):
        soldier = Soldier(
            pn = ui.pnEdit.text(),
            name = ui.soldierNameEdit.text(),
            platoon = ui.platoonCombo.currentText(),
            telephone = ui.telephoneEdit.text(),
            roles = (Role.OFFICER          * ui.rolesWidget.officerCheck.isChecked()         |
                     Role.COMMANDER        * ui.rolesWidget.commanderCheck.isChecked()       |
                     Role.SHARPSHOOTER     * ui.rolesWidget.sharpshooterCheck.isChecked()    |
                     Role.GRENADE_LAUNCHER * ui.rolesWidget.grenadeLauncherCheck.isChecked() |
                     Role.MEDIC            * ui.rolesWidget.medicCheck.isChecked()           |
                     Role.SNIPER           * ui.rolesWidget.sniperCheck.isChecked()          |
                     Role.SIGNALLER        * ui.rolesWidget.signallerCheck.isChecked()       |
                     Role.HALAMIST         * ui.rolesWidget.hamalistCheck.isChecked()        |
                     Role.HAMAL_RUNNER     * ui.rolesWidget.hamalRunnerCheck.isChecked()),
            absences = []  # Todo: Add absences
        ) # No need to avoid exceptions because we use validator
        
        return soldier
    
class SoldierDialog(QDialog):
    
    def __init__(self, parent : QWidget, soldier : Soldier = None):
        
        super().__init__(parent)
        
        self.ui = Ui_SoldierDialog()
        self.ui.setupUi(self)
                        
        # PN Validator
        pnValidator = QIntValidator(self.ui.pnEdit)
        pnValidator.setBottom(0)
        self.ui.pnEdit.setValidator(pnValidator)
        
        if soldier is not None:
            self.ui.pnEdit.setText(soldier.pn)
            self.ui.soldierNameEdit.setText(soldier.name)
            self.ui.platoonCombo.setCurrentText(soldier.platoon)
            self.ui.telephoneEdit.setText(soldier.telephone)
            
            self.ui.rolesWidget.officerCheck.setChecked(soldier.roles & Role.OFFICER)
            self.ui.rolesWidget.commanderCheck.setChecked(soldier.roles & Role.COMMANDER)
            self.ui.rolesWidget.sharpshooterCheck.setChecked(soldier.roles & Role.SHARPSHOOTER)
            self.ui.rolesWidget.grenadeLauncherCheck.setChecked(soldier.roles & Role.GRENADE_LAUNCHER)
            self.ui.rolesWidget.medicCheck.setChecked(soldier.roles & Role.MEDIC)
            self.ui.rolesWidget.sniperCheck.setChecked(soldier.roles & Role.SNIPER)
            self.ui.rolesWidget.signallerCheck.setChecked(soldier.roles & Role.SIGNALLER)
            self.ui.rolesWidget.hamalistCheck.setChecked(soldier.roles & Role.HALAMIST)
            self.ui.rolesWidget.hamalRunnerCheck.setChecked(soldier.roles & Role.HAMAL_RUNNER)
            self.ui.rolesWidget.driverCheck.setChecked(soldier.roles & Role.DRIVER)
