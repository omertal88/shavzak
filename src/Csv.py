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
            pn, name, platoon, roles, telephone, properties, comment = line.split(',')
            soldier = Soldier.makeFromCsv(pn, name, platoon, int(roles), telephone, int(properties), comment)
            soldiers.append(soldier)
    
    return soldiers

##============================================================================##

def exportToCsv(path : str, soldiers : List[Soldier]):
    
    with open(path, 'w') as csv:
        csv.write("pn,name,platoon,roles,telephone,properties,comment\n")
        for soldier in soldiers:
            csv.writelines("%s,%s,%s,%d,%s,%d,%s\n" % (soldier.pn, soldier.name, soldier.platoon, soldier.roles, soldier.telephone, soldier.properties, soldier.comment.strip()))
