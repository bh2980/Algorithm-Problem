function validIndex(idx, arr){
    return idx % arr.length;
}

function solution(answers) {
    var answer = [];
    let first = Array.from({length: 5}, (_, i) => i + 1);
    let second = [2, 1, 2, 3, 2, 4, 2, 5];
    let third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let firstAnswer = 0;
    let secondAnswer = 0;
    let thirdAnswer = 0;
    
    for(let i = 0; i < answers.length; i++){
        const firstValidIdx = validIndex(i, first);
        const secondValidIdx = validIndex(i, second);
        const thirdValidIdx = validIndex(i, third);
        
        if(answers[i] === first[firstValidIdx]) firstAnswer++;
        if(answers[i] === second[secondValidIdx]) secondAnswer++;
        if(answers[i] === third[thirdValidIdx]) thirdAnswer++;   
    }
    
    maxValue = Math.max(firstAnswer, secondAnswer, thirdAnswer);
    
    if(maxValue === firstAnswer){
        answer.push(1);
    }
    
    if(maxValue === secondAnswer){
        answer.push(2);
    }
    
    if(maxValue === thirdAnswer){
        answer.push(3);
    }
    
    return answer;
}