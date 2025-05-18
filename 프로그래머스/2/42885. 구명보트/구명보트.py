from collections import deque
def solution(people, limit):
    p = deque(sorted(people))
    result = 0
    
    while p:
        temp = p.pop()
        
        if p and temp + p[0] <= limit:
            temp += p.popleft()
        
        result += 1
    
    return result