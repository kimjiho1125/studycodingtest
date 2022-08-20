# #현재 나이트 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
# count = 0

# #나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2,-1),(-2,1),(-1,-2),(-1,+2),(1,-2),(1,2),(2,-1),(2,1)]

# for step in steps:
#     new_row = row + step[0]
#     new_column = column + step[1]

#     if new_row >= 1 and new_column >= 1 and new_row <=8 and new_column <= 8:
#         count += 1

# print(count)

import sys

input = sys.stdin.readline

steps = [(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2)]

location = input()

coulmn = int(ord(location[0])) - int(ord('a'))+1
row = int(location[1])
count = 0

for step in steps:
    new_column = coulmn + step[0]
    new_row = row + step[1]

    if new_column <= 8 and new_column >= 1 and new_row <= 8 and new_row >= 1: 
        count += 1

print(count)