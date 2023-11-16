// 속한 노래들의 총 재생 횟수가 많은 순으로 수록 2개
// 장르 내에서는 재생 횟수가 많은 노래 순으로 수록 2개
    // 재생 횟수가 같다면 고유 번호가 낮은 노래를 먼저 수록
    // 고유번호는 idx

function genreSort(a, b){
    const [aPlay, aIndex] = a;
    const [bPlay, bIndex] = b;
    
    if(aPlay != bPlay) return bPlay - aPlay;
    else return aIndex - bIndex;
}

function solution(genres, plays) {
    let answer = [];
    
    // 장르별로 [노래, 고유번호]를 취합
    const genreMap = new Map();
    
    for(let i = 0; i < plays.length; i++){
        genre = genres[i];
        play = plays[i];
        
        if(genreMap.has(genre)){
            genreMap.get(genre).push([play, i]);
        }else{
            genreMap.set(genre, [[play, i]]);
        }
    }
    
    // 장르별 배열에 정렬
    
    genreMap.forEach((item) => item.sort(genreSort));
    
    // 장르별 배열에 노래 횟수 취합
    
    genreCountMap = new Map();
    
    for(const [genre, songArr] of genreMap){
        genreCountMap.set(genre, songArr.reduce((acc, [play, idx]) => acc + play, 0));
    }
    
    return Array.from(genreCountMap.entries()).sort((a, b) => b[1] - a[1]).map(item => item[0]).map(genre => genreMap.get(genre).slice(0, 2).map(([play, idx]) => idx)).flat()
}