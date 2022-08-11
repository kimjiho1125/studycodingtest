import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int,input().split()))
prefix_sum = [0]

temp = 0

for i in numList:
    temp += i
    prefix_sum.append(temp)

for i in range(M):
    index1, index2 = map(int,input().split())
    print(prefix_sum[index2]-prefix_sum[index1-1])
    
