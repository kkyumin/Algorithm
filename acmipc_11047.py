splitList = list(map(int, input().split(" ") ))
a = splitList[0]
number = splitList[1]
inputList = list()
for i in range(a):
    inputList.append(int(input()))

countList = list()
nam = number

for i in range(a-1,-1,-1):
    count = nam // inputList[i]
    if(count!=0):
        nam = nam % inputList[i]
        countList.append(count)


print(sum(countList))

