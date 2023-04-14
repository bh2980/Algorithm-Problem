def solution(triangle):
    # 7
    # 3 8
    # 8 1 0
    # 2 7 4 4
    # 4 5 2 6 5
    
    # 점화식은 triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = 0
    
    floor = len(triangle)
    
    for i in range(1, floor):
        floor_length = len(triangle[i])
        prev_floor_length = len(triangle[i - 1])
                           
        for j in range(floor_length):
            comp_list = []
            
            if 0 <= i-1 < floor and 0 <= j-1 < prev_floor_length:
                comp_list.append(triangle[i-1][j-1])

            if 0 <= i-1 < floor and 0 <= j < prev_floor_length:
                comp_list.append(triangle[i-1][j])

            triangle[i][j] += max(comp_list)
            
    return max(triangle[floor - 1])