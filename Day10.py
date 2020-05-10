import math

File_Dir = input()
Asteroid_List = []
with open(File_Dir) as Input:
    [j,i] = [0,0]
    for Row in Input:
        i = 0
        for Char in Row:
            if Char == "#":
                Asteroid_List.append([j,i])
            i += 1
        j += 1

Ans1 = 0
Opt_Asteroid = []
for Monitor_Loc in Asteroid_List:
    Angle = set()
    for Observed_Loc in Asteroid_List:
        if Monitor_Loc == Observed_Loc:
            continue; 
        else:
            Rise = Observed_Loc[0] - Monitor_Loc[0]
            Run = Observed_Loc[1] - Monitor_Loc[1]
            Angle.add(math.atan2(Rise,Run))
    if len(Angle) > Ans1:
        Opt_Asteroid = Monitor_Loc
        Ans1 = len(Angle)
print(Ans1) 

Relative_Coordinates = {}
for Index, Asteroid in enumerate(Asteroid_List):
    if Asteroid != Opt_Asteroid:
        Rise = Asteroid[0] - Opt_Asteroid[0]
        Run = Asteroid[1] - Opt_Asteroid[1]
        Distance = (Rise**2+Run**2)**0.5
        Angle = math.atan2(Rise,Run)
        if Angle not in Relative_Coordinates.keys():
            Relative_Coordinates[Angle] = [[Distance, Index]]
        else:
            Relative_Coordinates[Angle].append([Distance, Index])
            
Pop_Count = 0
Popped_Ast = []
Ray_Direction = -1/2 * math.pi 

if Ray_Direction in Relative_Coordinates.keys():
    Min_Dist = math.inf
    for Index, Item in enumerate(Relative_Coordinates[Ray_Direction]):
        if Item[0] < Min_Dist:
            Min_Index = Index
            Min_Dist = Item[0]
    Popped_Ast.append(Relative_Coordinates[Ray_Direction].pop(Min_Index))
    Pop_Count += 1

while Pop_Count < len(Asteroid_List)-1:
    Max_Angle = 2 * math.pi
    for angle in Relative_Coordinates.keys():
        if angle < Max_Angle and angle > Ray_Direction:
            Max_Angle = angle
    if Max_Angle == 2 * math.pi:
        for angle in Relative_Coordinates.keys():
            if angle < Max_Angle and angle > Ray_Direction - 2*math.pi:
                Max_Angle = angle
    Min_Dist = math.inf
    if Relative_Coordinates[Max_Angle] != []:
        for Index, Item in enumerate(Relative_Coordinates[Max_Angle]):
            if Item[0] < Min_Dist:
                Min_Index = Index
                Min_Dist = Item[0]
        Popped_Ast.append(Relative_Coordinates[Max_Angle].pop(Min_Index))
        Pop_Count += 1
    Ray_Direction = Max_Angle
    
Ans2 = [Asteroid_List[member[1]] for member in Popped_Ast]
print(Ans2[199])