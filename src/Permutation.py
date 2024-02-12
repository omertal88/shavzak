from copy import copy
from itertools import islice, groupby
from statistics import stdev
from random import choice
from copy import deepcopy
from typing import List, Union, Dict, Tuple, Callable
from datetime import datetime, timedelta, date
from multiprocessing.pool import Pool
from src.Common import Role, TimeInterval, SoldierProperty, PositionProperty
from src.Manpower import Soldier
from src.Positions import Position
from src.Shifts import Shift
from src.Assignment import Assignment
from src.Schedule import Schedule

NO_ASSIGNMENT_RATIO = 1.0
LAST_ASSIGNMENTS_HISTORY_HOURS = 48

class PermutationSoldier(object):
    
    
    def __init__(self, soldier : Soldier, schedule : Schedule):
        
        self.soldier = soldier
        self.assignments : Dict[date, List[Assignment]] = {}
        self.accumalutingAssignmentDuration = timedelta()

        self.lastAssignment : Union[Assignment, None] = None
        self.schedule = schedule
        
        # Create a dictionary of date to assignments to make search easier.
        for assignment in reversed(schedule.assignments):
            if soldier in assignment.manpower:
                if not assignment.interval.start_time in self.assignments:
                    self.assignments[assignment.interval.start_time.date()] = []
                    
                self.assignments[assignment.interval.start_time.date()].append(assignment)

    ##============================================================================##

    def addAssignment(self, assignment : Assignment):
        
        if assignment.interval.start_time.date() not in self.assignments:
            self.assignments[assignment.interval.start_time.date()] = []

        self.assignments[assignment.interval.start_time.date()].append(assignment)
        self.accumalutingAssignmentDuration += assignment.interval.duration()
        
        self.lastAssignment = assignment
        assignment.manpower.append(self.soldier)
    
    def __repr__(self):
        return "%s" % self.soldier.name
    
    ##============================================================================##
    
    def calculateRatioWithinInterval(self, interval : TimeInterval):
        
        totalWorkTime = timedelta()
        
        iterDate = interval.start_time.date()
        while iterDate <= interval.end_time.date():
            
            if iterDate not in self.assignments:
                iterDate += timedelta(days=1)
                continue
            
            for assignment in self.assignments[iterDate]:
                
                if assignment.interval.intersects(interval):
                    assignmentRelevantInterval = TimeInterval(
                        start_time = assignment.interval.start_time if interval.contains(assignment.interval.start_time) else interval.start_time,
                        end_time = assignment.interval.end_time if interval.contains(assignment.interval.end_time) else interval.end_time
                    )
                    
                    totalWorkTime += assignmentRelevantInterval.duration()
            
            iterDate += timedelta(days=1)
        
        ratio = 1.0 - (totalWorkTime.total_seconds() / interval.duration().total_seconds())
        
        return ratio
    
    ##============================================================================##
    
    # def calculateAccumulatedRatio(self, currentTime : datetime):

    #     if self.schedule.assignments and self.schedule.assignments[0].interval.start_time != currentTime:
    #         timeSinceFirstAssignment = currentTime - self.schedule.assignments[0].interval.start_time # Note: This is the first assignment EVER. Not just for this soldier.
    #         absencesDuration = sum([absence.interval.duration() for absence in self.soldier.absences], timedelta())
    #         return 1.0 - (self.accumalutingAssignmentDuration.total_seconds() / (timeSinceFirstAssignment.total_seconds() - absencesDuration.total_seconds()))
        
    #     else:
    #         return 1.0
    
    def calculateRatioSinceLastAssignment(self, currentTime : datetime):
        
        if not self.lastAssignment:
            return 1.0
        
        workTime = self.lastAssignment.interval.duration()
        
        return 1.0 - workTime.total_seconds() / TimeInterval(self.lastAssignment.interval.start_time, currentTime).duration().total_seconds()
        
    ##============================================================================##
    
    def calculateRatioSinceTime(self, interval : TimeInterval):
        # TODO: Finish this..
        try:
            foundAssignmentIdx, foundAssignment = next((i, assignment) for i, assignment in enumerate(self.assignments) if assignment.interval.intersects(interval))
            totalAssignmentsDuration = sum(assignment.interval.duration() for i, assignment in islice(enumerate(self.assignments), foundAssignmentIdx, None) if self.assignments[i].interval.intersects(interval))
            timeSinceAssignmentBegin = interval.end_time - foundAssignment.interval.start_time
            return 
        except StopIteration:
            return NO_ASSIGNMENT_RATIO
        
    # ##============================================================================##
    
    # def assign(self, assignment):
    #     self.assignments.append(assignment)

##============================================================================##

class Permutation(object):
    
    def __init__(self, schedule : Schedule):
        
        self.schedule = deepcopy(schedule)
        self.assignments : List[Assignment] = []
        self.workAssignmentRatioStd : float = 1.0
        self.unassignedSoldiers = List[Soldier]
        
    def __bool__(self):
        return len(self.assignments) != 0
    
##============================================================================##
    
# def generatePermutations(schedule : Schedule, interval : TimeInterval,
#                             soldiers : List[Soldier], shifts : List[Shift],
#                             maxIterations = 1000):
    
#     assert shifts, "Shifts must not be an empty list!"
#     assert soldiers, "Soldiers must not be an empty list!"
    
#     assignableSoldiers = [soldier for soldier in soldiers if not soldier.properties & SoldierProperty.MANUAL_ASSIGN]
    
#     permutations : List[Permutation] = []
    
#     pool = Pool()
#     results = pool.starmap(generatePermutation, [(schedule, interval, assignableSoldiers, shifts)] * maxIterations)
#     permutations = [permutation for permutation in results if permutation is not None]
        
#     permutations.sort(key = lambda permutation: (len(permutation.unassignedSoldiers), permutation.restAssignmentRatioStd))
    
#     return permutations

##============================================================================##

def generatePermutations(schedule : Schedule, interval : TimeInterval,
                            soldiers : List[Soldier], shifts : List[Shift],
                            maxIterations = 1):
    
    assert shifts, "Shifts must not be an empty list!"
    assert soldiers, "Soldiers must not be an empty list!"
    
    permutationSoldiers = [PermutationSoldier(soldier, schedule) for soldier in soldiers if not soldier.properties & SoldierProperty.MANUAL_ASSIGN]
    permutations : List[Permutation] = []
    
    assignments = findAllDesiredAssignmentsWithinInterval(schedule, interval, shifts)
    
    pool = Pool()
    
    # TODO: Check if we actually need ro pass `interval` now that we have `assignments`
    # results = pool.starmap(generatePermutation, [(schedule, interval, permutationSoldiers, assignments)] * maxIterations)
    results = [generatePermutation(schedule, interval, permutationSoldiers, assignments)]
    permutations = [permutation for permutation in results if permutation is not None]
    
    permutations.sort(key = lambda permutation: (len(permutation.unassignedSoldiers), permutation.restAssignmentRatioStd))
    
    return permutations
    
def findAllDesiredAssignmentsWithinInterval(schedule : Schedule, interval : TimeInterval, shifts : List[Shift]):
    assignments = []
    
    copySchedule = deepcopy(schedule)
    # print("All assignments:\n", copySchedule.assignments)
    
    iterTime : datetime = interval.start_time
    while True:
        nextShift, nextShiftTime = copySchedule.findNextShift(iterTime, shifts)

        if nextShift is None or nextShiftTime >= interval.end_time:
            break
        
        nextShiftInterval = TimeInterval(nextShiftTime, nextShiftTime + nextShift.duration)
        assignment = Assignment(nextShiftInterval, nextShift.position, [])
        
        # schedule.assignments.append(assignment)
        copySchedule.add(assignment)
        assignments.append(assignment)
        
        iterTime = nextShiftTime
        
    return assignments

##============================================================================##
    
def generatePermutation(schedule : Schedule, interval : TimeInterval,
                            soldiers : List[PermutationSoldier], assignments : List[Assignment]):

    success = True
    permutation = Permutation(schedule)  # Creates a copy of `schedule``
    permutationSoldiers = copy(soldiers)
    schedule = permutation.schedule # Overwrite input argument `schedule`. We don't ever want to use the original object anymore.

    # Start permutations...
    for assignment in assignments:
        availableSoldiers = [permutationSoldier for permutationSoldier in permutationSoldiers if permutationSoldier.soldier.isAvailable(assignment.interval, schedule)]
        
        # soldiersAndRatios = calculateAndSortRatios(schedule, availableSoldiers, interval)
        mannedSoldiers = manAssignment(assignment, availableSoldiers)
        if mannedSoldiers is None:
            success = False
            break
        
        # print("Manned soldier for assignment %s: %s" % (assignment.position.name, ",".join(["%s" % s.name for s in mannedSoldiers])))
        assignment.manpower = mannedSoldiers
        permutation.schedule.add(assignment)
        permutation.assignments.append(assignment)
    
    print("Done")
    if success:
        # Calculate standard deviation of rest to assignment ratio of all soldiers
        restAssignmentRatios = [soldier.calculateRatioWithinInterval(interval) for soldier in permutationSoldiers]
        unAssignedSoldierIndexes = [i for i, ratio in enumerate(restAssignmentRatios) if ratio is None]
        permutation.unassignedSoldiers = [permutationSoldiers[idx] for idx in unAssignedSoldierIndexes]
        
        restAssignmentRatios = [ratio for ratio in restAssignmentRatios if ratio is not None]
        permutation.restAssignmentRatioStd = stdev(restAssignmentRatios)
            
        return permutation
    
    return None
        
##============================================================================##

def manAssignment(assignment : Assignment, soldiers : List[PermutationSoldier]) -> Union[List[Soldier],None]:
    
    mannedSoldiers : List[Soldier] = []
    platoonBound = False
    position = assignment.position
    
    # if position.needed_roles:
    #     for role in Role:
    #         if not role & position.needed_roles:
    #             continue
            
    #         # This role is needed
    #         relevantSoldiers = [soldier for soldier in soldiers if soldier.roles & role]
            
    #         if not relevantSoldiers:
    #             return None
            
    #         # Randomly pick a soldier
    #         randomSoldier = choice(relevantSoldiers)
    #         mannedSoldiers.append(randomSoldier)
            
    #         if not position.properties & PositionProperty.MIX_PLATOONS and not platoonBound:
    #             platoonBound = True
    #             soldiers = [soldier for soldier in soldiers if soldier.platoon == randomSoldier.platoon]
    #             soldiers.remove(randomSoldier)
    
    soldiersGroup = []
    soldiersGroupIter = getNextGroupOfSoldiersByRatio(soldiers, assignment.interval.start_time)
    
    while position.needed_manpower != len(mannedSoldiers):
        if not len(soldiersGroup):
            # We ran out of soldiers to assign
            try:
                soldiersGroup = next(soldiersGroupIter)
            except StopIteration:
                raise ValueError("Failed to man position %s for interval: %s -> %s" % (position.name, assignment.interval.start_time, assignment.interval.end_time))
        
        randomSoldier = choice(soldiersGroup)
        mannedSoldiers.append(randomSoldier.soldier)
        
        if not position.properties & PositionProperty.MIX_PLATOONS and not platoonBound:
            platoonBound = True
            soldiers = [soldier for soldier in soldiers if soldier.soldier.platoon == randomSoldier.soldier.platoon]

        randomSoldier.addAssignment(assignment)
        soldiersGroup.remove(randomSoldier)
        
    return mannedSoldiers

##============================================================================##

def getNextGroupOfSoldiersByRatio(soldiers : List[PermutationSoldier], currentTime : datetime):
    
    # TODO: Improve code readability!!!! This function is written terribly.
    assert len(soldiers)
    
    soldiersAndRatios = [(soldier, soldier.calculateRatioWithinInterval(TimeInterval(currentTime - timedelta(hours=LAST_ASSIGNMENTS_HISTORY_HOURS), currentTime))) for soldier in soldiers]
    
    sortedSoldiersAndRatios = sorted(soldiersAndRatios, key = lambda item: item[1], reverse=True)
    # print("Interval: %s -> %s" % (currentTime - timedelta(hours=LAST_ASSIGNMENTS_HISTORY_HOURS), currentTime))
    # print(sortedSoldiersAndRatios)
    
    lastSoldierAndRatioIdx = 0
    for soldierAndRatioIdx in range(1, len(sortedSoldiersAndRatios)):
        if sortedSoldiersAndRatios[soldierAndRatioIdx][1] != sortedSoldiersAndRatios[lastSoldierAndRatioIdx][1]:
            
            group = [sortedSoldiersAndRatios[i][0] for i in range(lastSoldierAndRatioIdx, soldierAndRatioIdx)]
            # Now let's create sub groups where each sub group has a unique ratio from last assignment:
            
            subGroups = groupby(group, lambda s: s.calculateRatioSinceLastAssignment(currentTime) if s.lastAssignment is not None else NO_ASSIGNMENT_RATIO)

            tuples : List[Tuple[float, PermutationSoldier]] = []
            for key, group in subGroups:
                tuples.append((key, list(group)))
                
                # yield list(reversed(soldiers))
            
            tuples.sort(key = lambda x: x[0], reverse=True)
            for tup in tuples:
                # print("Yielding group with ratio %.2f with soldiers: %s" % (tup[0], [s.soldier.name for s in tup[1]]))
                yield tup[1]
                
            # yield [sortedSoldiersAndRatios[i][0] for i in range(lastSoldierAndRatioIdx, soldierAndRatioIdx)]
            lastSoldierAndRatioIdx = soldierAndRatioIdx

    group = [sortedSoldiersAndRatios[i][0] for i in range(lastSoldierAndRatioIdx, soldierAndRatioIdx+1)]
    subGroups = groupby(group, lambda s: s.calculateRatioSinceLastAssignment(currentTime) if s.lastAssignment is not None else NO_ASSIGNMENT_RATIO)

    tuples : List[Tuple[float, PermutationSoldier]] = []
    for key, group in subGroups:
        tuples.append((key, list(group)))
        
        # yield list(reversed(soldiers))
    
    tuples.sort(key = lambda x: x[0], reverse=True)
    for tup in tuples:
        # print("Yielding group with ratio %.2f with soldiers: %s" % (tup[0], [s.soldier.name for s in tup[1]]))
        yield tup[1]
    
    
    # print("Ratio = %.2f", sortedSoldiersAndRatios[soldierAndRatioIdx][1])
    
##============================================================================##

def calculateAndSortRatios(schedule : Schedule, soldiers : List[Soldier], interval : TimeInterval):
    
    soldiersAndRatios = [(soldier, soldier.calculateRestToAssignmentRatio(schedule, interval)) for soldier in soldiers]
    
    # Sort by ratio
    return sorted(soldiersAndRatios, key = lambda x: x[1], reverse = True)  # Highest ratios (most rest) first
