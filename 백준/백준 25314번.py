n = int(input())
answer = ''

num_of_long = n // 4
for _ in range(num_of_long):
    answer += 'long '

answer += 'int'

print(answer)
