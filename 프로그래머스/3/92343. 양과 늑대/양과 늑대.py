from collections import defaultdict
def solution(info, edges):
    graph = defaultdict(list)
    result = 0
    
    for start, end in edges:
        graph[start].append(end)
    
    def find(sheep, wolf, node, next_nodes):
        nonlocal result
        
        if info[node] == 0:     sheep += 1
        else:                   wolf += 1
        
        if sheep <= wolf:       return
    
        result = max(result, sheep)
        
        next_nodes.extend(graph[node])
        next_nodes.remove(node)
        
        for next_node in next_nodes:
            find(sheep, wolf, next_node, next_nodes.copy())
    
    find(0, 0, 0, [0])
    
    return result