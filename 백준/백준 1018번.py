import sys

N, M = map(int,sys.stdin.readline().split())

board = []
repair = []

for _ in range(N):
    board.append(sys.stdin.readline())

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != 'W' :
                        first_W = first_W + 1
                    if board[k][l] != 'B' :
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W + 1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)
print(min(repair))

#브루스포스 문제
#첫번째,두번째 for문은 8x8씩 잘라서 모든 경우를 세기 위함 임
#세번째,네번째 for문은 8x8씩 실제로 잘라서 계산하는 부분임
#두 인덱스를 더해 2로 나누는 조건을 추가한 이유는 짝수번째 인덱스와 홀수번째
#인덱스를 한번에 계산하여 새로 칠해야할 개수를 세기 위함임