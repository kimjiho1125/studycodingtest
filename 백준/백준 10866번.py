from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if(command[0] == "push_front"):
        dq.appendleft(command[1])
    elif (command[0] == "push_back"):
        dq.append(command[1])
    elif (command[0] == "pop_front"):
        if(len(dq) == 0):
            print("-1")
        else:
            k = dq.popleft()
            print(k)
    elif (command[0] == "pop_back"):
        if(len(dq) == 0):
            print("-1")
        else:
            k = dq.pop()
            print(k)
    elif (command[0] == "size"):
        print(len(dq))
    elif (command[0] == "empty"):
        if(len(dq) == 0):
            print("1")
        else:
            print("0")
    elif (command[0] == "front"):
        if(dq):
            print(dq[0])
        else:
            print("-1")
    elif (command[0] == "back"):
        if(dq):
            print(dq[len(dq)-1])
        else:
            print("-1")

