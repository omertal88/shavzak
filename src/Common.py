from dataclasses import dataclass
from enum import Enum, IntFlag, auto
from datetime import datetime, date, time, timedelta
from PyQt5.QtCore import QDateTime, QTime

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
        return QDateTime(QDateTime.currentDateTime().date(),
                        QTime(QDateTime.currentDateTime().time().hour(), 0, 0))

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
    
    def dateAndTimeToDateTime(date : date, time : time) -> datetime:
        return datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)

@dataclass(init = True, repr = True)
class TimeInterval:
    start_time : datetime
    end_time   : datetime
    
    def duration(self) -> timedelta:
        return self.end_time - self.start_time
    
    def __and__(self, other : "TimeInterval"):
        return self.intersects(other)
    
    def intersects(self, other : "TimeInterval"):
        if self.end_time <= other.start_time or \
            other.end_time <= self.start_time:
            return False
        return True
