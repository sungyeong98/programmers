from collections import defaultdict, deque
def solution(n, wires):
    result = float('inf')
    
    for idx in range(len(wires)):
        temp = defaultdict(set)
        
        for i, (v1, v2) in enumerate(wires):
            if i!=idx:
                temp[v1].add(v2)
                temp[v2].add(v1)
        
        queue = deque([1])
        visited = set()
        visited.add(1)
        cnt = 0
        while queue:
            cur_v = queue.popleft()
            cnt += 1
            
            for next_v in temp[cur_v]:
                if next_v not in visited:
                    visited.add(next_v)
                    queue.append(next_v)
        result = min(result, abs(abs(n-cnt) - cnt))
    return result