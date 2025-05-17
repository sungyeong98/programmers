from heapq import heapify, heappush, heappop
def solution(scoville, K):
    result = 0
    heapify(scoville)

    while len(scoville)>1:
        current1 = heappop(scoville)
        if current1 >= K:
            return result

        current2 = heappop(scoville)
        
        heappush(scoville, current1 + (current2 * 2))
        result += 1
    
    if scoville[0] >= K:
        return result
    
    return -1