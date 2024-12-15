from collections import deque

#도시의 가로, 세로 크기 입력받기
n,m = map(int, input().split())
maps = []
#방문 여부를 표시할 리스트 초기화
visited = [[False] * n for _ in range(m)]

#도시의 형태 입력받기
for _ in range(m):
  maps.append(list(map(int, input().split())))

#이동 방향 동,남
dx = [0, 1]
dy = [1, 0]

#bfs 소스코드 구현
def bfs(start):
  x, y = start
  queue = deque([start])
  visited[x][y] = True

  #큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()

    #현재 위치에서 동쪽, 남쪽 방향 체크
    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]

      # 조건에 만족하는 경우 방문 표시 하고 queue에 추가
      if nx < m and ny < n and maps[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx,ny))

#bfs수행
bfs((0,0))

#결과 출력
if visited[m-1][n-1]:
  print("Yes")
else:
  print("No")