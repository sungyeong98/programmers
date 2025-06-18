def solution(stones, k):
    left, right = 1, max(stones)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        for i in stones:
            if mid > i: 
                cnt += 1
                if cnt >= k: break
            else:   cnt = 0
        
        if cnt < k:    
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result