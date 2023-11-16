function solution(s){
    let stack = 0;
    
    s = s.replace('()', '')
    
    for(const char of s){
        if(char === '('){
            stack++;
        }else{
            if(stack > 0){
                stack--;
            }else{
                return false;
            }
        }
    }

    return stack === 0 ? true : false;
}