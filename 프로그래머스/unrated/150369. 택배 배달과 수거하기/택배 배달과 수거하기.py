def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while True:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()

        while pickups and pickups[-1] == 0:
            pickups.pop()

        answer += max(len(deliveries), len(pickups)) * 2

        if not deliveries and not pickups:
            break

        d_cap = cap
        i = len(deliveries) - 1

        while deliveries and d_cap > 0:
            if deliveries[i] >= d_cap:
                deliveries[i] -= d_cap
                d_cap = 0
            else:
                d_cap -= deliveries[i]
                deliveries[i] = 0

            i -= 1

            if i < 0:
                break

        p_cap = cap
        i = len(pickups) - 1

        while pickups and p_cap > 0:
            if pickups[i] >= p_cap:
                pickups[i] -= p_cap
                p_cap = 0
            else:
                p_cap -= pickups[i]
                pickups[i] = 0

            i -= 1

            if i < 0:
                break

    return answer