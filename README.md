## Shavzak
This tool is used for easily creating work charts for assigning manpower to missions

# To-Do
1. Handle absences when calculating ratios (absence should reset ratio to 1.0).
2. Fix UI bug where an assignment appears twice in the calendar - FIXED
3. Export assignments to Excel Sheet (within some time interval) - DONE
4. Handle special roles.
5. Binding shifts to one-another (Maybe it needs to be binding positions instead of shifts)
6. Fix bug where updating positions doesn't also update the corresponding shifts  - FIXED
7. Export soldiers to CSV (For easily updating roles and stuff) - DONE
8. Allows user to accept / dismiss a permutation.
9. Allows user to auto assign soldiers to a manual assignment.
10. Manual assignments - add ability to split assignment (like with shifts).
11. UI improvement - Checkbox for splitting shift - if not checked - should disable the spinbox.
12. Split shifts - spinbox should be limitted to 24 hours.
13. Implement `Required spacing` for specific positions to ensure some positions get a minimal break regardless of ratios (those positions will have the calculateRatio functions only look back until returning from those positions) - same as with absence.
14. 