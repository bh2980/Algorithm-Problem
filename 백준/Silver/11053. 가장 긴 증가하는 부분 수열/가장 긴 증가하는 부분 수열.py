def solution(n, num_list):
    # 이전에 있는 것들 중 나보다 작으면서 최대 길이가 가장 큰 것

    dp = dict([[i, 1] for i in range(n)])

    max_length = 1

    for i in range(1, n):
        # 최대 길이가 가장 큰 순으로 정렬
        # 나보다 작은 것을 찾음
        for idx, length in sorted(list(dp.items()), key = lambda x: -x[1]):
            if idx < i and num_list[idx] < num_list[i]:
                dp[i] = length + 1

                max_length = max(max_length, dp[i])
                break

    return max_length

n = int(input())
num_list = list(map(int, input().split()))

print(solution(n, num_list))