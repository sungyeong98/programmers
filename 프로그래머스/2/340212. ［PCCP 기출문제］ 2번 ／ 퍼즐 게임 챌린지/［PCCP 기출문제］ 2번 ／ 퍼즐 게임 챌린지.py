def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    
    while left<=right:
        mid = (left + right) // 2
        
        if solve(diffs, times, limit, mid):
            right = mid - 1
        else:
            left = mid + 1
    return left        
        
def solve(diffs, times, limit, level):
    cnt, n = 0, len(diffs)
    
    for i in range(n):
        if diffs[i] <= level:
            cnt += times[i]
        else:
            fail = diffs[i] - level
            temp_cnt = times[i] * fail
            temp_cnt += times[i-1] * fail
            temp_cnt += times[i]
            
            cnt += temp_cnt
    if limit<cnt:
        return False
    return True