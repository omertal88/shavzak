from enum import Enum, IntFlag, auto
from datetime import datetime, date, time
from PyQt5.QtCore import QDateTime, QTime
class DialogReturnCode(Enum):
    
    CANCEL = 0
    OK     = 1

class Role(IntFlag):
    COMPANY_COMMANDER  = auto()
    PLATOON_COMMANDER  = auto()
    SQUAD_COMMANDER    = auto()
    RIFLEMAN           = auto()
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
    
class SoldierProperty(IntFlag):
    MANUAL_ASSIGN      = auto()

class Weekday(IntFlag):
    SUNDAY      = auto()
    MONDAY      = auto()
    TUESDAY     = auto()
    WEDNESDAY   = auto()
    THURSDAY    = auto()
    FRIDAY      = auto()
    SATURDAY    = auto()

class DateTimeTools:
    
    @staticmethod
    def getCurrentDateWithHour():
        return QDateTime(
            *[getattr(QDateTime.currentDateTime().date(), attr)() for attr in ("year", "month", "day")],
            QDateTime.currentDateTime().time().hour(), 0, 0)
    
    @classmethod
    def getCurrentDateWithNextHour(cls):
        return cls.getCurrentDateWithHour().addSecs(60 * 60)
    
    @staticmethod
    def qDateTimeToDateTimeNoSeconds(qDateTime : QDateTime) -> datetime:
        return datetime(
                *[getattr(qDateTime.date(), x)() for x in ("year", "month", "day")],
                *[getattr(qDateTime.time(), x)() for x in ("hour", "minute")]
        )
    
    def dateTimeToQDateTime(dateTime : datetime) -> QDateTime:
        return QDateTime(*[getattr(dateTime, attr) for attr in ("year", "month", "day", "hour", "minute", "second")])
    
    def dateTimeToQTime(dateTime : datetime) -> QTime:
        return QTime(*[getattr(dateTime, attr) for attr in ("hour", "minute")])
    
    def dateAndTimeToDateTime(date : date, time : time) -> datetime:
        return datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)