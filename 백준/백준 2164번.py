import sys
from collections import deque

N = int(sys.stdin.readline())
numbers = deque([])

for i in range(1,N+1):
    numbers.append(i)

while(len(numbers) > 1):
    #제일 위에 있는 카드를 바닥에 버린다.
    numbers.popleft()

    #제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    k = numbers.popleft()
    numbers.append(k)

print(numbers[0])