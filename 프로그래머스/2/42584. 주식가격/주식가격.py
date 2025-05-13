from collections import deque
def solution(prices):
    result, queue = [], deque(prices)
    
    while(queue):
        cur_price, cnt = queue.popleft(), 0
        
        for next_price in queue:
            cnt+=1
            if cur_price>next_price:    break
        
        result.append(cnt)
        
    return result