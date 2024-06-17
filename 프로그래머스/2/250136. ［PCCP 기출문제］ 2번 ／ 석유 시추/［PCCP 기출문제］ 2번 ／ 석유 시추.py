dx=[-1,1,0,0]
dy=[0,0,1,-1]
from collections import deque
def solution(land):
    max_oil=0
    oil={i:0 for i in range(len(land[0]))}
    visited=set()
    for i in range(len(land)):
        for j in range(len(land[0])):
            if (i,j) not in visited and land[i][j]==1:
                bfs(i,j,land,visited,oil)
    for i in oil:
        max_oil=max(max_oil,oil[i])
    return max_oil
def bfs(x,y,land,visited,oil):
    q=deque()
    q.append([x,y])
    new_col,start_num=set(),len(visited)
    while q:
        cx,cy=q.popleft()
        if (cx,cy) not in visited:
            visited.add((cx,cy))
            new_col.add(cy)
            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny]==1:
                    q.append([nx,ny])
    col_chk=[]
    for i in new_col:
        if i not in col_chk:
            col_chk.append(i)
            oil[i]+=len(visited)-start_num