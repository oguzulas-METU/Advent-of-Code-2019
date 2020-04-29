def Mass_Calc(Mass):
    Sum = 0 
    while Mass // 3 - 2 > 0:
        Sum += Mass // 3 - 2 
        Mass = Mass // 3 - 2 
    return Sum

Fuel_Matrix = []
Net_Sum = 0
for i in range(100):
    Fuel_Matrix.append(Mass_Calc(int(input())))
    Net_Sum += Fuel_Matrix[i]

print(Net_Sum)