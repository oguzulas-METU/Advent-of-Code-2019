import numpy as np 
import csv

def ORIGIN(Input_Grid):
    Width = np.size(Input_Grid, 0)
    Height = np.size(Input_Grid, 1)
    return [Width // 2, Height // 2]

def MOVE_FUNCTION(Input_Grid, Command_List, Wire_Name, Intersection_List):
    Origin = ORIGIN(Input_Grid)
    Dir_Dict = {"U":[0,-1], "D":[0,1], "R":[1,1], "L":[1,-1]}
    New_Origin = [0,0]
    Total_Step = 1

    for Cmd in Command_List:
        Dir = Cmd[0]
        Step_Size = int(Cmd[1:])
        Varying_Axis = Dir_Dict[Dir][0]
        Path_Sign = Dir_Dict[Dir][1]

        New_Origin[1-Varying_Axis] = Origin[1-Varying_Axis]    
        New_Origin[Varying_Axis] = Origin[Varying_Axis] + Path_Sign*Step_Size        
        
        min_lim = min(Origin[Varying_Axis]+Path_Sign, New_Origin[Varying_Axis]+Path_Sign)
        max_lim = max(Origin[Dir_Dict[Dir][0]]+Path_Sign, New_Origin[Dir_Dict[Dir][0]]+Path_Sign)
        
        Counter = 0
        for axis in range(min_lim,max_lim):
            if Varying_Axis == 0:
                if Input_Grid[axis, New_Origin[1]] != "" and Wire_Name not in Input_Grid[axis, New_Origin[1]]:
                    if Path_Sign == 1:
                        Intersection_List.append([axis, New_Origin[1], Total_Step + Counter])
                    else:
                        Intersection_List.append([axis, New_Origin[1], Total_Step + Step_Size - Counter])
                Input_Grid[axis, New_Origin[1]] += Wire_Name
            else:
                if Input_Grid[New_Origin[0], axis] != "" and Wire_Name not in Input_Grid[New_Origin[0], axis]:
                    if Path_Sign == 1:
                        Intersection_List.append([New_Origin[0], axis, Total_Step + Counter])
                    else:
                        Intersection_List.append([New_Origin[0], axis, Total_Step + Step_Size - Counter])
                Input_Grid[New_Origin[0], axis] += Wire_Name   
            Counter += 1       
        Origin = [Item for Item in New_Origin]
        Total_Step += Counter

Grid_Width = 15000
Grid_Height = 15000

Commands = []

File_Dir = input()
with open(File_Dir) as Input:
    Reader = csv.reader(Input)
    for Row in Reader:
        Commands.append(Row)

Grid = np.empty([Grid_Width,Grid_Height], dtype="<U5")
Grid_Origin = ORIGIN(Grid)
Intersects_1 = []
for Index, Row in enumerate(Commands):        
    MOVE_FUNCTION(Grid, Row, str(Index), Intersects_1)

Grid = np.empty([Grid_Width,Grid_Height], dtype="<U5")
Grid_Origin = ORIGIN(Grid)
Intersects_2 = []
for Index, Row in enumerate(reversed(Commands)):
    MOVE_FUNCTION(Grid, Row, str(Index), Intersects_2)

Net_Results = []
for Outer_Item in Intersects_1:
    for Inner_Item in Intersects_2:
        if Inner_Item[0] == Outer_Item[0] and Inner_Item[1] == Outer_Item[1]:
            Net_Results.append([Inner_Item[0], Inner_Item[1], Inner_Item[2]+Outer_Item[2]])

Min_Steps = 100000
Min_Dist = 100000
for Item in Net_Results:
    Manh_Dist = abs(Item[0] - Grid_Origin[0]) + abs(Item[1] - Grid_Origin[0])
    Min_Steps = Item[2] if Item[2] < Min_Steps else Min_Steps
    Min_Dist = Manh_Dist if Manh_Dist < Min_Dist else Min_Dist

print(Min_Dist)
print(Min_Steps)
