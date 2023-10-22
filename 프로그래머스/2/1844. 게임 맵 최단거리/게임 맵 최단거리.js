// 상대팀 진영에 도착할 수 없는 경우를 파악해야함.
// 모든 곳을 다 했는데 도착하지 않으면 fail

var N, M;
var WALL = 0;
var BLANK = 1;

function inRange(r, c){
    return 0 <= r && r < N && 0 <= c && c < M;
}

function not(input){
    return !input;
}

function makeKeyFromRC(r, c){
    return `${r}-${c}`;
}

function BFS(maps){
    const queue = [[0, 0]];
    const visitedSet = new Set();
    
    visitedSet.add(makeKeyFromRC(0, 0));
    
    const drs = [-1, 0, 1, 0];
    const dcs = [0, -1, 0, 1];
    
    let length = 1;
    let count = 0;
    
    while(queue.length > 0){
        const [cr, cc] = queue.shift();
        length--;
        
        if(cr === N - 1 && cc === M - 1){
            return count + 1;
        }
        
        for(let i = 0; i < 4; i++){
            const dr = drs[i];
            const dc = dcs[i];
            
            const nr = cr + dr;
            const nc = cc + dc;
            
            if(inRange(nr, nc) && maps[nr][nc] != WALL && not(visitedSet.has(makeKeyFromRC(nr, nc)))){
                visitedSet.add(makeKeyFromRC(nr, nc));
                queue.push([nr, nc]);
            }
        }
        
        if(length === 0){
            count++;
            length = queue.length;
        }
    }
    
    return -1;
}

function solution(maps) {
    var answer = 0;
    N = maps.length;
    M = maps[0].length;
    
    answer = BFS(maps);
    
    return answer;
}