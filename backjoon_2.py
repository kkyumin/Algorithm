
fisrt = input()

newList = fisrt.split(" ")
newList = list(map(int,newList))

orm = 0
narim = 0

for i in range(0,8):
    if ((i+1)== newList[i]):
        orm+=1
    elif ( (8-i) == newList[i]):
        narim+=1


if(orm == 8):
    print("ascending")
elif(narim == 8):
    print("descending")
else:
    print("mixed")