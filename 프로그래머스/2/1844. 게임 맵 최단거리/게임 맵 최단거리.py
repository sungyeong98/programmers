from collections import deque
def solution(maps):
    # dir = 4방향으로 이동할 수 있게 도와주는 방향 리스트
    n, m, dir = len(maps), len(maps[0]), [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # queue = bfs를 위한 큐
    # visited = 방문 여부를 등록하기 위한 리스트
    queue, visited = deque([(0, 0, 1)]), [[False]*m for _ in range(n)]
    # 시작 지점을 방문한 상태로 변경
    visited[0][0] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        # 현재 좌표가 도착 지점이면 반환
        if x == n-1 and y == m-1:
            return cnt
        
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]==1:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

    return -1