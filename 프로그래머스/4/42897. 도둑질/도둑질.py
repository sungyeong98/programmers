def solution(money):
    answer = 0
    dp1,dp2=[0],[0]
    for i in range(0,len(money)-1):
        dp1.append(money[i])
    for i in range(1,len(money)):
        dp2.append(money[i])
    for i in range(len(dp1)):
        if i>=2:
            dp1[i]=max(dp1[i-1],dp1[i]+dp1[i-2])
    for i in range(len(dp2)):
        if i>=2:
            dp2[i]=max(dp2[i-1],dp2[i]+dp2[i-2])
    answer=max(dp1[-1],dp2[-1])
    return answer