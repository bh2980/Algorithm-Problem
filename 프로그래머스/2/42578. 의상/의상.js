function solution(clothes) {
    clothMap = new Map();
    
    for(const [name, type] of clothes){
        if(clothMap.has(type)) clothMap.set(type, clothMap.get(type) + 1);
        else clothMap.set(type, 1);
    }
    
    const kindArr = Array.from(clothMap.values());
    
    return kindArr.reduce((acc, cur) => {
        return acc * (cur + 1)
    }, 1) - 1;
}