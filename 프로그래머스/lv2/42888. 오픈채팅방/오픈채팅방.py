from collections import defaultdict

def solution(record):      
    answer = []
    
    nickname_list = defaultdict(lambda x: '')
    log_list = []
    
    for rec in record:
        act, *information = rec.split()
        
        if act == 'Enter' or act == 'Change':
            nickname_list[information[0]] = information[1]
        
        if act == 'Enter' or act == 'Leave':
            log_list.append([act, information[0]])
    
    for log in log_list:
        act, user = log
        
        if act == 'Enter':
            answer.append(nickname_list[user] + '님이 들어왔습니다.')
        else:
            answer.append(nickname_list[user] + '님이 나갔습니다.')
    
    return answer