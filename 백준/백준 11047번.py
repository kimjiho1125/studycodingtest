n,k = map(int,input().split())
coins = []
count = 0

for i in range(n):
    x = int(input())
    coins.append(x)

for i in range(n-1,-1,-1):
    if k==0:
        break
    if coins[i] > k:
        continue
    count += k//coins[i]
    k %= coins[i]

print(count)
           
