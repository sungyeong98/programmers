import sys
INF=sys.maxsize
def solution(n, s, a, b, fares):
    answer = INF
    temp=[[INF]*n for _ in range(n)]
    for i in range(n):
        temp[i][i]=0
    for f in fares:
        u,v,m=f
        temp[u-1][v-1]=m
        temp[v-1][u-1]=m
    for k in range(n):
        for i in range(n):
            for j in range(n):
                temp[i][j]=min(temp[i][j],temp[i][k]+temp[k][j])
    for i in range(n):
        ans=temp[s-1][i]+temp[i][a-1]+temp[i][b-1]
        answer=min(answer,ans)
    return answer