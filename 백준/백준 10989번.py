import sys

N = int(sys.stdin.readline())
numbers = [0 for i in range(10001)]

for i in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i in range(len(numbers)):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)


#sort함수 쓰면 메모리 초과 발생 => for문 이 실행될때마다 메모리 재할당이 일어나기 때문
#계수 정렬을 사용하여 메모리 문제를 해결
#리스트의 길이만큼 무조건 순회해야 한다는 비효율적 문제가 있으나 이번 문제에서는 10000보다 작거나 같은 자연수로 제한하였기 때문에
#메모리를 크게 차지하지 않는다