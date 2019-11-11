def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
N = int(input())
for i in range (0,N):
    print(fibb(i), end = ', ')
