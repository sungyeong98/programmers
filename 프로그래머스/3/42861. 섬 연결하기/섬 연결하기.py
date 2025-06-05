from heapq import heappush, heappop
from collections import defaultdict
def solution(n, costs):
    graph = defaultdict(list)   # 경로 및 비용 저장
    visited = set()             # 방문 여부 확인용
    result = 0                  # 결과
    
    for start, end, cost in costs:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
    
    temp = [(0, 0)]             # heap을 사용하여 경로 탐색
    
    while temp:
        cost, cur_node = heappop(temp)  # 비용이 저렴한 경로를 우선적으로 꺼내옴
        if cur_node in visited:         # 현재 노드가 이미 방문을 했다면 건너뛰기
            continue
        visited.add(cur_node)           # 현재 노드를 방문 처리
        result += cost                  # 결과에 현재 비용을 추가
        
        for next_cost, next_node in graph[cur_node]:
            if next_node not in visited:
                heappush(temp, (next_cost, next_node))
    return result              