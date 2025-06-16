from collections import deque
def solution(board):
    n = len(board)
    result = float("inf")
    
    # 방향 - 아래(0), 오른쪽(1), 위(2), 왼쪽(3)
    direction = [(1, 0, 0), (0, 1, 1), (-1, 0, 2), (0, -1, 3)]
    distance = [[[float("inf") for _ in range(n)] for _ in range(n)] for _ in range(4)]
    queue = deque([(0, 0, 0, 0), (0, 0, 0, 1)])

    while queue:
        x, y, cur_cost, cur_dir = queue.popleft()
        
        for dx, dy, next_dir in direction:
            nx = x + dx
            ny = y + dy
            
            if 0<= nx < n and 0<= ny < n and board[nx][ny] == 0:
                next_cost = cur_cost + 100
                
                if cur_dir != next_dir:     next_cost += 500
                
                if distance[next_dir][nx][ny] > next_cost:
                    distance[next_dir][nx][ny] = next_cost
                    if (nx, ny) == (n-1, n-1):  continue
                    
                    queue.append((nx, ny, next_cost, next_dir))
        
    for i in range(4):      result = min(result, distance[i][n-1][n-1])
    
    return result