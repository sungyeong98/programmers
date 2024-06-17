def solution(m, n, puddles):
    temp=[[1 for _ in range(m)] for _ in range(n)]
    for i,j in puddles:
        temp[j-1][i-1]=0
    for i in range(m):
        if temp[0][i]==0:
            for j in range(i+1,m):
                temp[0][j]=0
            break
    for i in range(n):
        if temp[i][0]==0:
            for j in range(i+1,n):
                temp[j][0]=0
            break
    for i in range(1,n):
        for j in range(1,m):
            if temp[i][j]!=0:
                temp[i][j]=temp[i-1][j]+temp[i][j-1]
    return temp[n-1][m-1]%1000000007