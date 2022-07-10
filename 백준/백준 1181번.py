import sys
# 횟수 입력받기
# 입력받을 때 sys.stdin.readline()으로 입력받으면 입력속도를 1/10 수준으로 줄일 수 있음!
# n = int(input())
n = int(sys.stdin.readline())
char_list = []

# 횟수만큼 단어 입력받기
for i in range(n):
    char_list.append(sys.stdin.readline().strip())

# 중복 제거
set_list = set(char_list)
char_list = list(set_list)

# 정렬
char_list.sort()
char_list.sort(key=len)

for i in char_list:
    print(i)

# 정리
# sort() => 숫자 뿐만 아니라 문자열을 알파벳 순서대로 정렬해줌
# sort(key = len) => 문자열을 길이 순서대로 정렬해줌
# 중복을 제거할 때는 set 이용
# sys.stdin.readline()은 input()에 비해 속도가 10배가량 빠름
