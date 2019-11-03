a  = input()

word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(word)):
    a = a.replace(word[i], str(i))

print(len(a))