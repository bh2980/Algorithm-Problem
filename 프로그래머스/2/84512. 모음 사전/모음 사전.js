// DFS는 맞는 것 같아요.
// A, E I O, U를 돌면서 
// for문 내부에서 count ++ -> 전역 변수

let count = 0;
let findTarget = false;

function makeStrDFS(target, string = ''){
    if(string.length === 5){
        return;
    };
    
    for(const char of ['A', 'E', 'I', 'O', 'U']){
        //string에 char 추가
        string += char;
        //count 추가
        count++;
        // console.log(`${count}번째 단어 :`, string);
        //검증
        if(string === target){
            findTarget = true;
            return;
        }else{
            makeStrDFS(target, string);
            
            if(findTarget) break;
        }
            // 성공 시 return
            // 실패 시 DFS
        //string에서 char 제거
        string = string.slice(0, string.length - 1);
    }
    
    return;
}

function solution(word) {
    makeStrDFS(word);
    
    return count;
}