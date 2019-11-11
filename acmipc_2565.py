a = int(input())
b = list()
for i in range(a):
    temp = input().split(" ")
    temp = list(map(int,temp))
    b.append(temp)

b = sorted(b, key=lambda b:b[0])
answerList = [1] * a
for i in range(0, a):
    for j in range(0, i):
        if b[j][1] < b[i][1] and answerList[j] + 1 > answerList[i]:
            answerList[i] = answerList[j] + 1

print(a-max(answerList))

2
5
1
3  2
6
8
4
2