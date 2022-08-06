from curses.ascii import isalpha
from re import A
import sys

N, M = map(int,sys.stdin.readline().split())
Pdic = {}

for i in range(1,N+1):
    a = sys.stdin.readline().strip()
    Pdic[i] = a
    Pdic[a] = i

for _ in range(M):
    inputString = sys.stdin.readline().strip()
    if inputString.isalpha():
        print(Pdic[inputString])
    else:
        print(Pdic[int(inputString)])
