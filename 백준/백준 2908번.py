N = list(input().split())
nN = []
for x in N:
    x = list(x)
    x.reverse()
    nN.append("".join(map(str,x)))

print(max(nN[0],nN[1]))
        
#join함수와 reverse함수가 포인트. reverse함수는 list에서만 쓸 수 있음