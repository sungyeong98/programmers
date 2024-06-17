def solution(board, skill):
    answer = 0
    temp=[[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for i in skill:
        typ=i[0]
        sx,sy,ex,ey=i[1],i[2],i[3],i[4]
        num=i[5]
        if typ==1:
            num=-num
        temp[sx][sy]+=num
        temp[ex+1][sy]-=num
        temp[sx][ey+1]-=num
        temp[ex+1][ey+1]+=num
    for i in range(len(temp)):
        for j in range(1,len(temp[0])):
            temp[i][j]+=temp[i][j-1]
    for i in range(len(temp[0])):
        for j in range(1,len(temp)):
            temp[j][i]+=temp[j-1][i]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=temp[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>0:
                answer+=1
    return answer