import sys
sys.setrecursionlimit(10**6)
answer=0
def solution(a,edges):
    if sum(a)!=0:
        return -1
    temp=[[] for _ in range(len(a))]
    for i,j in edges:
        temp[i].append(j)
        temp[j].append(i)
    def dfs(child,parent,temp,a):
        global answer
        for i in temp[child]:
            if i!=parent:
                dfs(i,child,temp,a)
        a[parent]+=a[child]
        answer+=abs(a[child])
    dfs(0,0,temp,a)
    return answer