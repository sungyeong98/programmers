from collections import deque
def solution(maps):
    start, middle, end = 0, 0, 0
    maps = [[j for j in i] for i in maps]
    
    for i_idx, i in enumerate(maps):
        for j_idx, j in enumerate(i):
            if j == "S":    start = (i_idx, j_idx)
            if j == "L":    middle = (i_idx, j_idx)
            if j == "E":    end = (i_idx, j_idx)
    
    left_cnt = bfs(start, middle, maps)
    if left_cnt == -1:  return -1
    right_cnt = bfs(middle, end, maps)
    if right_cnt == -1: return -1

    return left_cnt + right_cnt
    
def bfs(start, end, maps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(start, 0)])
    visited = set()
    n, m = len(maps), len(maps[0])
    visited.add(start)
    result = float("inf")
    
    while queue:
        (x, y), cnt = queue.popleft()
        
        if (x, y) == end:   
            result = min(result, cnt)
            continue
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny] != "X":
                visited.add((nx, ny))
                queue.append(((nx, ny), cnt + 1))
    
    return result if result != float("inf") else -1