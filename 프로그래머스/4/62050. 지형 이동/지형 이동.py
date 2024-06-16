from collections import deque
from heapq import heappush,heappop
def solution(land, height):
    answer = 0
    visited=[[False for _ in range(len(land))] for _ in range(len(land))]
    temp=[[0,0,0]]
    dx,dy=[0,0,-1,1],[-1,1,0,0]
    while temp:
        val,x,y=heappop(temp)
        if visited[x][y]:
            continue
        visited[x][y]=True
        answer+=val
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<len(land) and 0<=ny<len(land) and not visited[nx][ny]:
                if abs(land[x][y]-land[nx][ny])>height:
                    heappush(temp,[abs(land[x][y]-land[nx][ny]),nx,ny])
                else:
                    heappush(temp,[0,nx,ny])
    return answer