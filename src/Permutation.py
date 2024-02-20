from copy import deepcopy
from typing import List, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from src.Common import DateTimeTools, Role
from src.Assignment import Assignment
from src.Manpower import Soldier
from src.Positions import Position
from src.Shifts import Shift

class Schedule:
    uid         : int
    assignments : List[Assignment]
    
    def __init__(self, uid : int):
        self.assignments : List[Assignment] = []
    
    ##============================================================================##
    
    def add(self, assignment : Assignment):
        self.assignments.append(assignment)
        self.assignments.sort(key = lambda x: x.start_time) # Make sure this list is always sorted. This assumption will help save precious time
    
    ##============================================================================##
    
    def generatePermutations(self, history : "Schedule", startTime : datetime, endTime : datetime,
                             soldiers : List[Soldier], positions : List[Position], shifts : List[Shift],
                             maxIterations = 1000):
        
        iterTime : datetime = startTime
        
        for i in range(maxIterations):
            schedule = deepcopy(history)
            
            # Start permutations...
            while True:
                nextShift, nextShiftTime = self.findNextShift(schedule, iterTime, shifts)
                if nextShiftTime > endTime:
                    # No more shifts available within this scope
                    break
                
                # Found the shift - now assign manpower
                firstSoldier = True
                availableSoldiers = [soldier for soldier in soldiers if not self.isSoldierOnShift(soldier, nextShiftTime, history)]
                position = next(position for position in positions if position.uid == nextShift.position_uid)  # TODO: What if we deleted the position?
                success = True
                
                assignedRoles = 0
                for i in range(position.needed_manpower):
                    if not availableSoldiers:
                        success = False
                        break
                    
                    if position.needed_roles:
                        for role in Role:
                            if not role & position.needed_roles:
                                continue
                            # This role is needed
                            relevantSoldiers = [soldier for soldier in availableSoldiers if soldier.roles & role]
                            if not relevantSoldiers:
                                success = False
                                break
                            
                    
                if not success:
                    continue
                    
    
    @staticmethod
    def findNextShift(history : "Schedule", dateTime : datetime, shifts : List[Shift]) -> Tuple[Shift, datetime]:
        
        nearestShift = None
        nearestShiftTime = None
        nearestShiftTimeDelta = None
        
        iterDateTime = dateTime
        for shift in shifts:
            while True:
                shiftWeekday = (dateTime.weekday() + 1) % 7  # Make sunday the first day of the week.
                if not shift.days & (1 << shiftWeekday):
                    # The shift is not operating on that weekday.
                    iterDateTime += timedelta(days=1)
                    continue
                
                shiftTime = DateTimeTools.dateAndTimeToDateTime(iterDateTime.date(), shift.start_time)
                timeToShift = shiftTime - dateTime
                
                if timeToShift.total_seconds < 0:
                    iterDateTime += timedelta(days=1)
                    continue
                
                if Schedule.isShiftOngoing(shift, shiftTime, history):
                    break
                
                # Candidate found
                if nearestShift is None or nearestShiftTimeDelta > timeToShift:
                    nearestShift = shift
                    nearestShiftTime = shiftTime
                    nearestShiftTimeDelta = timeToShift
                    
                break
        
        return nearestShift, nearestShiftTime
    
    # @staticmethod
    # def timeToShift()
            
    @staticmethod
    def isShiftOngoing(shift : Shift, dateTime : datetime, history : "Schedule"):
        
        for assignment in reversed(history.assignments):
            if assignment.shift == shift.uid:
                return assignment.start_time <= dateTime < assignment.end_time
        
        # Shift not found in history
        return False
    
    @staticmethod
    def isSoldierOnShift(soldier : Soldier, dateTime : datetime, history : "Schedule"):
        
        for assignment in reversed(history.assignments):
            if assignment.start_time <= dateTime <= assignment.end_time:
                if soldier.pn in assignment.manpower:
                    return True
        
        return False
