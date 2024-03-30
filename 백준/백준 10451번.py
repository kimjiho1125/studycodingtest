#순열 사이클
#사이클. 즉 순회 => 대놓고 DFS, BFS문제임

import sys

t = int(sys.stdin.readline())

def dfs(v):
    visited[v] = True
    nv = graph[v]

    if not visited[nv]:
        dfs(nv)

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = list(map(int, sys.stdin.readline().split()))
    graph.insert(0,0) #인덱스를 맞추기 위해서
    visited = [False] * (n + 1)
    cycle = 0

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
            cycle += 1
        
    print(cycle)