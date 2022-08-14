import sys

input = sys.stdin.readline

# 풀이 1
# N,M = map(int,input().split())
# numbers = [[0] * M for _ in range(N)]
# selectCard = 0

# for i in range(N):
#     temp = list(map(int,input().split()))
#     for j in range(M):
#         numbers[i][j] = temp[j]
#     if(min(numbers[i]) > selectCard):
#         selectCard = min(numbers[i])

# print(selectCard)

# 풀이 2
N,M = map(int,input().split())
result = 0

for _ in range(N):
    data = list(map(int,input().split()))
    currentMin = min(data)
    result = max(currentMin, result)

print(result)