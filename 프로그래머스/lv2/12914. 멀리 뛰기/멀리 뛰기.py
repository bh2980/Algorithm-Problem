#딱 봐도 dp 문제
#1칸 전 + 2칸 전을 더하는데 거기서 무엇을 더 고려해야할까요?
#1칸 전에서 목적지에 도달하는 방법은 1개
#2칸 전에서 목적지에 도달하는 방법은 1칸 + 1칸, 2칸이나 1칸 + 1칸은 위에 포함되므로 1개
#따라서 dp[n] = dp[n-1] + dp[n-2]
#초기값은 dp[1] = 1, dp[2] = 2

def solution(n):
    answer = 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567