import csv

class IntCodeObject():
    def __init__(self, IntCodeArg):
        self.intCode = IntCodeArg + [0 for i in range(10000)]
        self.EXECUTE()
            
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
        print(arg[0])

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
    
    def EXECUTE(self):
        index = 0
        base = 0
        while index < len(self.intCode):
            opcode = str(self.intCode[index])[-2:]
            pmode = str(self.intCode[index])[::-1][2:]
            opcode = self.EXTEND_STR(opcode[::-1], 2)[::-1]

            if opcode == "99":
                print("Program has halted!")
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
                self.intCode[write_loc] = int(input("Please provide input!"))
                index += 2
            elif opcode == "04":
                self.PRINT_MODULE(index, pmode, base)  
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
    Run_Code = IntCodeObject(IntCode)
    
