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
    
    unshift(value){
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
    
    shift(){
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
    
    print(callback = (node) => node.value, end = ', '){
        let node = this.start;
        
        process.stdout.write('[');
        
        while(node){
            if(isNull(node.next)) end = '';
            
            process.stdout.write(node.value.weight.toString() + end);
            node = node.next;
        }
        
        process.stdout.write(']');
        console.log();
    }
    
    top(){
        if(this.size <= 0) throw Error('queue가 비었습니다.');
        
        return this.start.value;
    }
    
    *[Symbol.iterator]() {
        let node = this.start;

        while (node) {
            yield node.value;
            node = node.next;
        }
    }
}

class Truck{
    constructor(weight){
        this.weight = weight;
        this.dis = 1;
    }
    
    move(){
        this.dis++;
    }
}

function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    
    const bridge = new Deque([]);
    truck_weights = new Deque(truck_weights);
    
    const TRUCK_COUNT = truck_weights.size;
    let passTruckCount = 0;
    let bridgeWeight = 0;
    
    //다리를 지난 트럭이 대기 트럭의 길이와 같아질 때까지 반복한다.
    while(passTruckCount < TRUCK_COUNT){
        // move 후 첫 번째 원소 값을 보면서 다리의 길이와 같다면 pop
        while(bridge.size > 0 && bridge.top().dis > bridge_length){
            const truck = bridge.shift();
            passTruckCount++;
            bridgeWeight -= truck.weight;
        }
        
        // 무게 재기
        // 대기 첫 트럭을 다리에 올릴 수 있다면 다리에 트럭을 하나 올림
        if(truck_weights.size > 0 && bridgeWeight + truck_weights.top() <= weight){
            const truckWeight = truck_weights.shift();
            bridge.push(new Truck(truckWeight));
            bridgeWeight += truckWeight;
        }
        
        // 다리 위에 있는 모든 트럭에게 move
        for(const truck of bridge){
            truck.move();
        }
        
        // bridge.print()
        // console.log()
        
        answer++;
        
        // 반복
    }
    
    return answer;
}