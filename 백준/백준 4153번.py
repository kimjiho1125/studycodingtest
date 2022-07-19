import sys

flag = 0

while flag == 0:
    numbers = []
    numbers = list(map(int,sys.stdin.readline().split()))

    if(numbers == [0,0,0]):
        flag = 1
        break

    numbers.sort()

    if ((pow(numbers[0],2) + pow(numbers[1],2)) == pow(numbers[2],2)):
        print("right")
    else:
        print("wrong")

    