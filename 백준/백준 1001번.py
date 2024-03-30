import sys

t = int(sys.stdin.readline())

for _ in range(t):
     x,y = map(int, sys.stdin.readline().split())
     distance = y - x
     count = 0 #이동 횟수
     move = 1 #count별 빈도수
     move_plus = 0 #이동한 거리의 합
     while move_plus < distance:
          count += 1
          move_plus += move
          if count % 2 == 0:
               move += 1
     print(count)
