a=  input()

inputList = a.split(" ")


for i in range(2):
    a = inputList.pop(0)
    inputList.append(a[::-1])

inputList = list(map(int,inputList))

print(max(inputList))