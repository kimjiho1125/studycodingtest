import sys

L = int(sys.stdin.readline())
answer = 0

a = list(sys.stdin.readline())
for i in range(L):
    x = ord(a[i]) - 96
    result = x*(31**i)
    answer += result

print(answer%1234567891)