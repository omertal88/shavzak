import unittest
from datetime import datetime, time, timedelta
from src.Common import TimeInterval, SoldierProperty, Weekday, Role
from src.Manpower import Soldier
from src.Positions import Position
from src.Shifts import Shift
from src.Absence import Absence
from src.Assignment import Assignment
from src.Schedule import Schedule
from src.Permutation import manPosition

    
soldier1 = Soldier("111", "John Smith", "3", "050-12345678", 0, comment="Good kid...",
                    absences=[Absence(1, datetime(2024, 2, 6), datetime(2024, 2, 8), "Spring break")])
soldier2 = Soldier("112", "Muhammad Chang", "3", "052-12345678", 0, comment="Tries his best...")
soldier3 = Soldier("113", "Rak Lo Bibi", "3", "053-12345678", 0, comment="oh boy...", properties = SoldierProperty.MANUAL_ASSIGN)
soldier4 = Soldier("114", "Rak Lo Bibi2", "2", "053-12345678", 0, comment="oh boy...")
soldier5 = Soldier("115", "Rak Lo Bibi2", "2", "053-12345678", 0, comment="oh boy...")
soldier6 = Soldier("116", "Rak Lo Bibi3", "2", "053-12345678", 0, comment="oh boy...")
soldier7 = Soldier("117", "Yoel HaMelech", "Maflag", "053-00000000", Role.COMPANY_COMMANDER, comment="Go Yoel!")

interval1 = TimeInterval(datetime(2024, 2, 3), datetime(2024, 2, 5)) # Soldier not on break
interval2 = TimeInterval(datetime(2024, 2, 5), datetime(2024, 2, 7)) # Soldier on break
interval3 = TimeInterval(datetime(2024, 2, 3), datetime(2024, 2, 9)) # Soldier on break
interval4 = TimeInterval(datetime(2024, 2, 9), datetime(2024, 2, 11)) # Soldier not on break
interval5 = TimeInterval(datetime(2024, 2, 1, 10, 0, 0), datetime(2024, 2, 1, 18, 0, 0)) # Soldier2 is on shift

position1 = Position(1, "Shin Gimel", 1, 0, 0)
position2 = Position(2, "Officer Position", 1, Role.COMPANY_COMMANDER, 0)
position3 = Position(3, "Homogenous", 3, 0, 0)

shift1 = Shift(1, "Test Shift1", position1,
               Weekday.SUNDAY | Weekday.MONDAY | Weekday.TUESDAY |
               Weekday.WEDNESDAY | Weekday.THURSDAY |
               Weekday.FRIDAY | Weekday.SATURDAY, start_time = time(12, 0), duration = timedelta(hours=2), valid_from = datetime(2024, 2, 1), valid_until = None)
shift2 = shift2 = Shift(2, "Test Shift2", position1,
               Weekday.SUNDAY | Weekday.MONDAY | Weekday.TUESDAY |
               Weekday.WEDNESDAY | Weekday.THURSDAY |
               Weekday.FRIDAY | Weekday.SATURDAY, start_time = time(16, 0), duration = timedelta(hours=2), valid_from = datetime(2024, 2, 1), valid_until = None)
assignment1 = Assignment(TimeInterval(datetime(2024, 2, 1, 12, 0, 0), datetime(2024, 2, 1, 14, 0, 0)), position1, manpower = [soldier2])
assignment2 = Assignment(TimeInterval(datetime(2024,2,25, 8, 0, 0), datetime(2024,2,25, 12, 0, 0)), position1, manpower = [soldier2])
assignment3 = Assignment(TimeInterval(datetime(2024,2,26, 12, 0, 0), datetime(2024,2,26, 16, 0, 0)), position1, manpower = [soldier2])
schedule = Schedule()
schedule.add(assignment1)
schedule.add(assignment2)
schedule.add(assignment3)

class TestSoldierMethods(unittest.TestCase):
    def test_isSoldierAbsent(self):
        self.assertEqual(soldier1.isAbsent(interval1), False)
        self.assertEqual(soldier1.isAbsent(interval2), True)
        self.assertEqual(soldier1.isAbsent(interval3), True)
        self.assertEqual(soldier1.isAbsent(interval4), False)
        
    def test_isSoldierOnShift(self):
        self.assertEqual(soldier1.isOnShift(interval1, schedule), False)
        self.assertEqual(soldier1.isOnShift(interval5, schedule), False)
        self.assertEqual(soldier2.isOnShift(interval5, schedule), True)
        self.assertEqual(soldier2.isOnShift(interval2, schedule), False)
    
    def test_isSoldierAvailable(self):
        self.assertEqual(soldier1.isAvailable(interval1, schedule), True)
        self.assertEqual(soldier1.isAvailable(interval3, schedule), False)
        self.assertEqual(soldier3.isAvailable(interval3, schedule), False)
    
    def test_scheduleFindNextShift(self):
        self.assertEqual(schedule.findNextShift(datetime(2024,2,20, 9, 0, 0), shifts=[shift1, shift2]), (shift1, datetime(2024,2,20, 12, 0)))
        self.assertEqual(schedule.findNextShift(datetime(2024,2,20, 13, 0, 0), shifts=[shift1, shift2]), (shift2, datetime(2024,2,20, 16, 0)))
        self.assertEqual(schedule.findNextShift(datetime(2024,2,19, 19, 0, 0), shifts=[shift1, shift2]), (shift1, datetime(2024,2,20, 12, 0)))
        self.assertEqual(schedule.findNextShift(datetime(2024, 2, 1, 14, 0, 0), shifts=[shift1, shift2]), (shift2, datetime(2024, 2, 1, 16, 0)))
        self.assertNotEqual(schedule.findNextShift(datetime(2024, 2, 26, 10, 0, 0), shifts=[shift1])[1], datetime(2024, 2, 26, 12, 0, 0))
    
    def test_scheduleManPosition(self):
        self.assertNotEqual(manPosition(position2, [soldier1, soldier2, soldier3, soldier4, soldier6, soldier7]), None)
        self.assertEqual(len(set([soldier.platoon for soldier in manPosition(position3, [soldier1, soldier2, soldier3, soldier4, soldier5, soldier6])])), 1)
        self.assertEqual(manPosition(position3, [soldier1, soldier2, soldier4, soldier5]), None) # No way to man that position with these soldiers
    
if __name__ == '__main__':
    unittest.main()
