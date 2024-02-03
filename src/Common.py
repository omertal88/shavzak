from enum import Enum

class DialogReturnCode(Enum):
    
    CANCEL = 0
    OK     = 1

class Role:
    OFFICER            = 1 << 0
    COMMANDER          = 1 << 1
    SHARPSHOOTER       = 1 << 2
    GRENADE_LAUNCHER   = 1 << 3
    MEDIC              = 1 << 4
    SNIPER             = 1 << 5
    SIGNALLER          = 1 << 6
    
class PositionProperty:
    MIX_PLATOONS       = 1 << 0
    NOT_PHYSICAL       = 1 << 1
    NO_REST_NEEDED     = 1 << 2
