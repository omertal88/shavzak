from array import array
from statistics import stdev
from random import choice
from copy import deepcopy
from typing import List, Union, Tuple
from datetime import datetime
from multiprocessing.pool import Pool
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
        self.restAssignmentRatioStd : float = float('inf')
        self.unassignedSoldiers = List[Soldier]
        # self.soldiersAssignmentRatios : List[Tuple[Soldier, float]] = [(soldier, float('inf')) for soldier in soldiers]
        
    def __bool__(self):
        return len(self.assignments) != 0
    
def generatePermutations(schedule : Schedule, interval : TimeInterval,
                            soldiers : List[Soldier], shifts : List[Shift],
                            maxIterations = 1000):
    
    assert shifts, "Shifts must not be an empty list!"
    assert soldiers, "Soldiers must not be an empty list!"
    
    assignableSoldiers = [soldier for soldier in soldiers if not soldier.properties & SoldierProperty.MANUAL_ASSIGN]
    
    permutations : List[Permutation] = []
    
    pool = Pool()
    results = pool.starmap(generatePermutation, [(schedule, interval, assignableSoldiers, shifts)] * maxIterations)
    permutations = [permutation for permutation in results if permutation is not None]
        
    permutations.sort(key = lambda permutation: (len(permutation.unassignedSoldiers), permutation.restAssignmentRatioStd))
    
    return permutations
    
##============================================================================##
    
def generatePermutation(schedule : Schedule, interval : TimeInterval,
                            soldiers : List[Soldier], shifts : List[Shift]):
    iterTime : datetime = interval.start_time
    success = True
    permutation = Permutation(schedule)  # Creates a copy of `schedule``
    
    # Start permutations...
    while success:
        nextShift, nextShiftTime = permutation.schedule.findNextShift(iterTime, shifts)
        if nextShift is None:
            break
        
        if nextShiftTime >= interval.end_time:
            # No more shifts available within this scope
            break
        
        nextShiftInterval = TimeInterval(nextShiftTime, nextShiftTime + nextShift.duration)
        availableSoldiers = [soldier for soldier in soldiers if soldier.isAvailable(nextShiftInterval, schedule)]
        availableSoldiers = [soldier for soldier in availableSoldiers if soldier.getRestTimestForInterval(nextShiftInterval, schedule)]
        
        # soldiersAndRatios = calculateAndSortRatios(schedule, availableSoldiers, interval)
        position = nextShift.position
        
        mannedSoldiers = manPosition(position, availableSoldiers)
        if mannedSoldiers is None:
            success = False
            break
        
        assignment = Assignment(nextShiftInterval, position, mannedSoldiers)
        permutation.assignments.append(assignment)
        permutation.schedule.add(assignment)
        
        iterTime = nextShiftTime
    
    if success:
        # Calculate standard deviation of rest to assignment ratio of all soldiers
        restAssignmentRatios = [soldier.calculateRestToAssignmentRatio(permutation.schedule, interval) for soldier in soldiers]
        unAssignedSoldierIndexes = [i for i, ratio in enumerate(restAssignmentRatios) if ratio is None]
        permutation.unassignedSoldiers = [soldiers[idx] for idx in unAssignedSoldierIndexes]
        
        restAssignmentRatios = [ratio for ratio in restAssignmentRatios if ratio is not None]
        permutation.restAssignmentRatioStd = \
            stdev(restAssignmentRatios)
            
        return permutation
    
    return None
        
##============================================================================##

def manPosition(position : Position, soldiers : List[Soldier]) -> Union[List[Soldier],None]:
    
    mannedSoldiers : List[Soldier] = []
    platoonBound = False

    # findSoldierWithLowerRatioFunc = lambda soldierAndRatios: next(i for i, soldierAndRatio in enumerate(soldiersAndRatios) if soldierAndRatio[1] != soldiersAndRatios[0][1])
    
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

##============================================================================##

def calculateAndSortRatios(schedule : Schedule, soldiers : List[Soldier], interval : TimeInterval):
    
    soldiersAndRatios = [(soldier, soldier.calculateRestToAssignmentRatio(schedule, interval)) for soldier in soldiers]
    
    # Sort by ratio
    return sorted(soldiersAndRatios, key = lambda x: x[1], reverse = True)  # Highest ratios (most rest) first
