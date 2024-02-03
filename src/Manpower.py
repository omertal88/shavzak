from typing import List
from dataclasses import dataclass
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QIntValidator
from ui.SoldierDialog import Ui_SoldierDialog

class SoldierDialog(QDialog):
    
    def __init__(self, parent : QWidget):
        
        super().__init__(parent)
        self.ui = Ui_SoldierDialog()
        self.ui.setupUi(self)
        
        # PN Validator
        pnValidator = QIntValidator(self.ui.pnEdit)
        pnValidator.setBottom(0)
        self.ui.pnEdit.setValidator(pnValidator)
        
class Role:
    OFFICER            = 1 << 0
    COMMANDER          = 1 << 1
    SHARPSHOOTER       = 1 << 2
    GRENADE_LAUNCHER   = 1 << 3
    MEDIC              = 1 << 4
    SNIPER             = 1 << 5
    SIGNALLER          = 1 << 6

@dataclass(init=True)
class Absence:
    from_time  : datetime
    until_time : datetime

@dataclass(init=True)
class Soldier:
    pn : int
    name : str
    platoon : str
    roles : int
    absences : List[Absence]
    
    @classmethod
    def makeSoldier(cls, ui : Ui_SoldierDialog):
        soldier = Soldier(
            pn = int(ui.pnEdit.text()),
            name = ui.soldierNameEdit.text(),
            platoon = ui.platoonCombo.currentText(),
            roles = (Role.OFFICER          * ui.officerCheck.isChecked()      |
                     Role.COMMANDER        * ui.commanderCheck.isChecked()    |
                     Role.SHARPSHOOTER     * ui.sharpshooterCheck.isChecked() |
                     Role.GRENADE_LAUNCHER * ui.grenLauncherCheck.isChecked() |
                     Role.MEDIC            * ui.medicCheck.isChecked()        |
                     Role.SNIPER           * ui.sniperCheck.isChecked()       |
                     Role.SIGNALLER        * ui.signallerCheck.isChecked()),
            absences = []
        ) # No need to avoid exceptions because we use validator
        
        return soldier