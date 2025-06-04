def solution(routes):
    result = 0
    temp = float("-inf")
    r = sorted(routes, key = lambda x:x[1])
    
    for start, end in r:
        if temp < start:
            temp = end
            result += 1
    
    return result