def solution(s):
    answer = []
    alphaDict = dict()
    
    # 사전에 알파벳이 없다면 알파벳의 idx를 추가하고 배열에는 -1을 추가합니다.
    # 사전에 알파벳이 있다면 배열에 내 idx - 알파벳 idx를 배열에 추가하고 알파벳의 idx를 내 idx로 업데이트합니다.
    
    for idx in range(len(s)):
        alpha = s[idx]
        
        if alpha in alphaDict:
            preIdx = alphaDict[alpha]
            answer.append(idx - preIdx)
            alphaDict[alpha] = idx
        else:
            answer.append(-1)
            alphaDict[alpha] = idx
            
    return answer