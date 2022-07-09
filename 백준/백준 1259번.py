# 팰린드롬수
# 문자열 뒤집기
while True:
    num_list = input()
    if (num_list == '0'):
        break
    elif (num_list == num_list[::-1]):
        print("yes")
    else:
        print("no")
