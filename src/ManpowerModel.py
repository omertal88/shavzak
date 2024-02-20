from typing import List
from enum import Enum
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtCore import Qt
from src.Manpower import Soldier

class Column:
    NAME       = 0
    PLATOON    = 1
    TELEPHONE  = 2
    COUNT      = 3

class ManpowerModel(QAbstractTableModel):
    
    def __init__(self):
        super().__init__()
        self.soldiers : List[Soldier] = []
        
    def add(self, soldier : Soldier):
        self.beginInsertRows(QModelIndex(), len(self.soldiers), len(self.soldiers))
        self.soldiers.append(soldier)
        self.endInsertRows()
        self.sort(0, Qt.AscendingOrder)
    
    def remove(self, soldier : Soldier):
        self.beginRemoveRows(QModelIndex(), 0, len(self.soldiers))
        result = next(i for i, val in enumerate(self.soldiers) if self.soldiers[i].pn == soldier.pn)
        self.soldiers.pop(result)
        self.endRemoveRows()
        
    def update(self, soldier : Soldier):
        self.soldiers[next(i for i, sol in enumerate(self.soldiers) if sol.pn == soldier.pn)] = soldier

    def rowCount(self, parent : QModelIndex):
        return len(self.soldiers)
    
    def columnCount(self, parent : QModelIndex):
        return Column.COUNT
    
    def data(self, index : QModelIndex, role : Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            soldier = self.soldiers[index.row()]
            if index.column() == Column.NAME:
                return QVariant(soldier.name)
            elif index.column() == Column.PLATOON:
                return QVariant(soldier.platoon)
            elif index.column() == Column.TELEPHONE:
                return QVariant(soldier.telephone)
        
    def sort(self, column : int, order : Qt.SortOrder):
        # if column == Column.PLATOON:
        sorter = lambda x: "%s%s" % (x.platoon, x.name)
        # else:
            # sorter = lambda x: x.name
            
        self.soldiers.sort(key = sorter, reverse = order == Qt.DescendingOrder)

    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if column == Column.NAME:
                    return QVariant("שם")
                elif column == Column.PLATOON:
                    return QVariant("מחלקה")
                elif column == Column.TELEPHONE:
                    return QVariant("טלפון")

    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, len(self.soldiers) - 1)
        self.soldiers.clear()
        self.endRemoveRows()