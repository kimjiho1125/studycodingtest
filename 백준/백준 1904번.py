n = int(input())

d = [1,1]

if n > 1:
    for i in range(2, n+1):
        d.append((d[i-1] + d[i-2]) % 15746)

print(d[n])
