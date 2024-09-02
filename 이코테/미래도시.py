n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

#간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
  a, b = map(int, input().split())
  #양뱡향 이므로 둘 모두 초기화
  graph[a][b] = 1
  graph[b][a] = 1

#거쳐 갈 노드 K와 최종 목적지 노드 X 입력받기
x, k = map(int, input().split())

#플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과 출력
distance = graph[1][k] + graph[k][x]

#도달할 수 없는 경우 -1을 출력
if distance >= INF:
  print(-1)
else:
  print(distance)


  



