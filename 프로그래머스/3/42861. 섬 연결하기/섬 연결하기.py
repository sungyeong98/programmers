from heapq import heappush, heappop
from collections import defaultdict
def solution(n, costs):
    graph = defaultdict(list)
    visited = set()
    result = 0
    
    for start, end, cost in costs:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
    
    temp = [(0, 0)]
    
    while temp:
        cost, cur_node = heappop(temp)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        result += cost
        
        for next_cost, next_node in graph[cur_node]:
            if next_node not in visited:
                heappush(temp, (next_cost, next_node))
    return result              