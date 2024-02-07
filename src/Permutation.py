from dataclasses import dataclass
from random import choice
from copy import deepcopy
from typing import List, Union
from datetime import datetime
from src.Common import Role, TimeInterval, SoldierProperty, PositionProperty
from src.Manpower import Soldier
from src.Positions import Position
from src.Shifts import Shift
from src.Assignment import Assignment
from src.Schedule import Schedule

class Permutation(object):
    
    def __init__(self, schedule : Schedule):
        
        self.schedule = deepcopy(schedule)
        self.assignments : List[Assignment] = []

def generatePermutations(history : Schedule, interval : TimeInterval,
                            soldiers : List[Soldier], shifts : List[Shift],
                            maxIterations = 1000):
    
    assert shifts, "Shifts must not be an empty list!"
    assert soldiers, "Soldiers must not be an empty list!"
    
    assignableSoldiers = [soldier for soldier in soldiers if not soldier.properties & SoldierProperty.MANUAL_ASSIGN]
    iterTime : datetime = interval.start_time
    
    # for i in range(maxIterations):
    success = True
    schedule = deepcopy(history)
    
    # Start permutations...
    while success:
        nextShift, nextShiftTime = history.findNextShift(iterTime, shifts)
        if nextShift is None:
            break
        
        if nextShiftTime >= interval.end_time:
            # No more shifts available within this scope
            break
        
        nextShiftInterval = TimeInterval(nextShiftTime, nextShiftTime + nextShift.duration)
        availableSoldiers = [soldier for soldier in assignableSoldiers if soldier.isAvailable(nextShiftInterval, history)]
        position = nextShift.position
        
        mannedSoldiers = manPosition(position, availableSoldiers)
        if mannedSoldiers is None:
            success = False
            break
        
        assignment = Assignment(nextShiftInterval, position, mannedSoldiers)
        history.add(assignment)
        
        iterTime = nextShiftTime

##============================================================================##

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
