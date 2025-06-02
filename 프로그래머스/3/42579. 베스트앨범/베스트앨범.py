from collections import defaultdict
def solution(genres, plays):
    music = defaultdict(list)       # 음악을 저장할 딕셔너리
    cnt = defaultdict(int)          # 장르별 재생 수를 저장할 딕셔너리
    result = []
    
    for idx, val in enumerate(genres):
        music[val].append((idx, plays[idx]))    # 인덱스, 재생 수를 튜플로 저장
        cnt[val] += plays[idx]
    
    for music_type in sorted(cnt.keys(), key=lambda x:-cnt[x]): # 장르별 재생수가 가장 많은 것부터 for문 순회
        music[music_type].sort(key=lambda x:(-x[1], x[0]))  # 특정 장르의 음악을 재생 수 desc, 인덱스 asc 정렬
        
        if len(music[music_type]) > 1:  # 장르의 음악수가 2개 이상이면 result에 상위 2개의 음악을 저장
            result.append(music[music_type][0][0])  
            result.append(music[music_type][1][0])
        
        else:   # 아니면 1개만 저장 (0개는 존재하지 않음)
            result.append(music[music_type][0][0])
    
    return result