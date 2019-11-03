numList =list()

for i in range(10):
    flag = 0
    num = int(input())
    namuji = num % 42
    for i in numList:
        if(namuji == i):
            flag = 1
            break

    if(flag == 0):
        numList.append(namuji)



print(len(numList))