idx = 0
find_idx = -1

def recursiveFindWordIdx(word, char_list = []):
    global idx
    global find_idx
    
    if ''.join(char_list) == word:
        find_idx = idx
        
        return
    
    if len(char_list) < 5:
        for char in ['A', 'E', 'I', 'O', 'U']:
            if find_idx > 0:
                break
                
            char_list.append(char)
            idx += 1
            recursiveFindWordIdx(word, char_list)
            char_list.pop()

    return

def solution(word):
    global find_idx
    
    recursiveFindWordIdx(word)
    
    return find_idx