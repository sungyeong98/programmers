from collections import deque
def solution(info, n, m):
    answer = float('inf')
    visited = set()
    
    queue = deque([(0, 0, 0)])
    
    while queue:
        a_cnt, b_cnt, idx = queue.popleft()
        
        if (a_cnt, b_cnt, idx) in visited:
            continue
        visited.add((a_cnt, b_cnt, idx))
        
        if idx == len(info):
            answer = min(answer, a_cnt)
            continue
        
        if a_cnt + info[idx][0] < n:
            queue.append((a_cnt + info[idx][0], b_cnt, idx + 1))
        if b_cnt + info[idx][1] < m:
            queue.append((a_cnt, b_cnt + info[idx][1], idx + 1))
    
    return answer if answer != float('inf') else -1