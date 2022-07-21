import sys
from collections import Counter

N = int(sys.stdin.readline())
list1 = sys.stdin.readline().split()
M = int(sys.stdin.readline())
list2 = sys.stdin.readline().split()

c = Counter(list1)
print(' '.join(f'{c[m]}' if m in c else '0' for m in list2))

#Counter함수 사용