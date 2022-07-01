from itertools import combinations

def solution(skill, skill_trees):
    skill_set = set([char for char in skill])
    count = 0

    for tree in skill_trees:
        order = ''.join([char for char in tree if char in skill_set])
        
        if skill.startswith(order):
            count += 1
            
    return count