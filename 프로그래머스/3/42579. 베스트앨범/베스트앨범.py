def solution(g, p):
    answer = []
    a={}
    for i in range(0,len(g)):
        if g[i] in a:
            a[g[i]].append([i,p[i]])
        else:
            a[g[i]]=[[i,p[i]]]
    a={x:sorted(y,reverse=True,key=lambda x:x[1]) for x,y in a.items()}
    temp={}
    for i in a:
        b=[]
        for j in a[i]:
            b.append(j[1])
        temp[i]=sum(b)
    temp=dict(sorted(temp.items(),key=lambda x:x[1],reverse=True))
    for i in temp:
        if len(a[i])==1:
            answer.append(a[i][0][0])
        else:
            answer.append(a[i][0][0])
            answer.append(a[i][1][0])
    return answer