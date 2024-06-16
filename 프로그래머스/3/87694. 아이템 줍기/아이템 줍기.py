from collections import deque
def solution(rectangle,characterX,characterY,itemX,itemY):
    answer=0
    point_list=[[-1 for _ in range(102)] for _ in range(102)]
    for i in rectangle:
        x1,y1,x2,y2=map(lambda x:x*2,i)
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if x1<x<x2 and y1<y<y2:
                    point_list[x][y]=0
                elif point_list[x][y]!=0:
                    point_list[x][y]=1
    queue=deque()
    start=(characterX*2,characterY*2)
    end=(itemX*2,itemY*2)
    queue.append(start)
    visited=[[1 for _ in range(102)] for _ in range(102)]
    while queue:
        current=queue.popleft()
        if current==end:
            break
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx=current[0]+dx
            ny=current[1]+dy
            if point_list[nx][ny]==1 and visited[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny]=visited[current[0]][current[1]]+1
    return visited[end[0]][end[1]]//2