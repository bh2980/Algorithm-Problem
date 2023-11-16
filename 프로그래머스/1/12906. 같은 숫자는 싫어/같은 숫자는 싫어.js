function top(arr){
    if(arr.length === 0){
        return null;
    }
    
    return arr[arr.length - 1];
}

function solution(arr)
{
    const answer = [];
    
    for(const num of arr){
        if(top(answer) !== num) answer.push(num)
    }
    
    return answer;
}