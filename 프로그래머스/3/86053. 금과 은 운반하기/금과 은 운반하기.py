def solution(a,b,g,s,w,t):
    INF=10**9*10**5*4
    answer=int(INF)
    start,end=0,int(INF)
    n=len(g)
    while start<=end:
        mid=(start+end)//2
        gold,silver,total=0,0,0
        for i in range(n):
            current_gold=g[i]
            current_silver=s[i]
            current_weight=w[i]
            current_time=t[i]
            count=mid//(current_time*2)
            if mid%(current_time*2)>=current_time:
                count+=1
            gold+=current_gold if current_gold<count*current_weight else count*current_weight
            silver+=current_silver if current_silver<count*current_weight else count*current_weight
            total+=current_gold+current_silver if current_gold+current_silver<count*current_weight else count*current_weight
        if gold>=a and silver>=b and total>=a+b:
            end=mid-1
            answer=min(answer,mid)
        else:
            start=mid+1
    return answer