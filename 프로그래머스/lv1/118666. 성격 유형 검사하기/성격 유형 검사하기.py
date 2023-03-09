def solution(survey, choices):
    answer = ''
    types = dict([[char, 0] for char in 'RTCFJMAN'])
    
    for i in range(len(survey)):
        type1 = survey[i][0]
        type2 = survey[i][1]
        
        choice = choices[i] - 4
        
        if choice < 0:
            types[type1] += choice * -1
        else:
            types[type2] += choice
            
    types = list(types.items())
    
    for i in range(0, 8, 2):
        answer += types[i][0] if types[i][1] >= types[i+1][1] else types[i+1][0]
            
    return answer