from collections import defaultdict
def solution(genres, plays):
    music = defaultdict(list)
    cnt = defaultdict(int)
    result = []
    
    for idx, val in enumerate(genres):
        music[val].append((idx, plays[idx]))
        cnt[val] += plays[idx]
    
    
    
    for music_type in sorted(cnt.keys(), key=lambda x:-cnt[x]):
        music[music_type].sort(key=lambda x:(-x[1], x[0]))
        
        if len(music[music_type]) > 1:
            result.append(music[music_type][0][0])
            result.append(music[music_type][1][0])
        
        else:
            result.append(music[music_type][0][0])
    
    return result