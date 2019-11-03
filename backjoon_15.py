#
# def star(cnt,start,arr):
#     print(cnt)
#     fuck = 3**cnt
#     for i in range(fuck, (fuck))):
#         for j in range(fuck, (2*(fuck))):
#                 arr[i][j] = " "
#
#
# n = int(input())
# v=n ;cnt = 0;
#
# while v!=1:
#     v/=3
#     cnt+=1
#
# cnt = int(cnt)
# print(cnt)
#
# arr =[["*"]*n for i in range(n)]
#
# print(arr)
# cnt = cnt-1
#
# star(cnt,start,arr)
#
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end ="")
#     print()

#
# n = int(input())
#
# for i in range(0,n):
#     for j in range(0,n):
#         dx = i
#         dy = j
#         while(dx):
#             if(dx% 3 == 1 and dy % 3 ==1):
#                 break
#             dx = dx//3
#             dy = dy//3
#         if(dx>0):
#             print(" ",end ="")
#         else:
#             print("*",end = "")
#     print("")
#

n = int(input())
arr = [["*"]*n for _ in range(n)]

v=n; cnt = 0
while v!= 1:
    v/=3
    cnt+=1
for cnt_ in range(cnt):
    idx = [i for i in range(n) if (i//3 ** cnt_)% 3 ==1 ]
    for i in idx:
        for j in idx:
            arr[i][j] = " "

print("\n".join([''.join([str(i) for i in row]) for row in arr]))