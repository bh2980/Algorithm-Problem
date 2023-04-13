def solution(n):
    dp = [0 for _ in range(n + 1)]

    for i in range(2, n + 1): #범위 수정
        comp_list = [dp[i - 1]]

        if i % 3 == 0:
            comp_list.append(dp[i // 3])

        if i % 2 == 0:
            comp_list.append(dp[i // 2])

        dp[i] = min(comp_list) + 1

    target = n
    make_list = [n]

    while n > 1:
        if dp[n] - 1 == dp[n-1]:
            make_list.append(n - 1)
            n -= 1
        elif n % 3 == 0 and dp[n] - 1 == dp[n // 3]:
            make_list.append(n // 3)
            n //= 3
        elif n % 2 == 0 and dp[n] - 1 == dp[n // 2]:
            make_list.append(n // 2)
            n //= 2

    print(dp[target])
    for num in make_list:
        print(num, end=' ')

n = int(input())

solution(n)