def solution(N, M):
    lenN = len(N)
    lenM = len(M)

    dp = [[0 for _ in range(lenM + 1)] for _ in range(lenN + 1)]

    for i in range(1, lenN + 1):
        for j in range(1, lenM + 1):
            charN = N[i - 1]
            charM = M[j - 1]

            if charN == charM:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[lenN][lenM]

N = input()
M = input()

print(solution(N, M))