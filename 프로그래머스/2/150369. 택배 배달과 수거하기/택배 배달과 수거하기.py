def solution(cap, n, deliveries, pickups):
    answer,d,p = 0,0,0
    for i in range(n-1,-1,-1):
        d-=deliveries[i]
        p-=pickups[i]
        cnt=0
        while d<0 or p<0:
            d+=cap
            p+=cap
            cnt+=1
        answer+=(i+1)*2*cnt
    return answer