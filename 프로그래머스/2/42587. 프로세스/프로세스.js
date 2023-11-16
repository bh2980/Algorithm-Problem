function not(value){
    return !value;
}

function isNull(value){
    return value === undefined || value === null;
}

class Node{
    constructor(value, prev = null, next = null){
        this.value = value;
        this.prev = prev;
        this.next = next;
    }
}

class Deque{
    constructor(list = []){
        this.start = null;
        this.end = null;
        this.size = 0;
        
        for (const value of list) {
            this.push(value);
        }
    }
    
    push(value){
        const newNode = new Node(value);
        const lastNode = this.end;
        this.size++;
        
        if(isNull(lastNode)){
            this.start = newNode;
            this.end = newNode;
        }else{
            this.end = newNode;
            lastNode.next = newNode;
            newNode.prev = lastNode;
        }
    }
    
    pop(){
        if(this.size <= 0){
            throw Error('[E]queue에 원소가 없습니다.')
        }
        
        const lastNode = this.end;
        const willLastNode = lastNode.prev;
        
        if(isNull(willLastNode)){
            this.start = null;
            this.end = null;
        }else{
            this.end = willLastNode;
            willLastNode.next = null;
        }
        
        this.size--;
        
        return lastNode.value;
    }
    
    pushleft(value){
        const newNode = new Node(value)
        const firstNode = this.start;
        
        this.size++;
        
        if(isNull(firstNode)){
            this.start = newNode;
            this.end = newNode;
        }else{
            //첫번째 노드를 두 번째로
            this.start = newNode;
            newNode.next = firstNode;
            firstNode.prev = newNode;
        }
    }
    
    popleft(){
        if(this.size <= 0) throw Error('[E] queue가 비었습니다.');
        
        const firstNode = this.start;
        const willFirstNode = firstNode.next;
        
        if(isNull(willFirstNode)){
            this.start = null;
            this.end = null;
        }else{
            this.start = willFirstNode;
            willFirstNode.prev = null;   
        }
        
        this.size--;
        
        return firstNode.value;
    }
    
    print(end = ', '){
        let node = this.start;
        
        process.stdout.write('[');
        
        while(node){
            if(isNull(node.next)) end = '';
            
            process.stdout.write(node.value.toString() + end);
            node = node.next;
        }
        
        process.stdout.write(']');
        console.log();
    }
    
    *[Symbol.iterator]() {
        let node = this.start;

        while (node) {
            yield node.value;
            node = node.next;
        }
    }
}

function solution(priorities, location) {
    let answer = 0;
    let maxPri = Math.max(...priorities);
    let processCount = 0;
    
    const queue = new Deque(priorities);
    
    itsMe = false;
    
    // 최대 우선순위 기록
    while(queue.size > 0){
        // 앞에서부터 하나씩 뺀다.
        const job = queue.popleft();
        
        console.log('뺀 작업 우선순위: ', job);
        
        // 뺄 때마다 idx --
        location--;
        console.log('idx 갱신 :', location);
        
        // 만약 idx가 음수라면 현재 나온 상태
        if(location < 0) itsMe = true;
        console.log('목표인가?', itsMe);
        
        // 최대 우선순위와 내가 같다면 throw
        if(job === maxPri){
            processCount++;
            console.log('프로세스 실행')
            if(itsMe) return processCount;
            // 최대 우선순위 갱신
            maxPri = Math.max(...queue);
            console.log('최대 우선순위 갱신:', maxPri);
        }else{
            // 아니라면 뒤로 다시 넣음
            queue.push(job);
            // 만약 내가 나왔다면, idx를 길이 - 1로 갱신
            if(itsMe){
                location = queue.size - 1;
                console.log('idx 갱신 :', location);
                itsMe = false;
            }
        }
        
        queue.print()
    }
    
    return answer;
}