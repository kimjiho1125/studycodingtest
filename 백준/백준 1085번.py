# x,y,w,h
# min 함수를 이용하여 풀이
x, y, w, h = map(int, input().split())

min1 = w-x
min2 = h-y

print(min(min1, min2, x, y))
