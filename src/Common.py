from enum import Enum, IntFlag, auto

class DialogReturnCode(Enum):
    
    CANCEL = 0
    OK     = 1

class Role(IntFlag):
    COMPANY_COMMANDER  = auto()
    PLATOON_COMMANDER  = auto()
    SQUAD_COMMANDER    = auto()
    SHARPSHOOTER       = auto()
    GRENADE_LAUNCHER   = auto()
    MEDIC              = auto()
    SNIPER             = auto()
    SIGNALLER          = auto()
    HALAMIST           = auto()
    HAMAL_RUNNER       = auto()
    DRIVER             = auto()
    
class PositionProperty(IntFlag):
    MIX_PLATOONS       = auto()
    NOT_PHYSICAL       = auto()
    NO_REST_NEEDED     = auto()
    NOT_COMMANDER      = auto()

class Weekday(IntFlag):
    SUNDAY      = auto()
    MONDAY      = auto()
    TUESDAY     = auto()
    WEDNESDAY   = auto()
    THURSDAY    = auto()
    FRIDAY      = auto()
    SATURDAY    = auto()
