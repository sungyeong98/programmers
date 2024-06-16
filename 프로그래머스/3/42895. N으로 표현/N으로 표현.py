def solution(n, number):
    if n==number:
        return 1
    dp=[[None],[n,-n]]
    for i in range(1,8):
        temp=[]
        for j in dp[i]:
            temp.extend(find(j,n))
        m=11
        for k in range(i):
            for j in dp[i-1-k]:
                temp.extend(find(j,n*m))
            m+=10**(k+2)
        if number in temp:
            return i+1
        dp.append(temp)
    return -1
def find(n,k):
    if n==None:
        return [k,-k]
    return [n+k,n-k,n*k,n//k]