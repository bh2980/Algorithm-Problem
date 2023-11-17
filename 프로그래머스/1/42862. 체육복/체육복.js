function solution(n, lost, reserve) {
    if(lost.length === 0 || reserve.length === n) return n;
    
    lost.sort();
    reserve.sort();
    
    // lost는 set으로 찾기 쉽게
    // reserve한 학생을 대상으로 -1 -> +1 순으로 체육복 여부를 탐색해가며 제거
    // 여벌 체육복을 가진 학생이 도난 당한 경우 1개만 가지고 있는 것으로 간주 !!!
    // intersection을 계산해서 제거
    
    lost = new Set(lost);
    reserve = new Set(reserve);
    
    const newLost = new Set([...lost].filter(student => !reserve.has(student)));
    const newReserve = new Set([...reserve].filter(student => !lost.has(student)));
    
    lost = newLost;
    reserve = newReserve;
    
    let participants = n - lost.size;
    
    for(const res of reserve){
        if(lost.has(res)){
            lost.delete(res);
            participants++;
            continue;
        }
        
        const prevStudent = res - 1;
        const nextStudent = res + 1;
        
        if(0 < prevStudent && lost.has(prevStudent)){
            lost.delete(prevStudent);
            participants++;
            continue;
        }
        
        if(nextStudent <= n && lost.has(nextStudent)){
            lost.delete(nextStudent);
            participants++;
        }
    }
    
    return participants;
}