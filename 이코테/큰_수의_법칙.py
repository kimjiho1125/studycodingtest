import sys

input = sys.stdin.readline

# 1번 풀이

# N, M, K = map(int,input().split())

# data = list(map(int,input().split()))
# data.sort()

# first = data[N-1]
# second = data[N-2]

# result = 0

# while True:
#     for i in range(K):
#         if M == 0:
#             break;
#         result += first
#         M -= 1
#     if M == 0:
#         break;
#     result += second;
#     M -= 1

# print(result);

# 2번 풀이
N, M, K = map(int,input().split())

data = list(map(int,input().split()))
data.sort()
first = data[N-1]
second = data[N-2]

#가장 큰 수가 더해지는 횟수 계산
count = (M // (K+1)) * K
count += M % (K+1)

result = 0
result += count * first
result += (M-count) * second

print(result)