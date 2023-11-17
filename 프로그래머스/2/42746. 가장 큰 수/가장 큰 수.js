function locationSort(a, b){
    const aStr = a.toString();
    const bStr = b.toString();
    
    return parseInt(bStr + aStr) - parseInt(aStr + bStr);
    
}

function solution(numbers) {
    const answer = numbers.sort(locationSort).join('').replace(/(^0+)/, '');
    return answer.length === 0 ? '0' : answer;
}