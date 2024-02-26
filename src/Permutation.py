from copy import copy
from collections import Counter
from itertools import islice, groupby
from statistics import stdev
from random import choice
from copy import deepcopy
from typing import List, Union, Dict, Tuple, Callable
from datetime import datetime, timedelta, date
from multiprocessing.pool import Pool
from src.Common import Role, TimeInterval, SoldierProperty, PositionProperty, hasProperty
from src.Manpower import Soldier, SoldierPositionsMode
from src.Positions import Position
from src.Shifts import Shift
from src.Assignment import Assignment
from src.Schedule import Schedule

NO_ASSIGNMENT_RATIO = 1.0
NOT_AVAILABLE_RATIO = 0.0
LAST_ASSIGNMENTS_HISTORY_HOURS = 48

class PermutationSoldier(object):
    
    def __init__(self, soldier : Soldier, schedule : Schedule):
        
        self.soldier = soldier
        self.assignments : Dict[date, List[Assignment]] = {}

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
        
        if not hasProperty(assignment.position.properties, PositionProperty.RESTING_POSITION):
            # We don't treat resting positions as real assignments.
            self.lastAssignment = assignment
            
        assignment.manpower.append(self.soldier)
    
    def __repr__(self):
        return "%s" % self.soldier.name
    
    ##============================================================================##
    
    def calculateRatioWithinIntervalWithRespectToFutureAssignments(self, interval : TimeInterval, schedule : Schedule):
        
        # First we'll find the last assignment of the soldier.
        for assignment in reversed(schedule.assignments):
            if assignment.interval.start_time < interval.end_time:
                break
            
            if self.soldier in assignment.manpower:
                interval = TimeInterval(interval.start_time, assignment.interval.end_time)
                break
            
        return self.calculateRatioWithinInterval(interval)
    
    ##============================================================================##
    
    def calculateRatioWithinInterval(self, interval : TimeInterval):
        
        interval = copy(interval)
        
        # We want to begin measurement when the first assignment started.
        if self.assignments:
            firstAssignment = self.assignments[sorted(self.assignments.keys())[0]][0]  # Get the first assignment from the first date in the dict.
            if interval.start_time - timedelta(hours = LAST_ASSIGNMENTS_HISTORY_HOURS) < firstAssignment.interval.start_time:
                interval.start_time = firstAssignment.interval.start_time
            
        totalWorkTime = timedelta()
        
        for absence in self.soldier.absences:
            if interval.start_time < absence.interval.end_time:
                interval.start_time = absence.interval.end_time

        if not interval:
            return NO_ASSIGNMENT_RATIO
        
        iterDate = interval.start_time.date()
        while iterDate <= interval.end_time.date():
            
            if iterDate not in self.assignments:
                iterDate += timedelta(days=1)
                continue
            
            for assignment in self.assignments[iterDate]:
                # This entire part needs refactoring!
                if assignment.position.properties & PositionProperty.SPACING_NEEDED:
                    if timedelta() <= interval.end_time - assignment.interval.end_time < assignment.position.required_spacing:
                        # Not assignable in this interval
                        return NOT_AVAILABLE_RATIO
                    
                    # We need to check if we can find an assignment that started after that assignment, but ended beore current time.
                    # That assignment's start time is the correct interval start time (measurement start)
                    nextAssignment = self.findLastAssignmentAfterTime(assignment.interval.end_time)
                    if not nextAssignment:
                        return NO_ASSIGNMENT_RATIO
                    
                    if interval.contains(nextAssignment.interval.start_time):
                        
                        totalWorkTime = timedelta()
                        interval.start_time = nextAssignment.interval.start_time
                            
                if assignment.interval.intersects(interval) and not hasProperty(assignment.position.properties, PositionProperty.RESTING_POSITION):
                    assignmentRelevantInterval = TimeInterval(
                        start_time = assignment.interval.start_time if interval.contains(assignment.interval.start_time) else interval.start_time,
                        end_time = assignment.interval.end_time if interval.contains(assignment.interval.end_time) else interval.end_time
                    )
                    
                    totalWorkTime += assignmentRelevantInterval.duration()
            
            iterDate += timedelta(days=1)
        
        ratio = 1.0 - (totalWorkTime.total_seconds() / interval.duration().total_seconds())
        
        return ratio
    
    ##============================================================================##
    
    def findLastAssignmentAfterTime(self, dateTime : datetime) -> Union[Assignment, None]:
        
        assignmentsDates = sorted(self.assignments.keys())
        
        for iterDate in assignmentsDates:
            for assignment in self.assignments[iterDate]:
                if assignment.interval.start_time > dateTime:
                    return assignment
        
        return None

    ##============================================================================##
    
    def calculateRatioSinceLastAssignment(self, currentTime : datetime):
        
        if not self.lastAssignment:
            return NO_ASSIGNMENT_RATIO
        
        elif self.lastAssignment.interval.start_time == currentTime:
            return NOT_AVAILABLE_RATIO
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
        assignment = Assignment(nextShiftInterval, nextShift.position, nextShift, [])
        
        if assignment.shift.stick_to_position is not None:
            # We need to find an assignment of that position that ends right when this assignment begins.
            
            for iterAssignment in copySchedule.assignments:
                
                if iterAssignment.position == assignment.shift.stick_to_position and iterAssignment.interval.end_time == assignment.interval.start_time:
                    # Found the assignment
                    iterAssignment.bound_assignment = assignment

        copySchedule.add(assignment)
        assignments.append(assignment)
        
        iterTime = nextShiftTime
    
    # Nowe we sort the assignments based on their priorities and their start times
    # The order of the list will force the order of assignments.
    # Notice that the priority key is negative (because higher priority means assigning first)
    sortFunction : Callable[[Assignment], Tuple[int, datetime]] = lambda x: (-x.position.priority, x.interval.start_time)
    assignments.sort(key = sortFunction)
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
        
        if assignment.shift.stick_to_position is not None and assignment.manpower:
            # Already manned this assignment
            continue
        
        assigneeFilterFunction : Callable[[PermutationSoldier, Assignment], List[PermutationSoldier]] = \
            lambda soldier, assignment: soldier.soldier.isAvailable(assignment.interval, schedule) and \
                hasProperty(soldier.soldier.properties, SoldierProperty.NO_PHYSICAL) <= hasProperty(assignment.position.properties, PositionProperty.NOT_PHYSICAL) and \
                isPositionWhitelisted(soldier.soldier, assignment.position)
            
        availableSoldiers = [permutationSoldier for permutationSoldier in permutationSoldiers if assigneeFilterFunction(permutationSoldier, assignment)]
        
        mannedSoldiers = manAssignment(assignment, availableSoldiers, schedule)
        if mannedSoldiers is None:
            success = False
            break
        
        assignment.manpower = mannedSoldiers
        permutation.schedule.add(assignment)
        permutation.assignments.append(assignment)
        
        if assignment.bound_assignment is not None:
            assignment.bound_assignment.manpower.extend(mannedSoldiers.copy())
    
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

def manAssignment(assignment : Assignment, soldiers : List[PermutationSoldier], schedule : Schedule) -> Union[List[Soldier],None]:
    
    print ("Manning assignment \"%s\"" % assignment.position.name)
    mannedSoldiers : List[Soldier] = []
    
    # if assignment.shift.stick_to_position is not None:
    #     # We need to find an assignment of that position that ends right when this assignment begins.
        
    #     for iterAssignment in schedule.assignments:
            
    #         if iterAssignment.position == assignment.shift.stick_to_position and iterAssignment.interval.end_time == assignment.interval.start_time:
                
    #             # Found the assignment
    #             mannedSoldiers.extend(iterAssignment.manpower.copy())
        
    #     if mannedSoldiers:
    #         return mannedSoldiers
        
    position = assignment.position
    
    soldiersGroup = []
    candidates = []
        
    soldiersGroupIter = getNextGroupOfSoldiersByRatio(soldiers, assignment.interval.start_time, schedule)
    
    while position.needed_manpower != len(mannedSoldiers):
        if not len(soldiersGroup):
            # We ran out of soldiers to assign
            try:
                soldiersGroup = next(soldiersGroupIter)
            except StopIteration:
                raise ValueError("Failed to man position %s for interval: %s -> %s" % (position.name, assignment.interval.start_time, assignment.interval.end_time))
        
        randomSoldier = choice(soldiersGroup)
        
        candidates.append(randomSoldier)
        soldiersGroup.remove(randomSoldier)
        
        manpower = getMannableSoldiersFromCandidates(position, candidates)
        
        if not manpower:
            continue
        
        for soldier in manpower:
            soldier.addAssignment(assignment)
            
        mannedSoldiers.extend(manpower)
        
    return [permutationSoldier.soldier for permutationSoldier in mannedSoldiers]
    
    ##============================================================================##
    
def getMannableSoldiersFromCandidates(position : Position, candidates : List[PermutationSoldier]):
    
    if hasProperty(position.properties, PositionProperty.ORGANIC_PLATOONS):
        platoons : Dict[str, List[PermutationSoldier]] = {}
        
        # Split to platoons
        for candidate in candidates:
            platoons.setdefault(candidate.soldier.platoon, []).append(candidate)
        
        for platoon in platoons.values():
            
            manpower = canCandidatesManPosition(position, platoon)
            if manpower:
                return manpower
    
    else:
        manpower = canCandidatesManPosition(position, candidates)
        if manpower:
            return manpower
    
##============================================================================##
    
def canCandidatesManPosition(position : Position, candidates : List[PermutationSoldier]) -> Union[None, List[PermutationSoldier]]:
    
    if len(candidates) < position.needed_manpower:
        return None
    
    candidates = copy(candidates)
    
    mannableCandidates : List[PermutationSoldier] = []
    for role in Role:
        foundRole = False
        if hasProperty(position.needed_roles, role): # This role is needed
            for candidate in candidates:
                if hasProperty(candidate.soldier.roles, role) and candidate not in mannableCandidates:
                    mannableCandidates.append(candidate)
                    candidates.remove(candidate)
                    foundRole = True
                    break
            
            if not foundRole:
                return None

    while position.needed_manpower > len(mannableCandidates):
        if not candidates:
            return None
        
        mannableCandidates.append(candidates.pop(0))
        
    return mannableCandidates
    
    
    # TODO: Currently hard coded commanders.
    
##============================================================================##

def getNextGroupOfSoldiersByRatio(soldiers : List[PermutationSoldier], currentTime : datetime, schedule : Schedule):
    
    # TODO: Improve code readability!!!! This function is written terribly.
    assert len(soldiers)
    
    startMeasureTime = currentTime - timedelta(hours=LAST_ASSIGNMENTS_HISTORY_HOURS)
        
    soldiersAndRatios = [(soldier, soldier.calculateRatioWithinIntervalWithRespectToFutureAssignments(TimeInterval(startMeasureTime, currentTime), schedule)) for soldier in soldiers]
    
    sortedSoldiersAndRatios = sorted(soldiersAndRatios, key = lambda item: item[1], reverse=True)
    
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

##============================================================================##

def isPositionWhitelisted(soldier : Soldier, position : Position):
    
    if soldier.positions_mode == SoldierPositionsMode.ALL:
        return True
    
    if soldier.positions_mode == SoldierPositionsMode.WHITELIST:
        return position in soldier.selected_positions
    
    if soldier.positions_mode == SoldierPositionsMode.BLACKLIST:
        return position not in soldier.selected_positions
