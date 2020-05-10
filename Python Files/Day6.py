Orbit_Map = {}

File_Dir = input()
with open(File_Dir) as Input:
    for Row in Input: 
        Large_Star, Small_Star = Row[:-1].split(")")
        Orbit_Map[Small_Star] = Large_Star

Sum = 0
for Key in Orbit_Map.keys(): 
    Recursion_Key = Key
    while Recursion_Key in Orbit_Map.keys():
        Sum += 1
        Recursion_Key = Orbit_Map[Recursion_Key]
print(Sum)

Ans = set()
for Key in ["SAN", "YOU"]:
    Recursion_Key = Key
    while Recursion_Key in Orbit_Map.keys():
        if Orbit_Map[Recursion_Key] in Ans:
            Ans.remove(Orbit_Map[Recursion_Key])
        else:
            Ans.add(Orbit_Map[Recursion_Key])
        Recursion_Key = Orbit_Map[Recursion_Key]
print(len(Ans))
