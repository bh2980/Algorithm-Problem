# [1, 3] 1 -> 3으로 옮기는 과정

# [1, 2], [1, 3], [2, 3] 1 -> 3으로 옮기는 과정

# [1, 3], [1, 2], [3, 2] 1 -> 2로 옮기는 과정 : 3을 2로 2를 3으로
# [2, 1], [2, 3], [1, 3] 2 -> 3 으로 옮기는 과정 : 1을 2로 2룰 1로

# [1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3] : 합체

# dp 문제

def solution(n):
    answer = [[]]
    
    dp = [[] for _ in range(n + 1)]

    dp[1] = [[1, 3]]
    
    for i in range(2, n + 1):
        left_arr_list = []
        right_arr_list = []
        
        for k, v in dp[i-1]:
            a, b = k, v
            
            if k == 3:
                a = 2
            elif k == 2:
                a = 3
            
            if v == 3:
                b = 2
            elif v == 2:
                b = 3
                
            left_arr_list.append([a, b])
        
        for k, v in dp[i-1]:
            a, b = k, v
            
            if k == 1:
                a = 2
            elif k == 2:
                a = 1
            
            if v == 1:
                b = 2
            elif v == 2:
                b = 1
                
            right_arr_list.append([a, b])
        
        dp[i] = left_arr_list + [[1, 3]] + right_arr_list
        
    return dp[n]