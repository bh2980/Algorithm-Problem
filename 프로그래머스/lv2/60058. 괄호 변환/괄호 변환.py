from collections import Counter

def makeUV(string):
    left_p = 0
    right_p = 0
    total_l, total_r = Counter(string).values()
    
    for i in range(len(string)):
        if string[i] == '(':
            left_p += 1
        else:
            right_p += 1
        
        if left_p == right_p and (total_l - left_p == total_r - right_p):
            return [string[:i+1], string[i+1:]]
        
def isRightPar(p):
    is_right = 0
    
    for char in p:
        if char == '(':
            is_right += 1
        else:
            is_right -= 1
        
        if is_right < 0:
            return False
    
    return True

def reverseU(u):
    string = ''
    
    for char in u[1:-1]:
        if char == '(':
            string += ')'
        else:
            string += '('
    
    return string

def solution(p):
    if p == '':
        return ''
    
    u, v = makeUV(p)

    if isRightPar(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverseU(u)