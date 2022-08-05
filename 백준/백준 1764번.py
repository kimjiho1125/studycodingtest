import sys

N , M = map(int,sys.stdin.readline().split())
NoListen = set()
NoSee = set()

for _ in range(N):
    NoListen.add(sys.stdin.readline().strip())
    
for _ in range(M):
    NoSee.add(sys.stdin.readline().strip())

common = sorted(list(NoListen & NoSee))

print(len(common))

for i in common:
    print(i)

