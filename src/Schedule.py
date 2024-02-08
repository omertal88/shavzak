from typing import List, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from src.Common import DateTimeTools
from src.Assignment import Assignment
from src.Shifts import Shift
# if TYPE_CHECKING:
    # from src.Positions import Position


@dataclass(init = False)
class Schedule:
    assignments : List[Assignment]
    
    def __init__(self):
        self.assignments : List[Assignment] = []
    
    ##============================================================================##
    
    def add(self, assignment : Assignment):
        self.assignments.append(assignment)
        self.assignments.sort(key = lambda x: x.interval.start_time) # Make sure this list is always sorted. This assumption will help save precious time
    
    def clear(self):
        self.assignments.clear()
        
    ##============================================================================##
    
    def findNextShift(self, dateTime : datetime, shifts : List[Shift]) -> Tuple[Shift, datetime]:
        
        nearestShift = None
        nearestShiftTime = None
        nearestShiftTimeDelta = None
        
        for shift in shifts:
            iterDateTime = dateTime
            while True:
                shiftWeekday = (iterDateTime.weekday() + 1) % 7  # Make sunday the first day of the week.
                if not shift.days & (1 << shiftWeekday):
                    # The shift is not operating on that weekday.
                    iterDateTime += timedelta(days=1)
                    continue
                
                shiftTime = DateTimeTools.dateAndTimeToDateTime(iterDateTime.date(), shift.start_time)
                timeToShift = shiftTime - dateTime
                
                if timeToShift.total_seconds() < 0:
                    iterDateTime += timedelta(days=1)
                    continue
                
                if shift.position.isAssigned(shiftTime, self):
                    iterDateTime += timedelta(days=1)
                    continue
                
                # Candidate found
                if nearestShift is None or nearestShiftTimeDelta > timeToShift:
                    nearestShift = shift
                    nearestShiftTime = shiftTime
                    nearestShiftTimeDelta = timeToShift
                    
                break
        
        return nearestShift, nearestShiftTime
