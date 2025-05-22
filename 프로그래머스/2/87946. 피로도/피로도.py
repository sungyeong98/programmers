from itertools import permutations
def solution(k, dungeons):
    result, n = 0, len(dungeons)
    
    for p in permutations(list(range(n)), n):
        cur_energy, cnt = k, 0
        for idx in p:
            need_energy, used_energy = dungeons[idx]
            if need_energy > cur_energy:
                break
            
            cur_energy -= used_energy
            cnt += 1
        result = max(result, cnt)
    return result