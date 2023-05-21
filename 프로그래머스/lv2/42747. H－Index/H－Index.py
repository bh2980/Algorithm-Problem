def solution(citations):
    #전체 논문 중 h회 이상 인용된 논문이 h편 이상
    #역순으로 정렬
    #index를 증가시키면서
    #index + 1보다 
    citations.sort(reverse = True)
    
    for index in range(len(citations)):
        subscribe_count = citations[index]
        if index + 1 > subscribe_count:
            return  index
        
    return len(citations)