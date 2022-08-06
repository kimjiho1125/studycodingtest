import sys

N = int(sys.stdin.readline())

sumN = 0
#5의 배수의 개수 + 25의 배수의 개수 + 125의 배수의 개수
sumN += int(N/5)
sumN += int(N/25)
sumN += int(N/125)

print(sumN)