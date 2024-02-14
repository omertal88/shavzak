from __future__ import annotations
from typing import TYPE_CHECKING
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
    needed_roles : int # bit field (Role)
    properties : int # bit field (PositionProperty)
    required_spacing : timedelta = timedelta()

    @staticmethod
    def make(ui : Ui_NewPositionDialog):
        position = Position(
            uid = int(ui.uidEdit.text()),
            name = ui.positionNameEdit.text(),
            needed_manpower = ui.manpowerSpin.value(),
            needed_roles = (
                Role.COMPANY_COMMANDER  * ui.rolesWidget.companyCommanderCheck.isChecked()     |
                Role.PLATOON_COMMANDER  * ui.rolesWidget.platoonCommanderCheck.isChecked()     |
                Role.SQUAD_COMMANDER    * ui.rolesWidget.squadCommanderCheck.isChecked()  |
                Role.SHARPSHOOTER       * ui.rolesWidget.sharpshooterCheck.isChecked()    |
                Role.GRENADE_LAUNCHER   * ui.rolesWidget.grenadeLauncherCheck.isChecked() |
                Role.MEDIC              * ui.rolesWidget.medicCheck.isChecked()           |
                Role.SNIPER             * ui.rolesWidget.sniperCheck.isChecked()          |
                Role.SIGNALLER          * ui.rolesWidget.signallerCheck.isChecked()       |
                Role.HALAMIST           * ui.rolesWidget.hamalistCheck.isChecked()        |
                Role.HAMAL_RUNNER       * ui.rolesWidget.hamalRunnerCheck.isChecked()     |
                Role.DRIVER             * ui.rolesWidget.driverCheck.isChecked()),
            properties = (
                PositionProperty.ORGANIC_PLATOONS  * ui.organicPlatoonsCheck.isChecked()    |
                PositionProperty.NOT_PHYSICAL      * ui.notPhysicalCheck.isChecked()    |
                PositionProperty.SPACING_NEEDED    * ui.spacingNeededCheck.isChecked()         |
                PositionProperty.NOT_COMMANDER     * ui.notCommanderCheck.isChecked()
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
            
            # Roles
            self.ui.rolesWidget.companyCommanderCheck.setChecked(position.needed_roles & Role.COMPANY_COMMANDER)
            self.ui.rolesWidget.platoonCommanderCheck.setChecked(position.needed_roles & Role.PLATOON_COMMANDER)
            self.ui.rolesWidget.squadCommanderCheck.setChecked(position.needed_roles & Role.SQUAD_COMMANDER)
            self.ui.rolesWidget.sharpshooterCheck.setChecked(position.needed_roles & Role.SHARPSHOOTER)
            self.ui.rolesWidget.grenadeLauncherCheck.setChecked(position.needed_roles & Role.GRENADE_LAUNCHER)
            self.ui.rolesWidget.medicCheck.setChecked(position.needed_roles & Role.MEDIC)
            self.ui.rolesWidget.sniperCheck.setChecked(position.needed_roles & Role.SNIPER)
            self.ui.rolesWidget.signallerCheck.setChecked(position.needed_roles & Role.SIGNALLER)
            self.ui.rolesWidget.hamalistCheck.setChecked(position.needed_roles & Role.HALAMIST)
            self.ui.rolesWidget.hamalRunnerCheck.setChecked(position.needed_roles & Role.HAMAL_RUNNER)
            self.ui.rolesWidget.driverCheck.setChecked(position.needed_roles & Role.DRIVER)

            # Properties
            self.ui.organicPlatoonsCheck.setChecked(position.properties & PositionProperty.ORGANIC_PLATOONS)
            self.ui.notPhysicalCheck.setChecked(position.properties & PositionProperty.NOT_PHYSICAL)
            self.ui.spacingNeededCheck.setChecked(position.properties & PositionProperty.SPACING_NEEDED)
            self.ui.spacingHourSpin.setValue(position.required_spacing.total_seconds() / 60 / 60)
            self.ui.spacingMinuteSpin.setValue(position.required_spacing.total_seconds() / 60 % 60)
            self.ui.notCommanderCheck.setChecked(position.properties & PositionProperty.NOT_COMMANDER)
