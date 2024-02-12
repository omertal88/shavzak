import xlsxwriter
from collections import namedtuple
from typing import Dict, List
from datetime import date, timedelta, datetime
from src.Common import TimeInterval
from src.Positions import Position
from src.Assignment import Assignment
from src.Schedule import Schedule

Cell = namedtuple("Cell", ["row", "col"])

COLUMN_WIDTH = 25

def exportToXlsx(path : str, schedule : Schedule, interval : TimeInterval):
    
    # Create header
    workbook = xlsxwriter.Workbook(path)
    
    merge_format = workbook.add_format(
        {
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "fg_color": "red",
        }
    )
    
    assignment_time_format = workbook.add_format(
        {
            "align": "center",
            "bold": 1
        }
    )
    positions_format = workbook.add_format(
        {
            "align": "center",
            "underline": 1,
            "bold": 1
        }
    )

    # Prepare assignments per date
    dateToAssignments : Dict[date, List[Assignment]] = {}
    for assignment in schedule.assignments:
        
        assignmentDate = assignment.interval.start_time.date()
        
        dateToAssignments.setdefault(assignmentDate, []).append(assignment)
    
    iterDate = interval.start_time.date()
    while iterDate <= interval.end_time.date():
        currentColumn = 0
        
        worksheet = workbook.add_worksheet(iterDate.strftime("%d-%m-%y"))
        worksheet.right_to_left()

        positionToCell : Dict[str, Cell] = {}
        for assignment in dateToAssignments[iterDate]:
            
            if assignment.position.name not in positionToCell:
                worksheet.write(1, currentColumn, assignment.position.name, positions_format)
                worksheet.set_column(currentColumn, currentColumn, COLUMN_WIDTH)
                positionToCell[assignment.position.name] = Cell(2, currentColumn)
                currentColumn += 1
            
            cell = positionToCell[assignment.position.name]
            worksheet.write(cell.row, cell.col, assignment.interval.start_time.time().strftime("%H:%M"), assignment_time_format)
            
            for i, assignee in enumerate(assignment.manpower, start=1):
                worksheet.write(cell.row + i, cell.col, assignee.name)
            
            positionToCell[assignment.position.name] = Cell(cell.row + i + 2, cell.col)
            
        worksheet.merge_range(0, 0, 0, currentColumn-1, "שיבוץ קרבי ליום %s" % iterDate.strftime("%d/%m/%y"), merge_format)
        
        iterDate += timedelta(days=1)

    workbook.close()

if __name__ == "__main__":
    
    exportToXlsx(None)
    