def solution(name):
    temp = {chr(val):idx if idx<=13 else 26-idx for idx, val in enumerate(list(range(65, 91)))}
    result = 0
    n = len(name)
    move = n - 1
    
    for idx, val in enumerate(name):
        result += temp[val]
        
        next_idx = idx + 1     # 오른쪽 방향으로 A가 안나올때까지 이동
        while next_idx < n and name[next_idx] == "A":
            next_idx += 1
            
        # 오른쪽으로 idx까지 이동
        # 0번째 인덱스에서 왼쪽으로 n - next_idx까지 이동 후 다시 후진
        right_move = idx + 2 * (n - next_idx)
        
        # 0번째 인덱스에서 idx까지 이동 후 다시 후진
        # 왼쪽으로 n - next_idx까지 이동
        left_move = 2 * idx + (n - next_idx)
        
        move = min(move, left_move, right_move)
    
    return result + move