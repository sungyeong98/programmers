def solution(edges):
    answer=[0,0,0,0]
    num=max([max(n) for n in edges])
    graph={i:[[],[]] for i in range(1,num+1)}
    root=0
    for i,j in edges:
        graph[i][0].append(j)
        graph[j][1].append(i)
    for i in graph:
        if len(graph[i][0])>=2 and len(graph[i][1])==0:
            answer[0]=i
        elif len(graph[i][0])==0 and len(graph[i][1])>0:
            answer[2]+=1
        elif len(graph[i][0])>=2 and len(graph[i][1])>=2:
            answer[3]+=1
    answer[1]=len(graph[answer[0]][0])-answer[2]-answer[3]
    return answer