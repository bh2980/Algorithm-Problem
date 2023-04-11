from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # 많이 플레이된 장르순 -> 장르 내에서 가장 많이 플레이된 노래 순으로 2개 수록
        # 같은 경우 idx가 작은 것부터 수록
    
    # 장르별 합산
    genre_dict = defaultdict(int)
    # 장르별 노래
    genre_song_dict = defaultdict(lambda : [])
    
    for i in range(len(plays)):
        genre = genres[i]
        song = i
        play = plays[i]
        
        genre_dict[genre] += play
        genre_song_dict[genre].append([song, play])
        
    # 장르별 순서 정렬
    for genre, song_list in genre_song_dict.items():
        genre_song_dict[genre] = [song_idx for song_idx, play in sorted(song_list, key = lambda x: -x[1])[:2]]
        
    print(genre_song_dict)

    for genre, play in sorted(list(genre_dict.items()), key = lambda x: -x[1]):
        answer += genre_song_dict[genre]
        
    return answer