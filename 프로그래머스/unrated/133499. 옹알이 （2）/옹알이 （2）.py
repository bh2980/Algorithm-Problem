def solution(babbling):
    answer = 0
    
    baby_word = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        if(len(word) == 0):
            continue
            
        thisWordTwice = False
        
        for baby_w in baby_word:
            twice = baby_w + baby_w
            if twice in word:
                thisWordTwice = True
                break
        
        if thisWordTwice:
            continue
            
        for baby_w in baby_word:
            word = word.replace(baby_w, '_')
            
        if word == "_" * len(word):
            answer += 1
                
            
    return answer