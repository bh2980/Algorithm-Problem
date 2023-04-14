from heapq import heappush, heappop

def solution(n, num_list):
    # 이전에 있는 것들 중 나보다 작으면서 최대 길이가 가장 큰 것

    dp_inc = [1 for _ in range(n)]

    for i in range(1, n):
        # 나보다 작은 idx 중에
        # 가장 긴 길이를 찾아서 + 1
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

    num_list = num_list[::-1]
    dp_inc_rev = [1 for _ in range(n)]

    for i in range(1, n):
        # 나보다 작은 idx 중에
        # 가장 긴 길이를 찾아서 + 1
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp_inc_rev[i] = max(dp_inc_rev[i], dp_inc_rev[j] + 1)

    return max([sum([a, b]) for a, b in zip(dp_inc, dp_inc_rev[::-1])]) - 1

n = int(input())
num_list = list(map(int, input().split()))

print(solution(n, num_list))