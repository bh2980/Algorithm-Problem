def solution(n):
    triangle = [[0 for _ in range(i + 1)] for i in range(n)]
    
    direction = [(1, 0), (0, 1), (-1, -1)]
    d_idx = 0
    cr, cc = -1, 0
    
    number = 1
    
    while n > 0:
        for i in range(n):
            dr, dc = direction[d_idx]
            cr += dr
            cc += dc
                
            triangle[cr][cc] = number
        
            number += 1
            
        n -= 1
        d_idx = (d_idx + 1) % 3
            
    answer = []
    
    for line in triangle:
        answer += line
        
    return answer