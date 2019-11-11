

# a = int(input())
#
# inputList = list([["1","2","3","4","5","6","7","8","9"]])
#
#
# for j in range(0,a):
#     tmpList = list()
#     for i in inputList[j]:
#         if (int(i[-1])-1 > -1):
#             tmpList.append(i + str(int(i[-1])-1))
#         if (int(i[-1])+1 < 10):
#             tmpList.append(i + str(int(i[-1])+1 ))
#     inputList.append(tmpList)
#
# print(len(inputList[a-1]))

intList = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 101):
    for j in range(10):
        if i == 1:
            intList[i][j] = 1
        else:
            if 1 <= j <= 8:
                intList[i][j] = intList[i - 1][j - 1] + intList[i - 1][j + 1]
            elif j == 0:
                intList[i][j] = intList[i - 1][j + 1]
            elif j == 9:
                intList[i][j] = intList[i - 1][j - 11]

inputNum = int(input())
print(sum(intList[inputNum][1:10]) % 1000000000)