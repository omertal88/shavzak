# Shavzak
## Introduction
This tool is used for easily creating work charts for assigning manpower to missions. Written specifically for the IDF. Am Israel Chai!
Author: Omer Tal (jaclawi@gmail.com).

Please feel free to suggest features and bug fixes through pull requests.

## Open Issues
Exported Xlsx sheets don't contain the assignments that started at some previous day, but still active in the current day.

## To-Do
4. Handle special roles.
8. Allows user to accept / dismiss a permutation.
9. Allows user to auto assign soldiers to a manual assignment.
10. Manual assignments - add ability to split assignment (like with shifts).
11. UI improvement - Checkbox for splitting shift - if not checked - should disable the spinbox.
12. Split shifts - spinbox should be limitted to 24 hours.
14. Don't allow soldiers to begin a new assignment if they just finished one (unless it's a `no rest needed` one) (Not sure about that one)
15. Some UI validations. For example: Gray-out the `run` button if no Soldiers, positions or shifts are present.
16. Easy removal of assignments in calendar.
17. Adding auto assignment to resting position based on different logic (hardest worker gets that assignment? or maybe random?)

## Done
1. Handle absences when calculating ratios (absence should reset ratio to 1.0). 
2. Fix UI bug where an assignment appears twice in the calendar - FIXED
3. Export assignments to Excel Sheet (within some time interval) - DONE
5. Binding positions to one-another. Shifts are still needed to be defined in order for the binding to occur.
6. Fix bug where updating positions doesn't also update the corresponding shifts  - FIXED
7. Export soldiers to CSV (For easily updating roles and stuff) - DONE
13. Implement `Required spacing` for specific positions to ensure some positions get a minimal break regardless of ratios (those positions will have the calculateRatio functions only look back until returning from those positions) - same as with absence. - DONE
16. When assigning a soldier - we should also take in consideration the future assignments (those assigned manually for example) - DONE


# Apendix
## Assignment Algorithm
This is still a work in progress.

The way it is implemented is this:

1. We start by finding all the assignments within the wanted time interval.
2. We sort those by their starting time.
3. We calculate the rest ratio (ratio between rest time and overall time) in the last 48 hours of each soldier.
4. Then we sort all the soldiers by that ratio. We split those to groups with equal ratios. The group with the highest ratio is first assigned.
5. For each group, we calculate for each soldier the ratio from the begining of the last assignment and sort them again using this ratio.
6. We assign the soldier with the highest ratios within its group.

Basically the idea is that the soldier that rested the most should be assigned to the next task.

This isn't always perfect and doesn't necessary produce the best result.
It may also create cases where a soldier is assigned twice in a row (because his ratio from the last 48 hours is low).

## Another approach
For each soldier we can calculate the amount of hours it needs to be assigned in order to reach the desired average (overall assignment hours, divided by the total hours times the soldier count).

The order of assignment is then simply the difference between the amount of hours needed, and the assignment duration.