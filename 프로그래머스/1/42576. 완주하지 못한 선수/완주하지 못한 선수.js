function solution(participant, completion) {
    let answer = '';
    
    // 정렬로 풀 수 있고
    // Map으로 풀 수 있음.
    
    partDict = new Map()
    
    for(const part of participant){
        if(partDict.has(part)){
            partDict.set(part, partDict.get(part)+1);
        }else{
            partDict.set(part, 1);
        }
    }
    
    for(const comp of completion){
        if(partDict.has(comp) && partDict.get(comp) > 0){
            partDict.set(comp, partDict.get(comp) - 1)
        }
    }
    
    for(const [key, value] of partDict){
        if(value !== 0) return key
    }
    
    return answer;
}