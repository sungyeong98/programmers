from collections import deque
def solution(n, roads, sources, destination):
    answer,temp = [],{n:[] for n in range(1,n+1)}
    for i,j in roads:
        temp[i].append(j)
        temp[j].append(i)

    q,dis=deque(),[int(1e9) for _ in range(n+1)]
    q.append(destination)
    dis[destination]=0
    while q:
        node=q.popleft()
        for j in temp[node]:
            if dis[j]==int(1e9):
                dis[j]=dis[node]+1
                q.append(j)
    for i in sources:
        if dis[i]==int(1e9):
            answer.append(-1)
        else:
            answer.append(dis[i])
    return answer