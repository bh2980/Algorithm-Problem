// 홀수면 1이면 return 짝수면 0이면 return하도록 최적화 가능
// 일단 전체 그래프를 만든다
// for문으로 돌면서 하나를 끊는다
// 계산한다
// 업데이트 한다
// 다시 복구한다.

function printGraph(graph){
    for(const line of graph){
        console.log(line);
    }
}

function setWire(r, c, graph){
    graph[r-1][c-1] = 1;
    graph[c-1][r-1] = 1;
}

function cutWire(r, c, graph){
    graph[r-1][c-1] = 0;
    graph[c-1][r-1] = 0;
}

function exploreBFS(graph, startNode){
    const visitedSet = new Set([startNode]);
    let treeNodeCount = 0;
    
    let queue = [startNode];
    
    while(queue.length > 0){
        const popNode = queue.shift();
        
        treeNodeCount++;
        
        for(let i = 0; i < graph[popNode].length; i++){
            if(!visitedSet.has(i) && graph[popNode][i] === 1){
                visitedSet.add(i);
                queue.push(i);
            }
        }
    }
    
    return [treeNodeCount, visitedSet];
}

function calcGraphNode(nodeCount, graph, visited = new Set()){
    // node를 0부터 끝까지 탐색해가면서 시작점으로 삼는다
    
    let firstTreeNodeCount = 0;
    
    for(let i = 0; i < nodeCount; i++){
        if(visited.has(i)) continue;
        
        const [nodeCount, visitedNodeSet] = exploreBFS(graph, i);
        
        // console.log(nodeCount, visitedNodeSet)
        
        visited = new Set([...visited, ...visitedNodeSet]);
        
        if(firstTreeNodeCount === 0) firstTreeNodeCount = nodeCount;
        else return Math.abs(firstTreeNodeCount - nodeCount)
    }
    // 각 node를 시작으로 BFS
    // 개수와 방문 여부를 return 받아서 visited에 등록
    // visited에 있는 노드를 제외하고 다시 BFS
    // 최종 개수의 차를 return
    
    return firstTreeNodeCount;
}

function solution(n, wires) {
    // 전체 그래프를 그린다.
    // 어떻게 그릴까?
    // Map을 통해, arr를 통해
    // 전선을 끊을 때는 arr가 편함.
    // 노드 최댓값을 알아야한다.
    
    const nodeCount = Math.max(...wires.flat());
    const graph = Array.from({length: nodeCount}, () => Array.from({length: nodeCount}).fill(0));
    
    let minNodeDiff = Infinity;
    
    for(const [r, c] of wires){
        setWire(r, c, graph);
    }
    
    for(const [r, c] of wires){
        cutWire(r, c, graph);
        
        minNodeDiff = Math.min(minNodeDiff, calcGraphNode(nodeCount, graph));
        
        if(nodeCount % 2 === 0 && minNodeDiff === 0) return 0;
        else if(nodeCount % 2 === 1 && minNodeDiff === 1) return 1;
        
        setWire(r, c, graph);
    }
    
    
    return minNodeDiff;
}