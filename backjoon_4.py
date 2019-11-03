number = int(input())

for i in range(number):
    word = input()


    countList = list()
    count = 0
    for i in word:
        if("O" == i):
            count += 1
            countList.append(count)
            continue
        elif("X" == i):
            count=0

    score = 0

    for i in countList:
        score += i

    print(score)