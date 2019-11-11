a = int(input())
inputList = list(map(int, input().split(" ") ))
answerList = [1] * a
for i in range(0, a):
    for j in range(0, i):
        if inputList[j] < inputList[i] and answerList[j] + 1 > answerList[i]:
            answerList[i] = answerList[j] + 1
print(max(answerList))
