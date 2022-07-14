def solution(n):
    #f(n) = 3 * f(n-2) + 2 * f(n-4) + f(n-6) * 1 + 1
    n //= 2
    
    dp = [1 for _ in range(n+1)]
    
    try:
        dp[1] = 3
        dp[2] = 11
        dp[3] = 41
    except:
        pass
    
    for i in range(4, n + 1):
        dp[i] = 3 * dp[i-1] + 2 * sum(dp[:i-1])
    
    return dp[n] % 1000000007