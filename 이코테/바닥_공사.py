#정수 n 입력받기
n = int(input())

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 1000

#다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
  dp[i] = (dp[i-1] + dp[i-2]*2) % 796796

#계산된 결과 출력
print(dp[n])