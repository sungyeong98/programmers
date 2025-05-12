def solution(progresses, speeds):
    temp = [(100 - p)//s if (100 - p)%s == 0 else (100 - p)//s + 1 for p, s in zip(progresses, speeds)]
    result, max_day = [], 0
    
    for day in temp:
        if day>max_day:
            max_day = day
            result.append(1)
        else:
            result[-1]+=1
    
    return result