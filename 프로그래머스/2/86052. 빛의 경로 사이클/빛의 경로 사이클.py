def solution(grid):
    answer=[]
    r,c=len(grid),len(grid[0])
    visited=[[[False]*4 for _ in range(c)] for _ in range(r)]
    dx,dy=[1,0,-1,0],[0,-1,0,1]
    for x in range(r):
        for y in range(c):
            for d in range(4):
                if visited[x][y][d]:
                    continue
                cnt,nx,ny=0,x,y
                while not visited[nx][ny][d]:
                    visited[nx][ny][d]=True
                    cnt+=1
                    if grid[nx][ny]=='S':
                        pass
                    elif grid[nx][ny]=='L':
                        d=(d-1)%4
                    else:
                        d=(d+1)%4
                    nx=(nx+dx[d])%r
                    ny=(ny+dy[d])%c
                answer.append(cnt)
    answer.sort()
    return answer