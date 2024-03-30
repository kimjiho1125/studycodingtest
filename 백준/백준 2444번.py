import sys

n = int(sys.stdin.readline())
middle = int((2*n-1) / 2) + 1 
l = 1 + 2*(middle - 1)
num = 1
space = (l - 1) // 2

for i in range(1,(2*n-1)+1):
    for _ in range(space):
        print(" ",end='')
    for _ in range(num):
        print("*",end='')
    print(end="\n")
    if i < middle:
        space -= 1
        num += 2
    elif i >= middle:
        space += 1
        num -= 2

