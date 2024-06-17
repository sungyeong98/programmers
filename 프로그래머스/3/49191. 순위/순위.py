def solution(n, results):
    answer = n
    temp=[['N']*n for _ in range(n)]
    for i in range(0,len(temp)):
        for j in range(0,len(temp)):
            if i==j:
                temp[i][j]=0
    for i in results:
        a,b=i
        temp[a-1][b-1]=1
        temp[b-1][a-1]=-1
    for i in range(0,len(temp)):
        for j in range(0,len(temp)):
            for k in range(0,len(temp)):
                if temp[j][i]==1 and temp[i][k]==1:
                    temp[j][k]=1
                    temp[k][j]=-1
    for i in temp:
        if 'N' in i:
            answer-=1
    return answer