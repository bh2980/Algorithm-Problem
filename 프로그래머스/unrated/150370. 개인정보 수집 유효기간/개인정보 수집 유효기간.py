from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    
    t_year, t_month, t_date = map(int, today.split('.'))
    
    terms_detail = defaultdict(int)
    
    for term in terms:
        policy, due_month = map(lambda x: x if x.isalpha() else int(x), term.split())
        terms_detail[policy] = due_month * 28
        
    for i in range(len(privacies)):
        privacy = privacies[i]
        start_day, term = privacy.split()
        year, month, date = map(int, start_day.split('.'))
        
        diff_year = t_year - year
        diff_month = t_month - month
        diff_date = t_date - date
        
        total_diff = diff_year * 28 * 12 + diff_month * 28 + diff_date
        
        if total_diff >= terms_detail[term]:
            answer.append(i+1)
    
    return answer