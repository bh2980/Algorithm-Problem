// h번 이상 인용된 논문이 h편 이상이면 h -> 최댓값

// 내림차순 정렬 후
// 처음부터 나까지의 개수가 나의 값보다 크거나 같은 값의 최대값

function solution(citations) {
    citations.sort((a, b) => b - a);
    
    let count = 0;
    
    for(let i = 0; i < citations.length; i++){
        const 인용횟수 = citations[i];
        const 논문개수 = i + 1;
        
        if(논문개수 > 인용횟수){
            return count;
        }else{
            count = 논문개수;
        }
    }
    
    return count;
}