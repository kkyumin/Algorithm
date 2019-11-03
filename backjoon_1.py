intList = list()

first = int(input())

second = input()

newList = second.split()

# map int 처리는 확실히 해줄것!
newList = list(map(int,newList[0:first]))

min = newList[0]
max = newList[0]
for i in newList:
    if(i < min):
        min = i
        continue
    if(i > max):
        max = i

print(min, max)