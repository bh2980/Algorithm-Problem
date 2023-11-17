const print = console.log;

function numSort(a, b){
    return a - b;
}

function solution(array, commands) {
    let answer = [];
    
    for(const [start, end, order] of commands){
        answer.push([...array].slice(start - 1, end).sort(numSort)[order-1]);
    }
    
    return answer;
}