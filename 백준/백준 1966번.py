import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    N , M = map(int,sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))
    idx = list(range(len(imp)))
    idx[M] = "target"
    
    #순서
    order = 0

    while True:
        # 가장 왼쪽에 있는 문서의 중요도가 전체 문서중 가장 높다면
        if imp[0] == max(imp):
            order += 1
            # 가장 왼쪽에 있는 문서가 우리가 찾는 문서라면 
            if idx[0] == "target":
                print(order)
                break
            else:
                idx.pop(0)
                imp.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))                
