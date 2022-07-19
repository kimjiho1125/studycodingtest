import sys 
from collections import deque

N,K = map(int,sys.stdin.readline().split())

q = deque()
result = []

for i in range(1,N+1):
    q.append(i)

while q:
    for i in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end='')
for i in range(N):
    if (i < N-1):
        print(result[i], end=', ')
    if (i == N-1) :
        print(result[i], end='>')
