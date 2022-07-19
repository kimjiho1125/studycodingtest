import sys

N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    numbers.append((x, y))

numbers.sort(key=lambda x: x[0])
numbers.sort(key=lambda x: x[1])

for i in numbers:
    print(i[0], i[1])
