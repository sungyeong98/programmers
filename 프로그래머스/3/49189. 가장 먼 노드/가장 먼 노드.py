import sys
from collections import deque
INF=sys.maxsize
def solution(n, edge):
    answer = 0
    temp={i:[] for i in range(1,n+1)}
    for i,j in edge:
        temp[i].append(j)
        temp[j].append(i)
    q,count=deque([]),[INF]*(n+1)
    q.append(1)
    count[1]=0
    while q:
        node=q.popleft()
        for i in temp[node]:
            if count[i]==INF:
                count[i]=count[node]+1
                q.append(i)
    answer=count[1:].count(max(count[1:]))
    return answer