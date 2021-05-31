def solution(sentence):
    result = ""
    if len(sentence) == 1:
        result = sentence
        return result
    
    else: 
        result += sentence[0]
        for i in range(1,len(sentence)):
            if sentence[i-1] != sentence[i]:
                result += sentence[i]
        return result

test_case = int(input())
cnt = 0
for i in range(test_case):
    sentence = input()
    ret = solution(sentence)
    if len(ret) == len(set(ret)):
        cnt += 1

print(cnt)
    