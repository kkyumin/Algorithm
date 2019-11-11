number = int(input())
stair = list()
maxList = [0 for i in range(number)]
for i in range(number):
    stair.append(int(input()))


for i in range(0,number):
    if(i==0):
        maxList[0] = stair[0]
    elif(i==1):
        maxList[1] = stair[0] + stair[1]
    elif(i==2):
        maxList[2] = max(stair[0], stair[1]) + stair[2]
    elif(i>=3):
        maxList[i] = max(maxList[i-3]+stair[i-1]+stair[i], maxList[i-2]+stair[i])
print(maxList[number-1])