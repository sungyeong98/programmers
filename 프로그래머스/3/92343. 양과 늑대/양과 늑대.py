def dfs(sheep,wolf,edges,visited,answer,info):
    if sheep>wolf:
        answer.append(sheep)
    else:
        return
    for i,j in edges:
        if visited[i] and not visited[j]:
            visited[j]=1
            if info[j]==0:
                dfs(sheep+1,wolf,edges,visited,answer,info)
            else:
                dfs(sheep,wolf+1,edges,visited,answer,info)
            visited[j]=0
def solution(info,edges):
    answer=[]
    n=len(info)
    visited=[0]*n
    visited[0]=1
    dfs(1,0,edges,visited,answer,info)
    return max(answer)