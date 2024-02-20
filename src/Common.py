from enum import Enum, IntFlag, auto

class DialogReturnCode(Enum):
    
    CANCEL = 0
    OK     = 1

class Role(IntFlag):
    OFFICER            = auto()
    COMMANDER          = auto()
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

class Weekday(Enum):
    SUNDAY      = 1
    MONDAY      = 2
    TUESDAY     = 3
    WEDNESDAY   = 4
    THURSDAY    = 5
    FRIDAY      = 6
    SATURDAY    = 7
