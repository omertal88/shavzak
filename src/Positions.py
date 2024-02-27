from __future__ import annotations
from typing import TYPE_CHECKING, Dict
from datetime import datetime, timedelta
from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget

from Ui.PositionDialog import Ui_NewPositionDialog
from src.Common import Role, PositionProperty

if TYPE_CHECKING:
    from src.Schedule import Schedule

@dataclass(init=True)
class Position:
    uid : int
    name : str
    needed_manpower : int
    needed_roles : Dict[Role, int] # Count needed for each role
    properties : int # bit field (PositionProperty)
    required_spacing : timedelta = timedelta()
    priority : int = 0

    @staticmethod
    def make(ui : Ui_NewPositionDialog):
        position = Position(
            uid = int(ui.uidEdit.text()),
            name = ui.positionNameEdit.text(),
            needed_manpower = ui.manpowerSpin.value(),
            priority = ui.prioritySpin.value(),
            needed_roles = {
                Role.COMPANY_COMMANDER :  ui.companyCommanderSpin.value() ,
                Role.PLATOON_COMMANDER :  ui.platoonCommanderSpin.value() ,
                Role.SQUAD_COMMANDER   :  ui.squadCommanderSpin.value()   ,
                Role.SHARPSHOOTER      :  ui.sharpshooterSpin.value()     ,
                Role.GRENADE_LAUNCHER  :  ui.grenadeLauncherSpin.value()  ,
                Role.MEDIC             :  ui.medicSpin.value()            ,
                Role.SNIPER            :  ui.sniperSpin.value()           ,
                Role.SIGNALLER         :  ui.signallerSpin.value()        ,
                Role.HALAMIST          :  ui.hamalistSpin.value()         ,
                Role.HAMAL_RUNNER      :  ui.hamalRunnerSpin.value()      ,
                Role.DRIVER            :  ui.driverSpin.value()           ,
                Role.RIFLEMAN          :  ui.riflemanSpin.value()
                
            },
            properties = (
                PositionProperty.ORGANIC_PLATOONS  * ui.organicPlatoonsCheck.isChecked()   |
                PositionProperty.NOT_PHYSICAL      * ui.notPhysicalCheck.isChecked()       |
                PositionProperty.SPACING_NEEDED    * ui.spacingNeededCheck.isChecked()     |
                PositionProperty.NOT_COMMANDER     * ui.notCommanderCheck.isChecked()      |
                PositionProperty.RESTING_POSITION  * ui.restingPositionCheck.isChecked()
            ),
            required_spacing = timedelta(hours = ui.spacingHourSpin.value(),
                                         minutes = ui.spacingMinuteSpin.value()) if ui.spacingNeededCheck.isChecked() else timedelta()
        )
        
        return position
    
    ##============================================================================##
    
    def update(self, position : "Position"):
        self.name = position.name
        self.needed_manpower = position.needed_manpower
        self.needed_roles = position.needed_roles
        self.properties = position.properties
        self.required_spacing = position.required_spacing
    
    ##============================================================================##
    
    def isAssigned(self, dateTime : datetime, schedule : Schedule):
        # TODO: Fix this
        for assignment in reversed(schedule.assignments):
            if assignment.position == self:
                if assignment.interval.contains(dateTime, include_start_point = True):
                    return True
        
        # Shift not found in history
        return False

##============================================================================##

class PositionDialog(QDialog):
    
    def __init__(self, parent : QWidget, position : Position = None):
        
        super().__init__(parent)
        
        self.ui = Ui_NewPositionDialog()
        self.ui.setupUi(self)
        
        if position is not None:
            self.ui.uidEdit.setText(str(position.uid))
            self.ui.positionNameEdit.setText(position.name)
            self.ui.manpowerSpin.setValue(position.needed_manpower)
            self.ui.prioritySpin.setValue(position.priority)
            
            # Roles
            if isinstance(position.needed_roles, int):
                position.needed_roles = {}

            if Role.RIFLEMAN not in position.needed_roles:
                position.needed_roles[Role.RIFLEMAN] = 0
                
            self.ui.companyCommanderSpin.setValue(position.needed_roles.get(Role.COMPANY_COMMANDER, 0))
            self.ui.platoonCommanderSpin.setValue(position.needed_roles.get(Role.PLATOON_COMMANDER, 0))
            self.ui.squadCommanderSpin.setValue(position.needed_roles.get(Role.SQUAD_COMMANDER, 0))
            self.ui.sharpshooterSpin.setValue(position.needed_roles.get(Role.SHARPSHOOTER, 0))
            self.ui.grenadeLauncherSpin.setValue(position.needed_roles.get(Role.GRENADE_LAUNCHER, 0))
            self.ui.medicSpin.setValue(position.needed_roles.get(Role.MEDIC, 0))
            self.ui.sniperSpin.setValue(position.needed_roles.get(Role.SNIPER, 0))
            self.ui.signallerSpin.setValue(position.needed_roles.get(Role.SIGNALLER, 0))
            self.ui.hamalistSpin.setValue(position.needed_roles.get(Role.HALAMIST, 0))
            self.ui.hamalRunnerSpin.setValue(position.needed_roles.get(Role.HAMAL_RUNNER, 0))
            self.ui.driverSpin.setValue(position.needed_roles.get(Role.DRIVER, 0))
            self.ui.riflemanSpin.setValue(position.needed_roles.get(Role.RIFLEMAN, 0))

            # Properties
            self.ui.organicPlatoonsCheck.setChecked(position.properties & PositionProperty.ORGANIC_PLATOONS)
            self.ui.notPhysicalCheck.setChecked(position.properties & PositionProperty.NOT_PHYSICAL)
            self.ui.spacingNeededCheck.setChecked(position.properties & PositionProperty.SPACING_NEEDED)
            self.ui.spacingHourSpin.setValue(position.required_spacing.total_seconds() / 60 / 60)
            self.ui.spacingMinuteSpin.setValue(position.required_spacing.total_seconds() / 60 % 60)
            self.ui.notCommanderCheck.setChecked(position.properties & PositionProperty.NOT_COMMANDER)
            self.ui.restingPositionCheck.setChecked(position.properties & PositionProperty.RESTING_POSITION)
