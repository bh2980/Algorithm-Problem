const print = console.log;

function top(arr){
    if(arr.length === 0) return 0;
    return arr[arr.length - 1].price;
}

function solution(prices) {
    let answer = Array.from({length: prices.length}).fill(-1);
    let stack = [];
    
    // 1초씩 증가시키면서 넣을때의 시간을 넣고 -> idx로 사용
    for(let idx = 0; idx < prices.length; idx++){
        const currentPrice = prices[idx];
        
        if(top(stack) > currentPrice){ // stack top 가격이 넣을 가격보다 높다면
            // 가격이 같아질 때까지 뺀다.
            while(top(stack) > currentPrice){
                const {price, time} = stack.pop();
                
                // print(`${price}는 ${time}초에 가격이고 ${currentPrice}보다 큽니다.`);
                // print(`유지기간은 ${idx - time}초입니다.`);
                
                answer[time] = idx - time;
            }
        }
        
        stack.push({ price: currentPrice, time: idx });
    }
    
    const totalTime = answer.length - 1;
    
    while(stack.length > 0){
        const {price, time} = stack.pop();
                
        // print(`${price}는 ${time}초에 가격입니다.`);
        // print(`유지기간은 ${totalTime - time}초입니다.`);
        
        answer[time] = totalTime - time;
    }
    
    return answer;
}