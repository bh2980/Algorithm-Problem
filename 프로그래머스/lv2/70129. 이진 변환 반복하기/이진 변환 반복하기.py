def solution(s):
    # remove all zero
    # make length to binary string
    # repeat until be 1
    
    # [count binary translation, count remove zero]
    
    count_transform = 0
    count_zero = 0
    
    while s != "1":
        old_length = len(s)

        s = s.replace("0", "")
        remove_zero_length = len(s)
        
        count_zero += old_length - remove_zero_length
        
        s = bin(len(s))[2:]
        
        count_transform += 1
        
    return [count_transform, count_zero]