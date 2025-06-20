from collections import deque, defaultdict
def solution(land):
    n, m = len(land), len(land[0])
    oil = defaultdict(int)
    visited = set()
    
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and land[i][j] == 1:
                visited.add((i, j))
                bfs(i, j, land, visited, oil, n, m)

    return max(oil.values()) if oil else 0

def bfs(x, y, land, visited, oil, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    temp = set([y])
    start_cnt = len(visited)
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and land[nx][ny] == 1:
                visited.add((nx, ny))
                queue.append((nx, ny))
                temp.add(ny)
                
    cnt = len(visited) - start_cnt + 1

    for col in temp:
        oil[col] += cnt