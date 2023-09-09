count_1 = 0
count_0 = 0

def recursiveCheck(arr, start_point, length):
    global count_1, count_0
    
    s_x, s_y = start_point
    
    # 1x1인 경우
    if(length == 1):
        if arr[s_x][s_y] == 0:
            count_0 += 1
        else:
            count_1 += 1
        
        return
    
    # 사각형 내부 합 계산
    check_sum = 0
    
    for i in range(s_x, s_x + length):
        for j in range(s_y, s_y + length):
            check_sum += arr[i][j]
    
    # 모두 같은 경우
    if check_sum == 0:
        count_0 += 1
        return
    
    if check_sum == length ** 2:
        count_1 += 1
        return
    
    # 4개로 나누기
    half_length = length // 2
        
    dx = [0, half_length]
    dy = [0, half_length]
    
    arr_list = []
    
    for diff_x in dx:
        for diff_y in dy:
            recursiveCheck(arr, (s_x + diff_x, s_y + diff_y), half_length)

def solution(arr):
    global count_1, count_0
    
    # 재귀함수로 풉니다
    # 만약 전체가 다 같은 수가 아니라면 4등분합니다.
    # 4등분한 내부 개수가 전부 같다면 그 수를 return합니다. 0 or 1
    # 1x1이라면 그 수를 return합니다.
    # return된 값을 모아서 개수를 세어 출력합니다.
    
    recursiveCheck(arr, (0, 0), len(arr))
    
    return [count_0, count_1]