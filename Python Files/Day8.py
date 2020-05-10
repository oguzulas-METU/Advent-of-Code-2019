import numpy as np
Img_W, Img_L = [25,6]

File_Dir = input()
L_Count = 0
Layers = []
with open(File_Dir) as Input: 
    String = str(next(Input))
    while (L_Count+1)*(Img_W*Img_L) <= len(String):
        Layers.append(String[L_Count*(Img_W*Img_L):(L_Count+1)*(Img_W*Img_L)])
        L_Count += 1

Min_Zeros = Img_W*Img_L + 1
for index, L in enumerate(Layers):
    if Min_Zeros > L.count("0"):
        Min_Zeros = L.count("0")
        min_index = index
    
print(Layers[min_index].count("1")*Layers[min_index].count("2"))

ans = np.zeros((Img_L, Img_W))
for j in range(Img_L):
    for i in range(Img_W):
        for L in Layers:
            if L[Img_W*j+i] == "2":
                continue;
            elif L[Img_W*j+i] == "0":
                break;
            else:
                ans[j,i] = 1
                break;

for Row in ans:
    print(Row)
