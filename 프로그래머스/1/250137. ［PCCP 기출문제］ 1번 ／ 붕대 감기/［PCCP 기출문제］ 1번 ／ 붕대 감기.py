from collections import deque
def solution(bandage, health, attacks):
    time = 0    # 현재 시간
    cnt = 0     # 연속 성공 시간
    max_health = health
    need_time, heal_for_sec, bonus_heal = bandage
    a = deque(attacks)
    
    while health > 0:
        if not a:
            return health
        
        time += 1
        
        if a[0][0] == time:
            _, damage = a.popleft()
            health -= damage
            cnt = 0
        else:
            health = min(max_health, health + heal_for_sec)
            cnt += 1
            if cnt == need_time:
                health = min(max_health, health + bonus_heal)
                cnt = 0
    
    return -1