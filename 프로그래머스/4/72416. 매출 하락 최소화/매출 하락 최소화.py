from collections import defaultdict
def solution(sales, links):
    dp=[[0,0]]+[[0,i] for i in sales]
    temp=generate(links)
    dfs(1,temp,dp)
    return min(dp[1])
def generate(l):
    temp=defaultdict(list)
    for i,j in l:
        temp[i].append(j)
    return temp
def dfs(node,temp,dp):
    if node not in temp:
        return
    cnt,zcnt,mv,md=0,0,0,float('inf')
    for i in temp[node]:
        dfs(i,temp,dp)
        mv+=min(dp[i])
        cnt+=1
        if dp[i][1]>dp[i][0]:
            zcnt+=1
            md=min(md,dp[i][1]-dp[i][0])
    dp[node][1]+=mv
    if cnt==zcnt:
        dp[node][0]+=mv+md
    else:
        dp[node][0]+=mv