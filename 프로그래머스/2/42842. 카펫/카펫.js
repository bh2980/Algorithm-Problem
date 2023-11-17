function calcYaksu(num, yellow){
    const arr = [];
    
    for(let i = 1; i < parseInt(Math.pow(num, 0.5)) + 1; i++){
        if((i - 2) * ((num / i) - 2) === yellow) return [num/i, i];
    }
    
    return null;
}

function solution(brown, yellow) {
    return calcYaksu(brown+yellow, yellow)
}