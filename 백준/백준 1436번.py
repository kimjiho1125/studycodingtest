import sys

input_number = int(sys.stdin.readline())
first_number = 666
cnt = 0
while input_number:
    if "666" in str(first_number):
        input_number -= 1
    first_number += 1

print(first_number-1)
