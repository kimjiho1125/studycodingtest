import sys
from collections import deque

n = int(sys.stdin.readline())

#board 초기화
board = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
count = 0 #단지수
result = [] #단지별 숫자 저장

#동서남북
dy = [-1,0,1,0]
dx = [0,1,0,-1]

#bfs - 방문처리 및 단지내 집 수 카운트
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt = 1 #단지별 집 수

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #방문 가능하면
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))
            count += 1

result.sort()
print(count)
for num in result:
    print(num)