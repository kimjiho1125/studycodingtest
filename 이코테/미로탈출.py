from collections import deque

n, m = map(int, input().split())
graph = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(i,j):
    queue = deque([(i,j)])

    while queue:
        x,y = queue.popleft()

        if x == n-1 and y == m-1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
            
bfs(0,0)

print(graph[n-1][m-1])