import heapq
import sys

#입력의 개수가 많을 경우를 대비해 readline함수 사용
input = sys.stdin.readline
#무한을 의미하는 값으로 10억 설정
INF = int(1e9)
#노드의 개수, 간선의 개수 입력받기
n,m = map(int, input().split())
#시작 노드 입력받기
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선의 정보 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijikstra(start):
  q = []
  #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q: #큐가 비어있지 않다면
    #가장 최단 거리가 짧은 노드의 정보 꺼내기
    dist, now = heapq.heappop(q)
    #현재 노드가 이미 처리된 적 있으면 무시
    if distance[now] < dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      #현재 노드를 거쳐서, 해당 노드로 연결했을 때의 거리 구하기
      cost = distance[now] + i[1]
      #현재 노드를 거쳐 해당 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        #최단 거리 갱신
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))
#다익스트라 알고리즘을 수행
dijikstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  #도달할 수 없는 경우, 무한이라고 출력
  if distance[i] == INF:
    print("INFINITY")
  #도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])