def solution(N, numList):
    dp = [[0 for _ in range(len(numList))] for _ in range(3)]

    dp[0][0] = numList[0]
    dp[1][0] = numList[0]
    dp[2][0] = numList[0]

    # 이전 최댓값 vs 이전 최댓값 + 현재값 vs 현재값

    for i in range(1, len(numList)):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = max(dp[1][i-1], dp[2][i-1]) + numList[i]
        dp[2][i] = numList[i]
    #
    # for line in dp:
    #     print(line)

    return max(dp[0][N-1], dp[1][N-1], dp[2][N-1])

N = int(input())
numList = list(map(int, input().split()))

print(solution(N, numList))