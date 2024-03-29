from collections import defaultdict

stack = []

def DFS(current, tickets, level, n):
    global stack
    
    if level >= n:
        #n개되면 stack return
        return stack
    
    if current not in tickets:
        #level이 n보다 작은 데 막다른 공항이면, 실패
        return False
    
    for arrive in tickets[current].keys():#도착지를 가져와서
        if tickets[current][arrive] != 0:#도착지로 향하는 티켓이 남아 있다면(0개가 아니면)
            stack.append(arrive)#stack에 넣고
            tickets[current][arrive] -= 1 #항공권 소비

            if DFS(arrive, tickets, level + 1, n):
                #DFS 결과가 stack(True)면 그만하고 return, 도달하지 못해서 False면 밑으로
                return stack

            tickets[current][arrive] += 1 #도달하지 못했으므로 항공권 다시 복구
            stack.pop()#stack에서 제거
            
    return False

def makeDict(tickets):
    tickets_dict = defaultdict(lambda: defaultdict(int))
    
    for depart, arrive in tickets:
        tickets_dict[depart][arrive] += 1
        
    for key, value in tickets_dict.items():#내부 사전의 key값에 따라 정렬
        tickets_dict[key] = dict(sorted(value.items(), key=lambda x:x[0]))
        
    return tickets_dict

def solution(tickets):
    #DFS
    #사전순으로 정렬 후 호출
    #모든 티켓을 사용하면 print하고 종료
    #dict(ICN : dict([ATL : 1], [SFO : 2]))
    n = len(tickets) + 1

    tickets = makeDict(tickets)
    
    stack.append('ICN')
    answer = DFS('ICN', tickets, 1, n)
    
    return answer