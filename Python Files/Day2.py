import csv

def IntCodeProgram(Noun, Verb, IntCode):
    OperatingCode = [Member for Member in IntCode]
    OperatingCode[1] = Noun
    OperatingCode[2] = Verb

    Index = 0
    while Index < len(OperatingCode):
        Input_1 = OperatingCode[OperatingCode[Index+1]]
        Input_2 = OperatingCode[OperatingCode[Index+2]]
        if OperatingCode[Index] == 1:
            OperatingCode[OperatingCode[Index+3]] = Input_1 + Input_2
        elif OperatingCode[Index] == 2:
            OperatingCode[OperatingCode[Index+3]] = Input_1 * Input_2
        elif OperatingCode[Index] == 99:
            break;
        Index += 4 
    
    return OperatingCode[0]

File_Dir = input()
with open(File_Dir) as Input:
    Read_Input = csv.reader(Input)
    IntCode = list(Read_Input)[0]
    IntCode = [int(member) for member in IntCode]

for Noun in range(100):
    for Verb in range(100):
        if IntCodeProgram(Noun, Verb, IntCode) == 19690720:
            print("Noun: %d, Verb: %d" %(Noun, Verb))
            print(100 * Noun + Verb)
