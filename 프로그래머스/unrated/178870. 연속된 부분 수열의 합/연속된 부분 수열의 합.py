def solution(sequence, k):
    ans_p1 = 0
    ans_p2 = len(sequence) + 1
    
    # p1부터 p2 - 1까지
    p1 = 0
    p2 = 0
    
    array_sum = sequence[0]
    
    # 합이 k보다 작으면, 길이를 늘린다.
    # 합이 k보다 크면, 앞에서부터 길이를 줄인다.
    # 이를 끝까지 반복한다. -> 가장 작은 길이를 계속 업데이트
        # 길이가 같으면 업데이트하지 않음.
        # 길이가 작으면 p2 - p1
        # 시작 idx가 작으면 p1
    while p1 < len(sequence) and p2 < len(sequence):
        if array_sum < k:
            p2 += 1
            if p2 < len(sequence):
                array_sum += sequence[p2]
        elif array_sum > k:
            array_sum -= sequence[p1]
            p1 += 1
        else: # array_sum == k
            min_length = ans_p2 - ans_p1 + 1
            current_length = p2 - p1 + 1

            if current_length < min_length:
                ans_p1 = p1
                ans_p2 = p2

            p2 += 1
            if p2 < len(sequence):
                array_sum += sequence[p2]

    return [ans_p1, ans_p2]