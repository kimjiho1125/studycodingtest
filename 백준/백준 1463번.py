import sys 

input = sys.stdin.readline

x = int(input())

arr = [0] * (x+1)

for i in range(2, x+1):
    arr[i] = arr[i-1]+1
    if(i%2==0 and arr[i]>arr[i//2]+1):
        arr[i] = arr[i//2]+1
    if(i%3==0 and arr[i]>arr[i//3]+1):
        arr[i] = arr[i//3]+1

print(arr[x])

#DP 문제