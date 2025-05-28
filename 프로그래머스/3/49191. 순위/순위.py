def solution(n, results):
    temp = [[float("inf")]*n for _ in range(n)]
    
    for i in range(n):
        temp[i][i] = 0          # 자기 자신은 0으로 처리
    
    for a, b in results:
        temp[a-1][b-1] = 1      # 승리
        temp[b-1][a-1] = -1     # 패배
    
    # Floyd-Warshall Algorithm
    for k in range(n):          # 새 정점  
        for i in range(n):      # 시작 노드
            for j in range(n):  # 끝 노드
                if temp[i][k] == 1 and temp[k][j] == 1:
                    temp[i][j] = 1
                    temp[j][i] = -1
    
    return n - sum([1 if float("inf") in i else 0 for i in temp])