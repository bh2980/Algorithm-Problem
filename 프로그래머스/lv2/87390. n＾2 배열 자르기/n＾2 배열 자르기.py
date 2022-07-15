def solution(n, left, right):
    #모든 줄을 구하지 말고 구해야하는 줄만 구하기.
    first = left // n + 1
    last = right // n + 1
    
    num_arr = []
    
    for i in range(first, last+1):
        for _ in range(i):
            num_arr.append(i)
        
        for j in range(i+1, n+1):
            num_arr.append(j)

    answer = num_arr[left % n : right - (left // n) * n +1]
    return answer