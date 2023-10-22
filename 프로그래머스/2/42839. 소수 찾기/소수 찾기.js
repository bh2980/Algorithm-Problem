function combinations(list, count){
    if(count === 1){
        return list.map(item => [item]);
    }
    
    const totalCombiList = [];
    
    for(let i = 0; i < list.length; i++){
        const fixedElement = list[i];
        
        exceptList = [...list].slice(i + 1);
        combiList = combinations(exceptList, count - 1);
        
        for(let j= 0; j < combiList.length; j++){
            totalCombiList.push([fixedElement, ...combiList[j]]);
        }
    }
    
    return totalCombiList;
}

function permutations(list, count){
    if(count === 1){
        return list.map(item => [item]);
    }
    
    const totalPermuList = [];
    
    for(let idx = 0; idx < list.length; idx++){
        const fixedElement = list[idx];
        
        const tempList = [...[...list].slice(0, idx), ...[...list].slice(idx + 1)];
        const permuList = permutations(tempList, count - 1);
        for(let j = 0; j < permuList.length; j++){
            totalPermuList.push([fixedElement, ...permuList[j]])
        }
    }
    
    return totalPermuList;
}

function checkSosu(number){
    if(number === 0 || number === 1){
        return false;
    }
    
    const limit = parseInt(Math.sqrt(number)) + 1;
    
    for(let i = 2; i < limit; i++){
        if(number % i === 0){
            return false;
        }
    }
    
    return true;
}

function solution(numbers) {
    var answer = 0;
    
    const numCharList = Array.from(numbers);
    const mySet = new Set();
    
    for(let count = 1; count < numCharList.length + 1; count++){
        const permuList = permutations(numCharList, count);
        
        for(const permu of permuList){
            const myNum = parseInt(permu.join(''));
            
            if(checkSosu(myNum)){
                mySet.add(myNum);
            }
        }
    }
    
    return mySet.size;
}