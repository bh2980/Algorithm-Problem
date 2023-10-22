function solution(sizes) {
    var answer = 0;
    
    let max_width = 0;
    let max_height = 0;
    
    for (let i = 0; i < sizes.length; i++){
        let [width, height] = sizes[i];
        
        temp_width = Math.max(width, height);
        temp_height = Math.min(width, height);
        
        max_width = Math.max(temp_width, max_width);
        max_height = Math.max(temp_height, max_height);
    }
    
    return max_width * max_height;
}