import pickle

from dataclasses import dataclass
from typing import List

from src.Manpower import Soldier
from src.Positions import Position
from src.Shifts import Shift
from src.Schedule import Schedule

@dataclass(init = True)
class SerializedData:
    
    soldiers  : List[Soldier]
    positions : List[Position]
    shifts    : List[Shift]
    schedule  : Schedule

    def dump(self, filePath):
        with open(filePath, 'wb') as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    @staticmethod
    def load(filePath):
        with open(filePath, 'rb') as f:
            return pickle.load(f)
