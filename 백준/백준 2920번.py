from audioop import reverse
from operator import truediv

# 풀이 1
num_list = list(map(int, input().split()))

if num_list == sorted(num_list):
    print("ascending")
elif num_list == sorted(num_list, reverse=True):
    print("descending")
else:
    print("mixed")


# 풀이 2 sort함수 직접 구현
def BubbleSort(x):
    for i in reversed(range(len(x))):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]  # swap
    return x


def BubbleSortReverse(x):
    for i in reversed(range(len(x))):
        for j in range(i):
            if x[j] < x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]  # swap
    return x


input_list = num_list.copy()  # input_list 값이 변경 되지 않게 얕은복사

if input_list == BubbleSort(num_list):
    print("ascending")
elif input_list == BubbleSortReverse(num_list):
    print("descending")
else:
    print("mixed")

# 알게된 점
# 파이썬에서 input_list = num_list 이런식으로 할당을 하면 포인터를 할당함(깊은 복사)
# 따라서 num_list가 변함에 따라 input_list를 변하지 않게 하려면 얕은 복사를 해야함
# 파이썬에서 얕은 복사를 하는 방법은 복사하려는 리스트 옆에 명시적으로 .copy()함수를 사용해 주면 됨
# ex. input_list = num_list.copy()
