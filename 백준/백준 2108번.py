import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(numbers)/N))

#중앙값
numbers.sort()
print(numbers[len(numbers) // 2])

#최빈값
countValue = Counter(numbers).most_common()
#최빈값이 2개 이상일 때
if len(countValue) > 1 and countValue[0][1] == countValue[1][1]:
    print(countValue[1][0])
else:
    print(countValue[0][0])

#번위
print(numbers[len(numbers)-1]-numbers[0])