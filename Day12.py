import numpy as np
import math

class Star():
    def __init__(self, x,y,z):
        self.coord = [x,y,z]
        self.vel = [0,0,0]
        self.trackVel = np.array([0,0,0])
        self.startPattern = [0,0,0]

    def GRAVITY(self, comp):
        for dim in range(len(self.coord)): 
            if self.coord[dim] < comp.coord[dim]:
                self.vel[dim] += 1
                comp.vel[dim] -= 1
            elif self.coord[dim] > comp.coord[dim]:
                self.vel[dim] -= 1
                comp.vel[dim] += 1
            else:
                continue; 

    def MOVE(self):
        self.trackVel = np.array(np.vstack((self.trackVel, self.vel)))
        for dim in range(len(self.coord)):
            self.coord[dim] += self.vel[dim]

    def ENERGY(self):
        Abs_Pos = [abs(x) for x in self.coord]
        Abs_Vel = [abs(x) for x in self.vel]
        Potential = sum(Abs_Pos)
        Kinetic = sum(Abs_Vel)
        return Potential * Kinetic

    def PATTERN(self, step):
        for dim in range(0,3):
            if self.pattern[dim] == 0:
                pattern_start = self.trackVel[0:10, dim]
                evaluated = list(self.trackVel[step-10:step, dim])
                if evaluated == list(pattern_start):
                    pattern_length = step-10
                    self.pattern[dim] = pattern_length

File_Dir = input()
Star_List = []
with open(File_Dir) as Input:
    for Row in Input:
        Updated_Input = ""
        for Char in Row:
            if Char.isnumeric() or Char == "-" or Char == ",":
                Updated_Input += Char
        a,b,c = Updated_Input.split(",")
        Star_List.append(Star(int(a),int(b),int(c)))

step = 0
expectRepeatList = [0,0,0,0]
while True:
    for Index, Star in enumerate(Star_List):       
        for Compared_Index in range(Index, len(Star_List)):
            Star.GRAVITY(Star_List[Compared_Index])
        Star.MOVE()
        if step > 10 and expectRepeatList[Index] == 0:
            Star.PATTERN(step)
            if 0 not in Star.pattern:
                expectRepeat = Star.pattern[0]
                for pattern in Star.pattern[1:]:
                    expectRepeat = expectRepeat*pattern//math.gcd(expectRepeat,pattern)
                expectRepeatList[Index] = expectRepeat
    if 0 not in expectRepeatList:
        break;
        
    step += 1

ans = 0
for Star in Star_List:
    ans += Star.ENERGY()
print(ans)

ans2 = expectRepeatList[0]
for pattern in expectRepeatList[1:]:
    ans2 = ans2*pattern//math.gcd(ans2,pattern)
print(ans2)
print(step)