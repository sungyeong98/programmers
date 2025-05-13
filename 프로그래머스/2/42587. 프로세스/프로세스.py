from collections import deque, Counter
def solution(priorities, location):
    queue = deque([(idx, val) for idx, val in enumerate(priorities)])
    p = sorted(set(priorities))
    counter = Counter(priorities)
    order = 1

    while queue:
        idx, val = queue.popleft()
        max_val = p[-1]
        
        if val == max_val:
            counter[max_val]-=1
            if counter[max_val] == 0:
                counter.pop(max_val)
                p.pop()
            if idx == location:
                return order
            order+=1
        else:
            queue.append((idx, val))