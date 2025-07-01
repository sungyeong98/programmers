def solution(n):
    left, right = 0, 0
    total_sum = 0
    result = 0
    
    while left < n:
        if total_sum < n:
            right += 1
            total_sum += right
        else:
            if total_sum == n:  result += 1
            left += 1
            total_sum -= left
    
    return result