
a=  input()

alphabet = list()
indexList = list()

for i in range(26):
    indexList.append(-1)

for i in range(97, 123):
    alphabet.append(i)



for i in a:
    for j in alphabet:
       if(ord(i) == j):
           indexList[j-97] = a.index(i)
           alphabet.pop(alphabet.index(j))
           break


for i in indexList:
    print (i, end=' ')