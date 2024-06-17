from collections import deque
def solution(n, m, x, y, r, c, k):
    q=deque([(x,y,'',0)])
    direction=[(1,0,'d'),(0,-1,'l'),(0,1,'r'),(-1,0,'u')]
    while q:
        x,y,path,cnt=q.popleft()
        if (x,y)==(r,c) and (k-cnt)%2==1:
            return 'impossible'
        if (x,y)==(r,c) and k==cnt:
            return path
        for i in range(4):
            dx,dy,dir=direction[i]
            nx,ny=x+dx,y+dy
            if nx<=0 or nx>n or ny<=0 or ny>m:
                continue
            if abs(nx-r)+abs(ny-c)+cnt+1>k:
                continue
            q.append((nx,ny,path+dir,cnt+1))
            break
    return 'impossible'