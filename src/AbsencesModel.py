from typing import Callable, List
from datetime import datetime
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from src.Manpower import Absence
from src.Common import DateTimeTools

class Column:
    FROM_TIME   = 0
    UNTIL_TIME  = 1
    COMMENT     = 2
    COUNT       = 3


class AbsencesModel(QAbstractTableModel):
    
    def __init__(self):
        
        super().__init__()
        self.absences : List[Absence] = []
    
    ##============================================================================##
    
    def add(self, absence):
        self.beginInsertRows(QModelIndex(), len(self.absences), len(self.absences))
        self.absences.append(absence)
        self.endInsertRows()
        self.sort(0, Qt.AscendingOrder)
    
    ##============================================================================##
    
    def remove(self, absence : Absence):
        result = next(i for i, abs in enumerate(self.absences) if abs.uid == absence.uid)
        self.removeRows(QModelIndex(), result, result)
    
    ##============================================================================##

    def removeRows(self, parent : QModelIndex, first : int, last : int):
        self.beginRemoveRows(QModelIndex(), first, last)
        
        for i in range(first,last + 1):
            self.absences.pop(i)
            
        self.endRemoveRows()

    ##============================================================================##
    
    def rowCount(self, parent : QModelIndex):
        return len(self.absences)
    
    ##============================================================================##
    
    def columnCount(self, parent : QModelIndex):
        return Column.COUNT
    
    ##============================================================================##
    
    def data(self, index : QModelIndex, role = Qt.DisplayRole):
        if role == Qt.DisplayRole:
            absence : Absence = self.absences[index.row()]
            if index.column() == Column.FROM_TIME:
                return QVariant(DateTimeTools.dateTimeToQDateTime(absence.from_time).toString("dd/MM/yyyy hh:mm"))
            elif index.column() == Column.UNTIL_TIME:
                return QVariant(DateTimeTools.dateTimeToQDateTime(absence.until_time).toString("dd/MM/yyyy hh:mm"))
            elif index.column() == Column.COMMENT:
                return QVariant(absence.comment)
    
    ##============================================================================##
    
    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if column == Column.FROM_TIME:
                    return QVariant("זמן התחלה")
                elif column == Column.UNTIL_TIME:
                    return QVariant("זמן סיום")
                elif column == Column.COMMENT:
                    return QVariant("הערה")
    
    ##============================================================================##
        
    def sort(self, column : int, order : Qt.SortOrder):
        sorter : Callable[[Absence], datetime] = lambda x: x.from_time
        self.absences.sort(key = sorter)