from collections import deque
def solution(maps):
    result = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    maps = [[j for j in i] for i in maps]
    n, m = len(maps), len(maps[0])
    visited = set()
    
    def bfs(x, y, cnt):
        queue = deque([(x, y, cnt)])
        total_cnt = 0
        
        while queue:
            cx, cy, cur_cnt = queue.popleft()
            total_cnt += int(cur_cnt)
            
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny] != "X":
                    visited.add((nx, ny))
                    queue.append((nx, ny, maps[nx][ny]))
        
        return total_cnt
    
    for x, i in enumerate(maps):
        for y, val in enumerate(i):
            if maps[x][y] != "X" and (x, y) not in visited:
                visited.add((x, y))
                result.append(bfs(x, y, maps[x][y]))
    
    return sorted(result) if result else [-1]