def solution(n, money):
    dp=[0 for _ in range(n+1)]
    dp[0]=1
    for i in money:
        for j in range(1,len(dp)):
            if j>=i:
                dp[j]+=dp[j-i]
    return dp[-1]