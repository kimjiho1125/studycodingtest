import sys

cnt = int(sys.stdin.readline())
stack = []
answer = []
count = 1
flag = 0

for i in range(cnt):
    num = int(sys.stdin.readline())
    while count <= num:  # 입력한 수를 만날 때까지 오름차순으로 push
        stack.append(count)
        answer.append("+")
        count += 1

    if stack[-1] == num:  # stack의 Top이 입력한 숫자와 같으면
        stack.pop()      # 스택의 Top을 꺼내 수열을 만들어줌
        answer.append("-")
    else:               # 스택에 오름차순으로 입력되었기 때문에
        print("NO")     # stack의 Top이 입력한 수가 아니면 수열을 만들 수 없다
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
