import math
import sys 

n1, n2 = map(int,sys.stdin.readline().split())

#Solution 1 math 라이브러리 사용
print(math.gcd(n1,n2)) #두 수의 최대공약수
print(math.lcm(n1,n2)) #두 수의 최소공배수

#Solution 2 직접 구현
# def gcd(a,b):
#     for i in range(min(a,b),0,-1):
#         if a % i == 0 and b % i == 0:
#             return i

# def lcm(a,b):
#     for i in range(max(a,b),(a*b)+1):
#         if i % a == 0 and i % b == 0:
#             return i


