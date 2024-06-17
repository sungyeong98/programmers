def check_intersection(x1,x2):
    a,b,e=x1
    c,d,f=x2
    if a*d-b*c==0:
        return False
    if (b*f-e*d)%(a*d-b*c)!=0 or (e*c-a*f)%(a*d-b*c)!=0:
        return False
    return True
def cal_intersection(x1,x2):
    a,b,e=x1
    c,d,f=x2
    return (b*f-e*d)//(a*d-b*c),(e*c-a*f)//(a*d-b*c)
def draw_intersection(max_x,max_y,min_x,min_y,inter_list):
    board,result=[],[]
    for _ in range(max_y-min_y+1):
        temp=[]
        for _ in range(max_x-min_x+1):
            temp.append('.')
        board.append(temp)
    for x,y in inter_list:
        board[y-min_y][x-min_x]='*'
    for i in range(len(board)):
        temp=''
        for j in range(len(board[0])):
            temp+=board[i][j]
        result.insert(0,temp)
    return result
def solution(line):
    answer,temp = [],[]
    for i in range(len(line)):
        for j in range(i,len(line)):
            if i!=j and check_intersection(line[i],line[j]):
                x,y=cal_intersection(line[i],line[j])
                temp.append((x,y))
    max_x,max_y,min_x,min_y=temp[0][0],temp[0][1],temp[0][0],temp[0][1]
    for x,y in temp:
        max_x=max(max_x,x)
        max_y=max(max_y,y)
        min_x=min(min_x,x)
        min_y=min(min_y,y)
    answer=draw_intersection(max_x,max_y,min_x,min_y,temp)
    return answer