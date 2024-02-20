from typing import List
from dataclasses import dataclass
from datetime import datetime, timedelta

# from src.Manpower import Soldier

@dataclass(init = True)
class Assignment:
    # uid        : int
    start_time : datetime
    end_time   : datetime
    position   : int
    shift      : int
    manpower   : List[int] # Soldiers' PN
