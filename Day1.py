def Mass_Calc(Mass):
    Sum = 0 
    while Mass // 3 - 2 > 0:
        Sum += Mass // 3 - 2 
        Mass = Mass // 3 - 2 
    return Sum

Net_Sum = 0
File_Dir = input()
with open(File_Dir) as Input:
    for Row in Input:
        Net_Sum += Mass_Calc(int(Row))

print(Net_Sum)