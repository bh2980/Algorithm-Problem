var count = 0;

function DFS(numList, targetNumber, idx = 0, totalSum = 0){
    // console.log(`idx : ${idx} / totalSum : ${totalSum}`);
    
    if(idx == numList.length){
        // console.log('다 돌았다', totalSum);
        
        if(totalSum === targetNumber){
            count++;
        }
        
        return;
    }
    
    const charArr = [+1, -1];
    
    for(const char of charArr){
        const newNum = numList[idx] * char;
        
        totalSum += newNum;
        DFS(numList, targetNumber, idx + 1, totalSum);
        totalSum -= newNum;
    }
    
    return;
}

function solution(numbers, target) {
    DFS(numbers, target);
    return count;
}