def solution(s):
    s= s.split(' ')
    
    answer = []
    
    for word in s:
        word = list(word)
        for index in range(len(word)):
            if index % 2 == 0:
                word[index] = word[index].upper()
            else :
                word[index] = word[index].lower()
        
        answer.append(''.join(word))
         
    answer = ' '.join(answer)

    return answer