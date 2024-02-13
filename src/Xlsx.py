import xlsxwriter
from xlsxwriter import format
from random import uniform
from collections import namedtuple
from typing import Dict, List
from datetime import date, timedelta
from src.Common import TimeInterval
from src.Assignment import Assignment
from src.Schedule import Schedule

Cell = namedtuple("Cell", ["row", "col"])

COLUMN_WIDTH = 25

def get_random_color(pastel_factor = 0.7):
    return [(x+pastel_factor)/(1.0+pastel_factor) for x in [uniform(0,1.0) for i in [1,2,3]]]

def color_distance(c1,c2):
    return sum([abs(x[0]-x[1]) for x in zip(c1,c2)])

def generate_new_color(existing_colors,pastel_factor = 0.5):
    max_distance = None
    best_color = None
    for _ in range(0,100):
        color = get_random_color(pastel_factor = pastel_factor)
        if not existing_colors:
            return color
        best_distance = min([color_distance(color,c) for c in existing_colors])
        if not max_distance or best_distance > max_distance:
            max_distance = best_distance
            best_color = color
    return best_color


def exportToXlsx(path : str, schedule : Schedule, interval : TimeInterval):
    
    # Create header
    workbook = xlsxwriter.Workbook(path)
    
    merge_format = workbook.add_format(
        {
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "fg_color": "#ff0000"
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
    
    discoveredColors = []
    positionToAssignmentFormat : Dict[str, format.Format] = {}
    iterDate = interval.start_time.date()
    while iterDate <= interval.end_time.date():
        currentColumn = 0
        
        worksheet = workbook.add_worksheet(iterDate.strftime("%d-%m-%y"))
        worksheet.right_to_left()

        positionToCell : Dict[str, Cell] = {}
        
        for assignment in dateToAssignments.get(iterDate, []):
            
            if assignment.position.name not in positionToAssignmentFormat:
                colorCode = generate_new_color(discoveredColors, pastel_factor=0.5)
                discoveredColors.append(colorCode)
                colorRgb = tuple(list((map(lambda x: int(x*255), colorCode))))
                positionToAssignmentFormat[assignment.position.name] = workbook.add_format(
                    {
                        "fg_color": "#%02x%02x%02x" % colorRgb
                    }
                )

            if assignment.position.name not in positionToCell:
                worksheet.write(1, currentColumn, assignment.position.name, positions_format)
                worksheet.set_column(currentColumn, currentColumn, COLUMN_WIDTH)
                positionToCell[assignment.position.name] = Cell(2, currentColumn)
                currentColumn += 1
            
            cell = positionToCell[assignment.position.name]
            worksheet.write(cell.row, cell.col, assignment.interval.start_time.time().strftime("%H:%M"), assignment_time_format)
            
            assignmentFormat = positionToAssignmentFormat[assignment.position.name]
            for i, assignee in enumerate(assignment.manpower, start=1):
                worksheet.write(cell.row + i, cell.col, assignee.name, assignmentFormat)
            
            positionToCell[assignment.position.name] = Cell(cell.row + i + 2, cell.col)
            
        worksheet.merge_range(0, 0, 0, currentColumn-1, "שיבוץ קרבי ליום %s" % iterDate.strftime("%d/%m/%y"), merge_format)
        
        iterDate += timedelta(days=1)

    workbook.close()

if __name__ == "__main__":
    
    exportToXlsx(None)
    