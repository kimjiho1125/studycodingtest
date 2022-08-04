import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        number = int(command[1])
    
    if command[0] == "add":
        if number not in S:
            S.add(number)
    if command[0] == "remove":
        if number in S:
            S.remove(number)
    if command[0] == "check":
        if number in S:
            print('1')
        else:
            print('0')
    if command[0] == "toggle":
        if number in S:
            S.remove(number)
        else:
            S.add(number)
    if command[0] == "all":
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    if command[0] == "empty":
        S.clear()