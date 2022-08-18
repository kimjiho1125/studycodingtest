import sys 
import time

start = time.time()

input = sys.stdin.readline

N, K = map(int,input().split())
count = 0

while True:
    if (N % K == 0):
        N /= K
        count += 1
    else:
        N -= 1
        count += 1
    if (N == 1):
        break

print(count)
print("time : ", time.time()-start)