from random import choice
from copy import deepcopy
from typing import List, Tuple, Union
from dataclasses import dataclass
from datetime import datetime, timedelta
from src.Common import DateTimeTools, Role, TimeInterval, SoldierProperty, PositionProperty
from src.Assignment import Assignment
from src.Manpower import Soldier
from src.Positions import Position
from src.Shifts import Shift


@dataclass(init = False)
class Schedule:
    assignments : List[Assignment]
    
    def __init__(self):
        self.assignments : List[Assignment] = []
    
    ##============================================================================##
    
    def add(self, assignment : Assignment):
        self.assignments.append(assignment)
        self.assignments.sort(key = lambda x: x.start_time) # Make sure this list is always sorted. This assumption will help save precious time
    
    def clear(self):
        self.assignments.clear()
        
    ##============================================================================##
    
    def generatePermutations(self, history : "Schedule", interval : TimeInterval,
                             soldiers : List[Soldier], shifts : List[Shift],
                             maxIterations = 1000):
        
        assignableSoldiers = [soldier for soldier in soldiers if not soldier.properties & SoldierProperty.MANUAL_ASSIGN]
        iterTime : datetime = interval.start_time
        
        for i in range(maxIterations):
            success = True
            schedule = deepcopy(history)
            
            # Start permutations...
            while success:
                nextShift, nextShiftTime = self.findNextShift(schedule, iterTime, shifts)
                if nextShiftTime > interval.end_time:
                    # No more shifts available within this scope
                    break
                
                nextShiftInterval = TimeInterval(nextShiftTime, nextShiftTime + nextShift.duration)
                availableSoldiers = [soldier for soldier in assignableSoldiers if soldier.isAvailable(nextShiftInterval, history)]
                position = nextShift.position
                
                mannedSoldiers = Schedule.manPosition(history, position, availableSoldiers)
                if mannedSoldiers is None:
                    success = False
                    break
    
    @staticmethod
    def manPosition(position : Position, soldiers : List[Soldier]) -> Union[List[Soldier],None]:
        
        mannedSoldiers : List[Soldier] = []
        platoonBound = False
        
        if position.needed_roles:
            for role in Role:
                if not role & position.needed_roles:
                    continue
                
                # This role is needed
                relevantSoldiers = [soldier for soldier in soldiers if soldier.roles & role]
                if not relevantSoldiers:
                    return None
                
                # Randomly pick a soldier
                randomSoldier = choice(relevantSoldiers)
                mannedSoldiers.append(randomSoldier)
                
                if not position.properties & PositionProperty.MIX_PLATOONS and not platoonBound:
                    platoonBound = True
                    soldiers = [soldier for soldier in soldiers if soldier.platoon == randomSoldier.platoon]
                    soldiers.remove(randomSoldier)
                    
        while position.needed_manpower != len(mannedSoldiers):
            if not soldiers:
                # We ran out of soldiers to assign
                return None
            
            randomSoldier = choice(soldiers)
            mannedSoldiers.append(randomSoldier)
            
            if not position.properties & PositionProperty.MIX_PLATOONS and not platoonBound:
                platoonBound = True
                soldiers = [soldier for soldier in soldiers if soldier.platoon == randomSoldier.platoon]

            soldiers.remove(randomSoldier)
            
        return mannedSoldiers
    
    @staticmethod
    def findNextShift(history : "Schedule", dateTime : datetime, shifts : List[Shift]) -> Tuple[Shift, datetime]:
        
        nearestShift = None
        nearestShiftTime = None
        nearestShiftTimeDelta = None
        
        for shift in shifts:
            iterDateTime = dateTime
            while True:
                shiftWeekday = (dateTime.weekday() + 1) % 7  # Make sunday the first day of the week.
                if not shift.days & (1 << shiftWeekday):
                    # The shift is not operating on that weekday.
                    iterDateTime += timedelta(days=1)
                    continue
                
                shiftTime = DateTimeTools.dateAndTimeToDateTime(iterDateTime.date(), shift.start_time)
                timeToShift = shiftTime - dateTime
                
                if timeToShift.total_seconds() < 0:
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
    
    @staticmethod
    def isShiftOngoing(shift : Shift, dateTime : datetime, history : "Schedule"):
        
        for assignment in reversed(history.assignments):
            if assignment.position is shift.position:
                if assignment.start_time <= dateTime < assignment.end_time:
                    return True
        
        # Shift not found in history
        return False
