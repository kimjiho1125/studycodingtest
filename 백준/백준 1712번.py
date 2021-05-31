#A=고정비용 B=가변비용 C=노트북가격
A,B,C = list(map(int,input().split()))
BEpoint = 0
if (B >= C):
    BEpoint = -1
else:
    BEpoint = A//(C-B)+1
print(BEpoint)