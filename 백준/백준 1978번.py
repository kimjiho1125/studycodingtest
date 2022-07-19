import sys

N = int(sys.stdin.readline())
cnt = 0

numbers = list(map(int,sys.stdin.readline().split()))

#소수 판별법
def primality(n):
    if (n==1):
        return False
    i=2
    while i*i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

for i in numbers:
    if primality(i)==True:
        cnt += 1

print(cnt)
    