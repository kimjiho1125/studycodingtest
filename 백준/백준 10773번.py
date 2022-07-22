import sys

numbers = []

K = int(sys.stdin.readline())

for _ in range(K):
    k = int(sys.stdin.readline())
    if(k == 0):
        numbers.pop()
    else:
        numbers.append(k)

print(sum(numbers))