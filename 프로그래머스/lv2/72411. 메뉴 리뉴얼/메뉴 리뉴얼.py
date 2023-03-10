from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    combi_list = []
    
    for order in orders:
        for num in course:
            combi_list += list(set("".join(sorted(combi)) for combi in combinations(order, num)))
            
    combi_result = sorted(list([k, v] for k, v in Counter(combi_list).items() if v != 1), key = lambda x: (len(x[0]), -x[1]))
    
    prev_len = 0
    prev_max = 0
    
    for combi in combi_result:
        string, count = combi
        
        if prev_len != len(string):
            answer.append(string)
            prev_max = count
            prev_len = len(string)
        else:
            if prev_max == count:
                answer.append(string)
    
    return sorted(answer)