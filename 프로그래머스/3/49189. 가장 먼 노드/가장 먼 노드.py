from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(set)
    
    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)
    
    distance = [float('inf') for _ in range(n+1)]
    queue = deque([1])
    distance[1] = 0
    
    while queue:
        cur_node = queue.popleft()
        
        for next_node in graph[cur_node]:
            if distance[next_node] == float('inf'):
                distance[next_node] = distance[cur_node] + 1
                queue.append(next_node)
    
    return distance[1:].count(max(distance[1:]))