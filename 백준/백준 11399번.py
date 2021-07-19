#사람수 N입력
n = int(input())
#시간 P
p = list(map(int,input().split()))

p.sort()
result = []
x = 0

for i in p:
    x += i
    result.append(x)

print(str(sum(result)))
