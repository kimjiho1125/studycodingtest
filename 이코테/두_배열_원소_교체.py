n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0

a.sort()
b.sort(reverse=True)


for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break
        
print(a)