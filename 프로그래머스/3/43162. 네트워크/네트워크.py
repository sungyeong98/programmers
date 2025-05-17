from collections import defaultdict, deque
def solution(n, computers):
    networks = defaultdict(list)
    for idx, network_list in enumerate(computers):
        for i, val in enumerate(network_list):
            if idx != i and val == 1:
                networks[idx].append(i)
    
    visited = set()
    result = 0
    for computer in range(n):
        if computer in visited:
            continue
        queue = deque([])
        queue.append(computer)
        
        while queue:
            cur_computer = queue.popleft()
            
            if cur_computer not in visited:
                visited.add(cur_computer)
                for next_computer in networks[cur_computer]:
                    queue.append(next_computer)
                    
        result += 1
    
    return result