from collections import deque

n,m = map(int, input().split())
board = []
visited = [[False for _ in range(m)] for _ in range(n)]
count = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    board.append(input())

def bfs(board, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = False

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '0' and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if board[i][j] == '0' and not visited[i][j]:
            bfs(board, (i,j), visited)
            count += 1

print(count)