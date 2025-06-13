from collections import defaultdict, deque
def solution(n, roads, sources, destination):
    result = []
    graph = defaultdict(list)
    
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
        
    queue = deque([destination])
    distance = [float("inf") for _ in range(n + 1)]
    distance[destination] = 0
    
    while queue:
        cur_node = queue.popleft()
        
        for next_node in graph[cur_node]:
            if distance[next_node] == float("inf"):
                distance[next_node] = distance[cur_node] + 1
                queue.append(next_node)
    
    for target in sources:
        if distance[target] == float("inf"):
            result.append(-1)
        else:   result.append(distance[target])
    
    return result