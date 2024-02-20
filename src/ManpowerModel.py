from typing import List
from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant
from PyQt5.QtCore import Qt
from src.Manpower import Soldier

class ManpowerModel(QAbstractListModel):
    
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
    
    def data(self, index : QModelIndex, role : Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            soldier = self.soldiers[index.row()]
            return QVariant("%s (%s)" % (soldier.name, soldier.platoon))
        
    def sort(self, column : int, order : Qt.SortOrder):
        sorter = lambda x: "%s%s" % (x.platoon, x.name)
        self.soldiers.sort(key = sorter)
