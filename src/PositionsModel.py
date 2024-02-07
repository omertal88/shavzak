from typing import List
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtCore import Qt
from src.Positions import Position

class Column:
    NAME     = 0
    UID      = 1
    MANPOWER = 2
    COUNT    = 3
class PositionsModel(QAbstractTableModel):
    
    def __init__(self):
        super().__init__()
        self.positions : List[Position] = []
    
    ##============================================================================##
    
    def add(self, position : Position):
        self.beginInsertRows(QModelIndex(), len(self.positions), len(self.positions))
        self.positions.append(position)
        self.endInsertRows()
        self.sort(Column.NAME, Qt.AscendingOrder)
    
    ##============================================================================##
    
    def remove(self, position : Position):
        result = next(i for i, pos in enumerate(self.positions) if pos is position)
        self.removeRows(QModelIndex(), result, result)
    
    ##============================================================================##
    
    def removeRows(self, parent : QModelIndex, first : int, last : int):
        self.beginRemoveRows(QModelIndex(), first, last)
        
        for i in range(first,last + 1):
            self.positions.pop(i)
            
        self.endRemoveRows()
    
    ##============================================================================##
    
    def update(self, position : Position):
        self.positions[next(i for i, pos in enumerate(self.positions) if pos == position)] = position
    
    ##============================================================================##
    
    def rowCount(self, parent : QModelIndex):
        return len(self.positions)
    
    ##============================================================================##
    
    def columnCount(self, parent : QModelIndex):
        return Column.COUNT
    
    ##============================================================================##
    
    def uidToName(self, uid : int):
        return next(pos.name for pos in self.positions if pos.uid == uid)
    
    ##============================================================================##
    
    def data(self, index : QModelIndex, role : Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            if index.column() == Column.NAME:
                return QVariant(self.positions[index.row()].name)
            elif index.column() == Column.UID:
                return QVariant(self.positions[index.row()].uid)
            elif index.column() == Column.MANPOWER:
                return QVariant(self.positions[index.row()].needed_manpower)
    
    ##============================================================================##
    
    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if column == Column.NAME:
                    return QVariant("שם")
                elif column == Column.UID:
                    return QVariant("מס\"ד")
                elif column == Column.MANPOWER:
                    return QVariant("סד\"כ")
    
    ##============================================================================##
    
    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, len(self.positions) - 1)
        self.positions.clear()
        self.endRemoveRows()