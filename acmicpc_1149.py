a = input()
a = int(a)

inputList = list()
minList = list()
for i in range(a):
    tempWord = input()
    tempList = tempWord.split(" ")
    tempList = list(map(int,tempList))
    inputList.append(tempList)

minList.append(inputList[0])

for i in range(1,a):
    minList.append([0,0,0])
    minList[i][0] = min(minList[i-1][1],minList[i-1][2]) + inputList[i][0]
    minList[i][1] = min(minList[i-1][0],minList[i-1][2]) + inputList[i][1]
    minList[i][2] = min(minList[i-1][0],minList[i-1][1]) + inputList[i][2]

print(min(minList[i][0],minList[i][1],minList[i][2]))