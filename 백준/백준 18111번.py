import sys

N, M, B = map(int,sys.stdin.readline().split())
grd = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
ans = 999999999999
height = 0

for i in range(257):
    up = 0
    down = 0
    for j in range(N):
        for k in range(M):
            if grd[j][k] > i:
                up += (grd[j][k] - i)
            else:
                down += (i - grd[j][k])
    inventory = up + B
    if inventory < down:
        continue
    time = 2*up+down
    if time <= ans:
        ans = time
        height = i
print(ans,height)

