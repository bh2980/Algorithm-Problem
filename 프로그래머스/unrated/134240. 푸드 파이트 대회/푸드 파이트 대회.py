def solution(food):
    answer = ''
    # 0번째 idx를 제외합니다.
    # 1번째부터 2로 나눈 몫 * 2만큼 idx를 string으로 연결합니다.
    # 다 끝나면 reverseString을 만든 후 사이에 0을 넣은채로 연결합니다.
    
    for idx in range(1, len(food)):
        foodCount = food[idx]
        
        answer += str(idx) * (foodCount // 2)
        
    return answer + '0' + answer[::-1]