def solution(a):
    answer,n =0,len(a)
    a,chk=[a[0]]+a+[a[-1]],[-1]*(n+2)
    cnt=dict()
    for i in range(1,n+1):
        if a[i] not in cnt:
            cnt[a[i]]=0
        if a[i-1]!=a[i] and chk[i-1]!=a[i]:
            chk[i-1]=a[i]
            cnt[a[i]]+=1
        elif a[i+1]!=a[i] and chk[i+1]!=a[i]:
            chk[i+1]=a[i]
            cnt[a[i]]+=1
        answer=max(answer,2*cnt[a[i]])
    return answer