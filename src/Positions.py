from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog, QWidget

from ui.PositionDialog import Ui_NewPositionDialog
from src.Common import Role, PositionProperty

@dataclass(init=True)
class Position:
    uid : int
    name : str
    needed_manpower : int
    needed_roles : int # bit field (Role)
    properties : int # bit field (PositionProperty)

    @staticmethod
    def make(ui : Ui_NewPositionDialog):
        position = Position(
            uid = int(ui.uidEdit.text()),
            name = ui.positionNameEdit.text(),
            needed_manpower = int(ui.manpowerEdit.text()),
            needed_roles = (
                Role.OFFICER          * ui.rolesWidget.officerCheck.isChecked()         |
                Role.COMMANDER        * ui.rolesWidget.commanderCheck.isChecked()       |
                Role.SHARPSHOOTER     * ui.rolesWidget.sharpshooterCheck.isChecked()    |
                Role.GRENADE_LAUNCHER * ui.rolesWidget.grenadeLauncherCheck.isChecked() |
                Role.MEDIC            * ui.rolesWidget.medicCheck.isChecked()           |
                Role.SNIPER           * ui.rolesWidget.sniperCheck.isChecked()          |
                Role.SIGNALLER        * ui.rolesWidget.signallerCheck.isChecked()       |
                Role.HALAMIST         * ui.rolesWidget.hamalistCheck.isChecked()        |
                Role.HAMAL_RUNNER     * ui.rolesWidget.hamalRunnerCheck.isChecked()     |
                Role.DRIVER           * ui.rolesWidget.driverCheck.isChecked()),
            properties = (
                PositionProperty.MIX_PLATOONS    * ui.mixPlatoonsCheck.isChecked()    |
                PositionProperty.NOT_PHYSICAL    * ui.notPhysicalCheck.isChecked()    |
                PositionProperty.NO_REST_NEEDED  * ui.noRestCheck.isChecked()         |
                PositionProperty.NOT_COMMANDER   * ui.notCommanderCheck.isChecked()
            )
        )
        
        return position
    
class PositionDialog(QDialog):
    
    def __init__(self, parent : QWidget, position : Position = None):
        
        super().__init__(parent)
        
        self.ui = Ui_NewPositionDialog()
        self.ui.setupUi(self)
        
        if position is not None:
            
            self.ui.uidEdit.setText(str(position.uid))
            self.ui.positionNameEdit.setText(position.name)
            self.ui.manpowerEdit.setText(str(position.needed_manpower))
            
            # Roles
            self.ui.rolesWidget.officerCheck.setChecked(position.needed_roles & Role.OFFICER)
            self.ui.rolesWidget.commanderCheck.setChecked(position.needed_roles & Role.COMMANDER)
            self.ui.rolesWidget.sharpshooterCheck.setChecked(position.needed_roles & Role.SHARPSHOOTER)
            self.ui.rolesWidget.grenadeLauncherCheck.setChecked(position.needed_roles & Role.GRENADE_LAUNCHER)
            self.ui.rolesWidget.medicCheck.setChecked(position.needed_roles & Role.MEDIC)
            self.ui.rolesWidget.sniperCheck.setChecked(position.needed_roles & Role.SNIPER)
            self.ui.rolesWidget.signallerCheck.setChecked(position.needed_roles & Role.SIGNALLER)
            self.ui.rolesWidget.hamalistCheck.setChecked(position.needed_roles & Role.HALAMIST)
            self.ui.rolesWidget.hamalRunnerCheck.setChecked(position.needed_roles & Role.HAMAL_RUNNER)
            self.ui.rolesWidget.driverCheck.setChecked(position.needed_roles & Role.DRIVER)

            # Properties
            self.ui.mixPlatoonsCheck.setChecked(position.properties & PositionProperty.MIX_PLATOONS)
            self.ui.notPhysicalCheck.setChecked(position.properties & PositionProperty.NOT_PHYSICAL)
            self.ui.noRestCheck.setChecked(position.properties & PositionProperty.NO_REST_NEEDED)
            self.ui.notCommanderCheck.setChecked(position.properties & PositionProperty.NOT_COMMANDER)