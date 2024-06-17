def solution(n, c):
    answer = 0
    q,v=[],[]
    for i in range(n):
        if i not in v:
            q.append(i)
            answer+=1
            while q:
                temp=q.pop(0)
                for j in range(n):
                    if c[temp][j]==1 and j not in v:
                        v.append(j)
                        q.append(j)
    return answer