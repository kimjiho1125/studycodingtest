import sys 

n = int(sys.stdin.readline())
number1= set(sys.stdin.readline().split())

c = int (sys.stdin.readline())
number2 = sys.stdin.readline().split()

for i in number2:
    if i in number1:
        print('1')
    else:
        print('0')
    

     
        