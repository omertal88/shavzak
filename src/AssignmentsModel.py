from typing import List
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant, QModelIndex
from src.Positions import Position
from src.Assignment import Assignment

class Column:
    START_TIME = 0
    END_TIME   = 1
    POSITION   = 2
    COUNT      = 3
    
class AssignmentsModel(QAbstractTableModel):
    
    def __init__(self):
        super().__init__()

        self.assignments : List[Assignment] = []
    
    ##============================================================================##
    
    def add(self, assignment : Assignment):
        self.beginInsertRows(QModelIndex(), len(self.assignments), len(self.assignments))
        self.assignments.append(assignment)
        self.endInsertRows()
        self.sort(Column.START_TIME, Qt.AscendingOrder)
    
    ##============================================================================##
    
    def removeRows(self, parent : QModelIndex, first : int, last : int):
        self.beginRemoveRows(QModelIndex(), first, last)
        
        for i in range(first,last + 1):
            self.assignments.pop(i)
            
        self.endRemoveRows()
    
    ##============================================================================##
    
    def rowCount(self, parent : QModelIndex):
        return len(self.assignments)
    
    ##============================================================================##
    
    def columnCount(self, parent : QModelIndex):
        return 3
    
    ##============================================================================##
    
    def data(self, index : QModelIndex, role : Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            if index.column() == Column.POSITION:
                return QVariant(self.assignments[index.row()].position.name)
            elif index.column() == Column.START_TIME:
                return QVariant(self.assignments[index.row()].interval.start_time.strftime("%d/%m/%y %H:%M"))
            elif index.column() == Column.END_TIME:
                return QVariant(self.assignments[index.row()].interval.end_time.strftime("%d/%m/%y %H:%M"))
    
    ##============================================================================##
    
    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if column == Column.POSITION:
                    return QVariant("עמדה")
                elif column == Column.START_TIME:
                    return QVariant("זמן התחלה")
                elif column == Column.END_TIME:
                    return QVariant("זמן סיום")
    
    ##============================================================================##
    
    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, len(self.assignments) - 1)
        self.assignments.clear()
        self.endRemoveRows()
