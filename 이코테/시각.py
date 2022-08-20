import sys

input = sys.stdin.readline

n = int(input())

# 24 x 60 x 60 = 86,400가지 이므로 경우의 수가 10만 이내이다.
# 따라서 2초안에 문제를 해결할 수 있음
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)