# 자카드 유사도 측정
# 문자열1과 문자열2를 2글자씩 끊어서 집합의 원소로 만든다.
    # 영문으로 된 글자 쌍만 유효하고, 공백, 숫자, 특수문자가 포함된 문자쌍은 버린다.
    # 대소문자 차이는 무시한다.
# 자카드 유사도 = 교집합 개수 / 합집합 개수
    # 중복 원소를 하나로 처리하지 않는다.
        
# 유사도 값에 65536을 곱해 return한다.

import re
# 하나의 문자열에서 두 글자씩 끊어서 문자쌍을 만드는 함수
def makeCharList(string):
    arr = []
    
    charRegex = re.compile('^[A-Za-z]+$')
    
    for idx in range(len(string) - 1):
        char1 = string[idx]
        char2 = string[idx + 1]
        
        substring = (char1 + char2).lower()
        
        if charRegex.match(substring):
            arr.append(substring)
    
    return sorted(arr)
    
# 교집합을 만드는 함수 -> 중복 허용
def intersect(arr1, arr2):
    intersectArr = []
    
    p1, p2 = 0, 0
    
    while p1 < len(arr1) and p2 < len(arr2):
        elm1 = arr1[p1]
        elm2 = arr2[p2]
        
        if elm1 == elm2:
            intersectArr.append(elm1)
            
            p1 += 1
            p2 += 1
        elif elm1 < elm2:
            p1 += 1
        else:
            p2 += 1
            
    return intersectArr

# 합집합을 만드는 함수 -> 중복 허용
def union(arr1, arr2):
    p1, p2 = 0, 0
    
    unionArr = []
    
    while p1 < len(arr1) and p2 < len(arr2):
        elm1 = arr1[p1]
        elm2 = arr2[p2]
        
        if elm1 == elm2:
            unionArr.append(elm1)
            
            p1 += 1
            p2 += 1
        elif elm1 < elm2:
            unionArr.append(elm1)
            p1 += 1
        else:
            unionArr.append(elm2)
            p2 += 1
            
    if p1 < len(arr1):
        for elm in arr1[p1: len(arr1)]:
            unionArr.append(elm)
    
    if p2 < len(arr2):
        for elm in arr2[p2: len(arr2)]:
            unionArr.append(elm)
            
    return unionArr
    

# 자카드 유사도를 구하는 함수
def makeJacardSimilarity(str1, str2):
    str1Arr = makeCharList(str1)
    str2Arr = makeCharList(str2)
    
    unionArr = union(str1Arr, str2Arr)
    intersectArr = intersect(str1Arr, str2Arr)
    
    if len(unionArr) == 0:
        return 1
    
    return len(intersectArr) / len(unionArr)

def solution(str1, str2):
    answer = int(makeJacardSimilarity(str1, str2) * 65536)
    
    return answer