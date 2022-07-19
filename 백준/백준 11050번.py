import sys

def factorial(n):
    result = 1
    for i in range(1, n+1, 1):
        result *= i
    return result

N, K = map(int,sys.stdin.readline().split())

result = int(factorial(N) / (factorial(N-K)*factorial(K)))

print(result)