// 각 기능은 진도가 100일 때 배포
// 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 가능
// 뒤에 있는 기능은 앞에 있는 기능과 같이 배포되어야함.

// 각 배포마다 몇 개의 기능이 배포되는지 배열로 return

const print = console.log;

function solution(progresses, speeds) {
    let answer = [];
    
    //progresses가 비워질 때까지 반복
    
    //첫 번째 원소의 개발이 끝날때까지 걸리는 시간을 구한다. +1
    //나머지 원소를 돌면서 작업률을 계산
        // 작업률이 100이 넘어가면 +1
        // 작업률이 100이 안 넘어가면 break
    
    progresses.reverse()
    speeds.reverse()
    
    while(progresses.length > 0){
        let jobCount = 0;
        
        const firstJob = progresses.pop();
        const firstSpeed = speeds.pop();
        
        jobCount++;
        
        
        const reqDay = Math.ceil((100 - firstJob) / firstSpeed)
        
        print(firstJob, firstSpeed, reqDay);
        
        while(progresses[progresses.length - 1] + speeds[progresses.length - 1] * reqDay >= 100){
            progresses.pop();
            speeds.pop();
            jobCount++;
        }
        
        for(let i = 0; i < progresses.length; i++){
            progresses[i] += speeds[i] * reqDay;
        }
        
        answer.push(jobCount);
    }
    
    
    return answer;
}