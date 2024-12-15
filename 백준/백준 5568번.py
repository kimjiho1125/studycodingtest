#from itertools import permutations
#import sys

#input = sys.stdin.readline

#n = int(input())
#k = int(input())

#cards = [input().rstrip() for _ in range(n)]
#candidates = list(permutations(cards, k))
#results = set()

#for candidate in candidates:
#  results.add(''.join(candidate))

#print(len(results))

#백트래킹
import sys

input = sys.stdin.readline

def dfs(depth):
  if depth == k:
    s.add(''.join(map(str, li)))
    return
  for i in range(n):
    if check[i]:
      continue
    li.append(cards[i])
    check[i] = 1
    dfs(depth + 1)
    li.pop()
    check[i] = 0

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
li, s = [], set()
check = [0]*n
dfs(0)
print(len(s))