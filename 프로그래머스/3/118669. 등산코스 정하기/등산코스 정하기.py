from collections import defaultdict
from heapq import heappop,heappush
def solution(n,paths,gates,summits):
    summits.sort()
    gates.sort()
    summits,gates=set(summits),set(gates)
    dp=[float('inf')]*(n+1)
    graph=defaultdict(list)
    for i in range(1,n+1):
        if i in gates:
            dp[i]=0
    for s,e,w in paths:
        graph[s].append((e,w))
        graph[e].append((s,w))
    
    heap=[]
    for gate in gates:
        heappush(heap,(gate,0))

    while heap:
        node,weight=heappop(heap)
        if node in summits:
            continue
        if weight>dp[node]:
            continue
        
        for child_node,child_weight in graph[node]:
            if child_node in gates:
                continue
            next_weight=max(weight,child_weight)
            if next_weight>=dp[child_node]:
                continue
            dp[child_node]=next_weight
            heappush(heap,(child_node,next_weight))
    
    answer=[]
    for summit in summits:
        temp=[]
        temp.append(summit)
        temp.append(dp[summit])
        answer.append(temp)
    answer.sort(key=lambda x:(x[1],x[0]))
    return answer[0]