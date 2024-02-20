from typing import List
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtCore import Qt
from src.Positions import Position

class PositionsModel(QAbstractTableModel):
    
    def __init__(self):
        super().__init__()
        self.setHeaderData(0, Qt.Horizontal, QVariant("שם"), role = Qt.UserRole)
        self.setHeaderData(1, Qt.Horizontal, QVariant("סד\"כ"), role = Qt.UserRole)
        self.positions : List[Position] = []
        
    def add(self, position : Position):
        self.beginInsertRows(QModelIndex(), len(self.positions), len(self.positions))
        self.positions.append(position)
        self.endInsertRows()
        self.sort(0, Qt.AscendingOrder)
    
    def remove(self, position : Position):
        self.beginRemoveRows(QModelIndex(), 0, len(self.positions) - 1)
        result = next(i for i, pos in enumerate(self.positions) if self.positions[i].uid == position.uid)
        self.positions.pop(result)
        self.endRemoveRows()

    def update(self, position : Position):
        self.positions[next(i for i, pos in enumerate(self.positions) if pos.uid == position.uid)] = position
        
    def rowCount(self, parent : QModelIndex):
        return len(self.positions)
    
    def columnCount(self, parent : QModelIndex):
        return 3

    def data(self, index : QModelIndex, role : Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return QVariant(self.positions[index.row()].name)
            elif index.column() == 1:
                return QVariant(self.positions[index.row()].uid)
            elif index.column() == 2:
                return QVariant(self.positions[index.row()].needed_manpower)

    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if column == 0:
                    return QVariant("שם")
                elif column == 1:
                    return QVariant("מס\"ד")
                elif column == 2:
                    return QVariant("סד\"כ")
