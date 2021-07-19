#문자열 S입력받기
s = input()
#결과를 출력할 리스트 result 만들기
result = []
#숫자를 더한 결과값 num 
num = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        num += int(i)

result.sort()

if num > 0 :
    result.append(str(num))


print(''.join(result))