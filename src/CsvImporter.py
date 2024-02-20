from typing import List
from src.Manpower import Soldier

def importFromCsv(path) -> List[Soldier]:
    
    soldiers = []
    firstLine = True
    with open(path) as csv:
        for line in csv:
            if firstLine:
                # Ignore csv's first line
                firstLine = False
                continue
            pn, name, platoon, telephone, comment = line.split(',')
            soldier = Soldier.makeFromCsv(pn, name, platoon, telephone, comment)
            soldiers.append(soldier)
    
    return soldiers