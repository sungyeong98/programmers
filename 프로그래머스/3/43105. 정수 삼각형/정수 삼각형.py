def solution(triangle):
    tt=sorted(triangle,key=lambda x:len(x),reverse=True)
    for i in range(1,len(tt)):
        for j in range(0,len(tt[i])):
            tt[i][j]=max(tt[i][j]+tt[i-1][j],tt[i][j]+tt[i-1][j+1])
    answer = tt[-1][0]
    return answer