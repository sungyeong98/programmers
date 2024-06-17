from collections import deque
INF=int(1e9)
def solution(board):
    answer,n = INF,len(board)
    dp=[[[INF for _ in range(n)] for _ in range(n)] for _ in range(4)]
    direction=[[0,1,0],[1,0,1],[0,-1,2],[-1,0,3]]
    q=deque([[0,0,0,0],[0,0,0,1]])
    while q:
        x,y,m,d=q.popleft()
        for i in range(4):
            nx=x+direction[i][0]
            ny=y+direction[i][1]
            if -1<nx<n and -1<ny<n and board[nx][ny]==0:
                nm=m+1
                if not d==direction[i][2]:
                    nm+=5
                if nm<dp[direction[i][2]][nx][ny]:
                    dp[direction[i][2]][nx][ny]=nm
                    if nx==n-1 and ny==n-1:
                        continue
                    q.append([nx,ny,nm,direction[i][2]])
    for i in range(4):
        answer=min([answer,dp[i][n-1][n-1]])
    return answer*100