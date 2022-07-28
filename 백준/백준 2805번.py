import sys

N,M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
left = 0
right = max(trees)
result = 0

while left <= right:  
    mid = (left + right) // 2
    _sum = 0
    for tree in trees:
        if tree > mid :
            _sum += tree - mid
            if _sum > M:
                break

    if _sum < M :
        right = mid - 1
    else:
        result = mid
        left = mid + 1
        
print(result)

#이분 탐색 이용
