#분해합
import sys

n = int(sys.stdin.readline())
result = 0

for i in range (1, n+1):
    x = list(map(int,str(i)))
    s = i + sum(x)
    if (s == n):
        result = i
        break

print(result)







