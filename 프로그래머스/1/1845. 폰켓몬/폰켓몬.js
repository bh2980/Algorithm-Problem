function solution(nums) {
    let answer = 0;
    
    const numSet = new Set(nums);
    
    return Math.min(numSet.size, parseInt(nums.length / 2));
}