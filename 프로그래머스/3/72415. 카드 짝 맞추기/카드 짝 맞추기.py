from collections import deque
from copy import deepcopy
INF=int(1e9)
answer=INF
def bfs(board,current_x,current_y,target_x,target_y):
    dx,dy=[1,0,0,-1],[0,1,-1,0]
    q=deque()
    q.append((current_x,current_y))
    visited=[[INF for _ in range(4)] for _ in range(4)]
    visited[current_x][current_y]=0
    while q:
        x,y=q.popleft()
        if x==target_x and y==target_y:
            return visited[x][y]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<4 and 0<=ny<4 and visited[nx][ny]>visited[x][y]+1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            while 0<=nx+dx[i]<4 and 0<=ny+dy[i]<4 and board[nx][ny]==0:
                nx,ny=nx+dx[i],ny+dy[i]
            if 0<=nx<4 and 0<=ny<4 and visited[nx][ny]>visited[x][y]+1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
def find_num(board,target):
    for i in range(4):
        for j in range(4):
            if board[i][j]==target:
                return i,j
def IsEnd(board):
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                return False
    return True
def dfs(board,r,c,target_x,target_y,count):
    global answer
    board=deepcopy(board)
    target_num=board[target_x][target_y]
    count+=bfs(board,r,c,target_x,target_y)
    board[target_x][target_y]=0
    second_target_x,second_target_y=find_num(board,target_num)
    count+=bfs(board,target_x,target_y,second_target_x,second_target_y)
    board[second_target_x][second_target_y]=0
    count+=2
    if IsEnd(board):
        answer=min(answer,count)
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                dfs(board,second_target_x,second_target_y,i,j,count)
def solution(board,r,c):
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                dfs(board,r,c,i,j,0)
    return answer