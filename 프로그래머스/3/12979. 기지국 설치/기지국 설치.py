import math
def solution(n, stations, w):
    answer,idx = 0,1
    for i in stations:
        s,e=i-w,i+w
        if s<1:
            s=1
        if e>n:
            e=n
        answer+=math.ceil((s-idx)/(w*2+1))
        idx=e+1
    if n-idx>=0:
        answer+=math.ceil((n-idx+1)/(w*2+1))
    return answer