# 모든 후보키가 될 수 있는 조합을 추출한다

# 유일성 검증
# 조합별로 후보키가 될 수 있는지 검증한다.
# 후보키가 될 수 있다면 후보키 리스트에 넣는다.

answer = 0
total_att_set = set()

def checkUnique(att_set, relation):
    ROW_COUNT = len(relation)
    element_set = set([tuple([relation[i][j] for j in att_set]) for i in range(ROW_COUNT)])
    
    return len(element_set) == ROW_COUNT

def recursiveDFS(start, att_count, relation, att_list):
    global answer, total_att_list

    # 성분을 하나씩 포함해서 조합을 만듬
    for idx in range(start, att_count):
        att_list.append(idx)

        # 유일성 파악
        is_unique = checkUnique(att_list, relation)

        # 유일성을 만족하는 순간 재귀를 호출하지 않고, 다음 차례로 넘어감.
        if is_unique:
            temp_set = set(att_list)
            remove_list = []
            
            for att_set in total_att_set:
                if temp_set < set(att_set):
                    remove_list.append(att_set)
                    
            for remove_att in remove_list:
                total_att_set.remove(remove_att)
            
            total_att_set.add(tuple(temp_set))
            
        # 유일성을 만족하지 않으면 계속 재귀
        else:
            recursiveDFS(idx + 1, att_count, relation, att_list)

        att_list.pop()
        
    return

def solution(relation):
    # 유일성과 최소성을 만족하여야한다.
    
    # 후보키의 최대 개수
    
    # 유일성 판별법
    # relation을 읽어서 tuple로 set에 넣고, 길이를 센다.
    # 길이가 relation의 행의 길이와 같다면, 유일성 만족
    
    # 최소성 판별법
    # 후보키를 포함하는 다른 후보키를 포함하지 않는다.
    
    # 재귀로 계속 돌면서 후보키를 DFS 해간다.
    # 만약 해당 키가 후보키를 만족한다면 이 키에 추가되는 것은 최소성을 만족하지 못하므로
        # 더 이상 DFS를 하지 않고 같은 레벨의 다음 것으로 넘어간다. 
        # 최소성 필터링
    # 조합을 백트래킹으로 풀면 된다.
    
    global answer, total_att_list
    
    att_count = len(relation[0])
    
    recursiveDFS(0, att_count, relation, [])

    return len(total_att_set)

