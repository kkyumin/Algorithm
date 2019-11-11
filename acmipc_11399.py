a = int(input())
splitList = list(map(int, input().split(" ") ))

splitList.sort()
count = 0
for i in range(0,a+1,1):
    for j in range(0,i,1):
        count += splitList[j]

print(count)