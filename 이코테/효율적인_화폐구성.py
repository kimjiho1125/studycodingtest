n,m = map(int, input().split())
costs = []
d = [10001] * (m+1)

for _ in range(n):
  costs.append(int(input()))

d[0] = 0

for i in range(n):
  for j in range(costs[i], m+1):
    if d[j - costs[i]] != 10001:
      d[j] = min(d[j], d[j - costs[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])