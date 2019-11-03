n = int(input())

if (n < 100):
    print(n)
else:
    count = 0
    for i in range(100, (n + 1)):
        back = int(i/100)
        ship = int((i%100)/ 10)
        ill = int((i % 100) % 10)

        if ((back - ship) == (ship - ill)):
            count += 1
    print(99 + count)




