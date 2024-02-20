from typing import List
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtCore import Qt
from src.Positions import Position
from src.PositionsModel import PositionsModel
from src.Shifts import Shift

class ShiftsModel(QAbstractTableModel):
    
    def __init__(self, positionsModel):
        super().__init__()
        
        self.positionsModel : PositionsModel = positionsModel
        
        self.setHeaderData(0, Qt.Horizontal, QVariant("עמדה"), role = Qt.UserRole)
        self.setHeaderData(1, Qt.Horizontal, QVariant("שם"), role = Qt.UserRole)
        self.setHeaderData(2, Qt.Horizontal, QVariant("מס\"ד"), role = Qt.UserRole)
        self.shifts : List[Shift] = []
        
    def add(self, shift : Shift):
        self.beginInsertRows(QModelIndex(), len(self.shifts), len(self.shifts))
        self.shifts.append(shift)
        self.endInsertRows()
        self.sort(0, Qt.AscendingOrder)
    
    def remove(self, shift : Shift):
        self.beginRemoveRows(QModelIndex(), 0, len(self.shifts) - 1)
        result = next(i for i, sh in enumerate(self.shifts) if sh.uid == shift.uid)
        self.shifts.pop(result)
        self.endRemoveRows()

    def update(self, shift : Shift):
        self.shifts[next(i for i, sh in enumerate(self.shifts) if sh.uid == shift.uid)] = shift
        
    def rowCount(self, parent : QModelIndex):
        return len(self.shifts)
    
    def columnCount(self, parent : QModelIndex):
        return 3

    def data(self, index : QModelIndex, role : Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return QVariant(self.positionsModel.uidToName(self.shifts[index.row()].position_uid))
            elif index.column() == 1:
                return QVariant(self.shifts[index.row()].nickname)
            elif index.column() == 2:
                return QVariant(self.shifts[index.row()].uid)

    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if column == 0:
                    return QVariant("עמדה")
                elif column == 1:
                    return QVariant("שם")
                elif column == 2:
                    return QVariant("מס\"ד")

    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, len(self.shifts))
        self.shifts.clear()
        self.endRemoveRows()