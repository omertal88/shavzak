from typing import List
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtCore import Qt
from src.Positions import Position
from src.PositionsModel import PositionsModel
from src.Shifts import Shift

class ShiftsModel(QAbstractTableModel):
    
    def __init__(self, positionsModel): # TODO: Maybe just pass positions and not the model
        super().__init__()
        
        self.positionsModel : PositionsModel = positionsModel
        self.shifts : List[Shift] = []
    
    ##============================================================================##
    
    def add(self, shift : Shift):
        self.beginInsertRows(QModelIndex(), len(self.shifts), len(self.shifts))
        self.shifts.append(shift)
        self.endInsertRows()
        self.sort(0, Qt.AscendingOrder)
    
    ##============================================================================##
    
    def remove(self, shift : Shift):
        result = next(i for i, sh in enumerate(self.shifts) if sh == shift)
        self.removeRows(QModelIndex(), result, result)
    
    ##============================================================================##
    
    def removeRows(self, parent : QModelIndex, first : int, last : int):
        self.beginRemoveRows(QModelIndex(), first, last)
        
        for i in range(first,last + 1):
            self.shifts.pop(i)
            
        self.endRemoveRows()

    ##============================================================================##
    
    def update(self, shift : Shift):
        
        foundShift = self.shifts[next(i for i, sh in enumerate(self.shifts) if sh == shift)]
        foundShift.update(shift)
    
    ##============================================================================##
    
    def rowCount(self, parent : QModelIndex):
        return len(self.shifts)
    
    ##============================================================================##
    
    def columnCount(self, parent : QModelIndex):
        return 2
    
    ##============================================================================##
    
    def data(self, index : QModelIndex, role : Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return QVariant(self.positionsModel.uidToName(self.shifts[index.row()].position.uid))
            elif index.column() == 1:
                return QVariant(self.shifts[index.row()].nickname)
    
    ##============================================================================##
    
    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if column == 0:
                    return QVariant("עמדה")
                elif column == 1:
                    return QVariant("שם")
    
    ##============================================================================##
    
    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, len(self.shifts) - 1)
        self.shifts.clear()
        self.endRemoveRows()