def solution(n, num_list):
    # 이전에 있는 것들 중 나보다 작으면서 최대 길이가 가장 큰 것

    dp = [1 for _ in range(n)]

    for i in range(1, n):
        # 나보다 작은 idx 중에
        # 가장 긴 길이를 찾아서 + 1
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

n = int(input())
num_list = list(map(int, input().split()))

print(solution(n, num_list))