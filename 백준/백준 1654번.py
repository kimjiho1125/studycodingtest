# 랜선 자르기
import sys

# k,n입력받기
k, n = map(int, sys.stdin.readline().split())
num_list = []

for i in range(k):
    num_list.append(int(sys.stdin.readline()))

start = 1
end = max(num_list)

while (start <= end):
    mid = (start+end) // 2
    cnt = 0
    for i in range(k):
        cnt += num_list[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# 이분 탐색을 이용한 문제
