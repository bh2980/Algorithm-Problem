let maxCount = 0;

function exploreDFS(dungeons, k, currentIdx = 0, count = 0, visited = new Set()){
    if(maxCount === dungeons.length) return;
    
    // console.log(`현재까지 탐사한 던전 ${count}개 / 현재 피로토 ${k}`)
    //재귀적으로 for문을 돌려 탐색함.
    for(let i = 0; i < dungeons.length; i++){
        if(visited.has(i)) continue;
        
        const [minNeed, consume] = dungeons[i];
        
        if(k < minNeed) {
            // console.log(`${i}번째 던전 탐사 불가 / 필요 피로도 ${minNeed}`)
            continue
        };
        
        // console.log(`${i}번째 던전 탐사 / 소모 피로도 ${consume} / 남은 피로도 ${k - consume}`);
        k -= consume;
        visited.add(i);
        exploreDFS(dungeons, k, i + 1, count + 1, visited);
        k += consume;
        visited.delete(i);
    }
    //하나를 돌 때마다 count ++;
    //더 이상 돌 수 있는 던전이 없다면 maxCount 업데이트
    //만약 모든 던전을 다 돌 수 있는 경우가 나오면 바로 return하는 최적화
    
    maxCount = Math.max(count, maxCount);
    
    // console.log()
    
    return;
}

function solution(k, dungeons) {
    exploreDFS(dungeons, k);
    
    return maxCount;
}