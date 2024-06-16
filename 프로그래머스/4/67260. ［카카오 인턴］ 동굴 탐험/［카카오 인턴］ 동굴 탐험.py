from collections import deque
def solution(n, path, order):
    answer = True
    temp,p1,p2,q,v={n:[] for n in range(n)},{},{},deque(),[0]*n
    for i,j in path:
        temp[i].append(j)
        temp[j].append(i)
    for i,j in order:
        p1[i]=j
        p2[j]=i
        if j==0:
            return False
        if i==0:
            p1[0]=0
    v[0]=1
    q.append(0)
    while q:
        node=q.popleft()
        if node==p1.get(p2.get(node)):
            v[node]=2
        else:
            for i in temp[node]:
                if v[i]==0:
                    q.append(i)
                    v[i]=1
                    if p1.get(i):
                        if v[p1[i]]==2:
                            q.append(p1[i])
                            v[p1[i]]=1
                        p1[i]=0
    for i in v:
        if i==0:
            return False
    return answer