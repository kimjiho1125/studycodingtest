import sys

N = int(sys.stdin.readline())
person=[]

for i in range(N):
    list1 = list(map(int,sys.stdin.readline().split()))
    person.append(list1)

order = []

for i in range(N):
    cnt = 0
    for j in range(N):
        if (i==j):
            continue
        else:
            if (person[i][0] < person[j][0] and person[i][1] < person[j][1]):
                cnt += 1
    order.append(cnt+1)

for i in order:
    print(i,end=' ')
