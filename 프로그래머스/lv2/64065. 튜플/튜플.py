# string으로 들어오기 때문에 먼저 int의 집합으로 만들어줘야한다.
# 당장은 효율적으로 하는 방법이 떠오르지 않기 떄문에 무식하게 해보자
# 각 집합으로 만들었다면, 길이순으로 정렬한다
# 길이가 작은 것부터 기존과 여집합을 구하여 answer에 차례대로 쌓는다.

def solution(s):
    answer = []
    
    num_list = []
    use_num_set = set()
    
    for num_string in s[2:len(s) - 2].split('},{'):
        num_list.append(set(map(int, num_string.split(','))))
    
    num_list.sort(key = lambda x: len(x))
    
    for num_set in num_list:
        left_element = ((num_set | use_num_set) - (num_set & use_num_set)).pop()
        
        use_num_set.add(left_element)
        answer.append(left_element)
        
    return answer