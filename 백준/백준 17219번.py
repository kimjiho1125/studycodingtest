import sys

N,M = map(int,sys.stdin.readline().split())
result = {}

for _ in range(N):
    URL , PW = sys.stdin.readline().split()
    result[URL] = PW

for _ in range(M):
    print(result[sys.stdin.readline().rstrip()])


