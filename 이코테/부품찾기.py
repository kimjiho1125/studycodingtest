import sys

def binary_search(array, target, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if array[mid] > target:
    return binary_search(array, target, start, mid-1)
  elif array[mid] < target:
    return binary_search(array, target, mid+1, end)
  else:
    return mid+1

N = int(input())
parts = list(map(int,sys.stdin.readline().rstrip().split()))
parts.sort()

M = int(input())
req = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(M):
  if binary_search(parts, req[i], 0, N-1):
    print("yes")
  else:
    print("no")