def solution(n, num_list):
    dp = num_list[:]

    for i in range(n):
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i], dp[j] + num_list[i])

    return max(dp)

n = int(input())
num_list = list(map(int, input().split()))

print(solution(n, num_list))