a= input()


minusList = a.split("-")
plusList = list()
for i in minusList:
    temp = i.split("+")
    temp = list(map(int,temp))
    count = 0
    for i in temp:
        count += int(i)
    plusList.append(count)


count = plusList[0]
for i in range(1,len(plusList)):
    count -= int(plusList[i])
print(count)