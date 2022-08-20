import sys

input = sys.stdin.readline

n = int(input())
# x => 현재 col y => 현재 row
x = 1
y = 1

#맵을 나타낼 2차원 배열 선언
array = [[0 for col in range(n)] for row in range(n)]

#계획서 입력받기
plans = input().split()

for i in plans:
    if i == "R":
        if (y+1) > n:
            continue
        else:
            y += 1
    if i == "L":
        if (y-1) < 1:
            continue
        else:
            y -= 1
    if i == "U":
        if (x-1) < 1:
            continue
        else:
            x -= 1
    if i == "D":
        if (x+1) > n:
            continue
        else:
            x += 1

print(x,y)
