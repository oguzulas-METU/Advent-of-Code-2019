import csv
import numpy as np

class IntCodeObject():
    def __init__(self, IntCodeArg):
        self.intCode = IntCodeArg + [0 for i in range(10000)]
        self.direction = {"+i": [0,1], "-i": [0,-1], "+j": [1,0], "-j": [-1,0]}
        self.position = [0,0]
            
    def CALC_MODULE(self, index, opcode, pmode, base):
        pmode = self.EXTEND_STR(pmode, 2)
        args = self.GET_ARGS(index, 2, pmode, base)

        if opcode == "01":
            return args[0]+args[1]
        else:
            return args[0]*args[1]
       
    def PRINT_MODULE(self, index, pmode, base):
        pmode = self.EXTEND_STR(pmode, 1)
        arg = self.GET_ARGS(index, 1, pmode, base)
        return arg[0]

    def JUMP_MODULE(self, index, opcode, pmode, base):
        pmode = self.EXTEND_STR(pmode, 2)
        args = self.GET_ARGS(index, 2, pmode, base)
        
        if (opcode == "05" and args[0] != 0) or (opcode == "06" and args[0] == 0):
            return args[1]
        else:
            return index + 3
        
    def LOGIC_MODULE(self, index, opcode, pmode, base):
        pmode = self.EXTEND_STR(pmode, 2)
        args = self.GET_ARGS(index, 2, pmode, base)   
        
        if (opcode == "07" and args[0] < args[1]) or (opcode == "08" and args[0] == args[1]):
            return 1
        else:
            return 0

    def GET_ARGS(self, index, n, pmode, base):
        args = []
        for arg, mode in zip([i for i in range(1,n+1)], pmode):
            if mode == "0":
                loc = self.intCode[index+arg]
            elif mode == "1":
                loc = arg + index
            else:
                loc = base + self.intCode[index+arg]
            args.append(self.intCode[loc])
        return args            

    @staticmethod
    def EXTEND_STR(String, Length):
        while len(String) < Length:
            String = String + "0"
        return String
    
    def EXECUTE(self, Grid, Start):
        index, base = [0,0]
        input_set = set()
        output_counter = 0
        direct = "+j"
        while index < len(self.intCode):
            opcode = str(self.intCode[index])[-2:]
            pmode = str(self.intCode[index])[::-1][2:]
            opcode = self.EXTEND_STR(opcode[::-1], 2)[::-1]
            grid_input = Grid[self.position[0]+ Start[0], self.position[1]+ Start[1]]

            if opcode == "99":
                print("Program has halted!")
                return(len(input_set))
                break;
            elif opcode == "01" or opcode == "02":
                if len(pmode) == 3 and pmode[-1] == "2":
                    write_loc = base + self.intCode[index+3] 
                else: 
                    write_loc = self.intCode[index+3]
                self.intCode[write_loc] = self.CALC_MODULE(index, opcode, pmode, base)
                index += 4
            elif opcode == "03":
                if len(pmode) == 1 and pmode[-1] == "2":
                    write_loc = base + self.intCode[index+1] 
                else: 
                    write_loc = self.intCode[index+1]
                self.intCode[write_loc] = int(grid_input)
                input_set.add((self.position[0], self.position[1]))
                index += 2
            elif opcode == "04":
                output_counter += 1
                output = self.PRINT_MODULE(index, pmode, base)  
                if output_counter % 2 == 1:
                   Grid[self.position[0]+ Start[0], self.position[1]+ Start[1]] = output
                else:
                    if output == 0:
                        Turn_Left = {"+i": "+j", "-i": "-j", "+j": "-i", "-j": "+i"} 
                        direct = Turn_Left[direct]
                    else:
                        Turn_Right = {"+i": "-j", "-i": "+j", "+j": "+i", "-j": "-i"} 
                        direct = Turn_Right[direct]
                    self.position = [self.position[0] + self.direction[direct][0],
                                 self.position[1] + self.direction[direct][1]]
                index += 2
            elif opcode == "05" or opcode == "06":
                index = self.JUMP_MODULE(index, opcode, pmode, base)
            elif opcode == "07" or opcode == "08":
                if len(pmode) == 3 and pmode[-1] == "2":
                    write_loc = base + self.intCode[index+3] 
                else: 
                    write_loc = self.intCode[index+3]
                self.intCode[write_loc] = self.LOGIC_MODULE(index, opcode, pmode, base)
                index += 4
            elif opcode == "09":
                pmode = self.EXTEND_STR(pmode, 1)
                shift = self.GET_ARGS(index, 1, pmode, base) 
                base += shift[0]
                index += 2

File_Dir = input()
with open(File_Dir) as Input:
    Read_Input = csv.reader(Input)
    IntCode = list(Read_Input)[0]
    IntCode = [int(member) for member in IntCode]

Grid_L, Grid_W = [101, 101]
Grid = np.zeros((Grid_L,Grid_W))
Start = [Grid_L//2, Grid_W//2]
Grid[Start] = 1

Run_Code = IntCodeObject(IntCode)
Covered_Area = Run_Code.EXECUTE(Grid, Start)
print(Covered_Area)

with open("Results.txt", "w") as Result:
    Index = len(Grid)
    while Index:
        Index -=1
        if 1.0 in Grid[Index]:
            for Val in Grid[Index]:
                if Val == 1.0:
                    Result.write("#")
                else:
                    Result.write(" ")
            Result.write("\n")
            
    
