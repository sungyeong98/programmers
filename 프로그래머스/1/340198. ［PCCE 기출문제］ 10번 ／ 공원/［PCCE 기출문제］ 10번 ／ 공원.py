def solution(mats, park):
    result, m, n = -1, len(park), len(park[0])
    dp = [[0]*n for _ in range(m)]
    temp = set()
    
    for i in range(m):
        for j in range(n):
            if park[i][j]=='-1':
                dp[i][j]=1
                
    for i in range(1,m):
        for j in range(1,n):
            if dp[i][j]==0: continue
            
            dp[i][j]=min(dp[i-1][j-1], min(dp[i-1][j],dp[i][j-1]))+1
            temp.add(dp[i][j])
    
    for i in mats:
        if i in temp:
            result = max(result, i)
        
    return result