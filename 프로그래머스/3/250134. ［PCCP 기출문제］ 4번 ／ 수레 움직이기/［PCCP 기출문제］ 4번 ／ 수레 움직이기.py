from itertools import product
min_cnt=float('inf')
dx,dy=[0,0,1,-1],[-1,1,0,0]
def solution(maze):
    red_pos,blue_pos,red_end,blue_end=0,0,0,0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==1:
                red_pos=(i,j)
            if maze[i][j]==2:
                blue_pos=(i,j)
            if maze[i][j]==3:
                red_end=(i,j)
            if maze[i][j]==4:
                blue_end=(i,j)
    red_visited,blue_visited={red_pos},{blue_pos}
    dfs(red_pos,blue_pos,red_end,blue_end,red_visited,blue_visited,0,maze)
    return min_cnt if min_cnt!=float('inf') else 0

def dfs(red_pos,blue_pos,red_end,blue_end,red_visited,blue_visited,cnt,maze):
    global min_cnt
    if red_pos==red_end and blue_pos==blue_end:
        min_cnt=min(min_cnt,cnt)
        return
    red_list=move(red_pos,maze,red_visited,red_end)
    blue_list=move(blue_pos,maze,blue_visited,blue_end)

    for red_cp in red_list:
        for blue_cp in blue_list:
            if red_cp!=blue_cp and (red_cp,blue_cp)!=(blue_pos,red_pos):
                red_new_visited=red_visited | {red_cp}
                blue_new_visited=blue_visited | {blue_cp}
                dfs(red_cp, blue_cp, red_end, blue_end, red_new_visited, blue_new_visited, cnt+1, maze)

def move(pos,maze,visited,target):
    temp=[]
    if pos==target:
        return [target]
    for i in range(4):
        np=(pos[0]+dx[i],pos[1]+dy[i])
        if 0<=np[0]<len(maze) and 0<=np[1]<len(maze[0]) and np not in visited and maze[np[0]][np[1]]!=5:
            temp.append(np)
    return temp  