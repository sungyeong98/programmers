def solution(arr):
    INF,num,op=int(1e9),[],[]
    for i in arr:
        if i.isdigit():
            num.append(int(i))
        else:
            op.append(i)
    n=len(num)
    maxdp=[[-INF for _ in range(n)] for _ in range(n)]
    mindp=[[INF for _ in range(n)] for _ in range(n)]
    for step in range(n):
        for i in range(n-step):
            j=i+step
            if step==0:
                maxdp[i][i]=num[i]
                mindp[i][i]=num[i]
            else:
                for k in range(i,j):
                    if op[k]=='+':
                        maxdp[i][j]=max(maxdp[i][j],maxdp[i][k]+maxdp[k+1][j])
                        mindp[i][j]=min(mindp[i][j],mindp[i][k]+mindp[k+1][j])
                    else:
                        maxdp[i][j]=max(maxdp[i][j],maxdp[i][k]-mindp[k+1][j])
                        mindp[i][j]=min(mindp[i][j],mindp[i][k]-maxdp[k+1][j])
    return maxdp[0][n-1]