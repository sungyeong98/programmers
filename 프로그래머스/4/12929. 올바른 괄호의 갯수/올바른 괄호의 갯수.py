def solution(n):
    dp=[1,1,2,5,14]
    if n<=4:
        return dp[n]
    else:
        for i in range(5,n+1):
            cnt=0
            for j in range(i):
                cnt+=dp[j]*dp[i-1-j]
            dp.append(cnt)
    return dp[n]