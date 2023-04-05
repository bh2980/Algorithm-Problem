# from collections import Counter

def Counter(list):
    count_number = dict()

    for num in list:
        if num not in count_number:
            count_number[num] = 0

        count_number[num] += 1

    return count_number

def flipMatrix(arr):
    flip_arr = list(map(list, zip(*arr)))

    return flip_arr

def operateR(arr):
    row_count = len(arr)

    new_arr = [[] for _ in range(row_count)]

    max_len = 0

    # R 연산 수행
    for i in range(row_count):
        for item in sorted(Counter(arr[i]).items(), key=lambda x: (x[1], x[0])):
            if item[0] == 0:  # 0은 고려하지 않음.
                continue

            new_arr[i] += item

        max_len = max(len(new_arr[i]), max_len)

    if max_len > 100:
        max_len = 100

    # 크기 조절
    for i in range(row_count):
        if len(new_arr[i]) <= max_len:
            new_arr[i] += [0 for _ in range(max_len - len(new_arr[i]))]
        else: # 길이가 100보다 큰 경우
            new_arr[i] = new_arr[:100]

    return new_arr

def solution(r, c, k, arr):
    # 배열의 크기는 3 x 3
    # 정렬은 1초마다 빈도 -> 숫자 순으로 오름차순 정렬하되 [숫자, 빈도, 숫자, 빈도, ...] 꼴로 새로운 배열은 만듬
        # 정렬 시 0은 세지 않음
    # 행의 개수와 열의 개수를 비교해서 행이 같거나 크면 행을 기준으로, 열이 크면 열을 기준으로 정렬
    # 길이가 다를 경우 가장 긴 배열을 기준으로 모자란 길이를 0으로 채움
    # 길이가 100을 넘어가면 100개 이후 무시
    # (1 ≤ r, c, k ≤ 100) -> 1부터 시작함. 조심

    # arr[r][c]의 값이 k가 되는 최소 시간, 100초가 넘더라도 안되면 -1

    time = 0

    while time <= 100:
        # 행과 열 크기 비교
        row_count = len(arr)
        col_count = len(arr[0])

        # 조건 충족 시 return
        if r <= row_count - 1 and c <= col_count - 1 and arr[r][c] == k:
            return time

        if row_count >= col_count:
            # R연산 수행 후 크기 조절
            arr = operateR(arr)

        else:
            #C 연산 수행

            # 뒤집기
            arr = flipMatrix(arr)

            # R연산과 동일 계산 후 크기 조절
            arr = operateR(arr)

            # 뒤집기
            arr = flipMatrix(arr)

        time += 1

    # 100초가 지나면 -1 return
    return -1


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

print(solution(r - 1, c - 1, k, arr))