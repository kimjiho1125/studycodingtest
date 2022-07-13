# 검증수
import sys
num_list = list(map(int, sys.stdin.readline().split()))
sum = 0

for i in range(len(num_list)):
    sum += (num_list[i]**2)

sum = sum % 10

print(sum)
