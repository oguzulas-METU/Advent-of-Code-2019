Input = "147981-691423"
Input = Input.split("-")

def INCREASING(Int):
    Str = str(Int)
    for Index in range(len(Str)-1):
        if int(Str[Index]) > int(Str[Index+1]):
            return False
    return True

def DOUBLES(Int):
    Str = str(Int)
    for Index in range(len(Str)-1):
        if Index < len(Str) - 2 and Str[Index] == Str[Index+1] and Str[Index+1] == Str[Index+2]:
            continue;
        elif Index > 0 and Str[Index] == Str[Index+1] and Str[Index] == Str[Index-1]:
            continue;
        elif Str[Index] == Str[Index+1]:
            return True
    return False 

Count = 0
for integer in range(int(Input[0]), int(Input[1])):
    if INCREASING(integer) and DOUBLES(integer):
        Count = Count + 1

print(Count)
