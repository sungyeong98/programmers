def solution(board):
    answer,on,xn,ow,xw = 0,0,0,0,0
    b=[list(board[i]) for i in range(len(board))]
    for i in b:
        on+=i.count('O')
        xn+=i.count('X')
    if on-xn!=0 and on-xn!=1:
        return 0
    if on==0 and xn==0:
        return 1
    for i in range(len(b)):
        if i==0:
            if b[i][0]=='O' and b[1][1]=='O' and b[2][2]=='O':
                ow+=1
            if b[0][2]=='O' and b[1][1]=='O' and b[2][0]=='O':
                ow+=1
            if b[0][0]=='O' and b[1][0]=='O' and b[2][0]=='O':
                ow+=1
            if b[0][1]=='O' and b[1][1]=='O' and b[2][1]=='O':
                ow+=1
            if b[0][2]=='O' and b[1][2]=='O' and b[2][2]=='O':
                ow+=1
            if b[i][0]=='X' and b[1][1]=='X' and b[2][2]=='X':
                xw+=1
            if b[0][2]=='X' and b[1][1]=='X' and b[2][0]=='X':
                xw+=1
            if b[0][0]=='X' and b[1][0]=='X' and b[2][0]=='X':
                xw+=1
            if b[0][1]=='X' and b[1][1]=='X' and b[2][1]=='X':
                xw+=1
            if b[0][2]=='X' and b[1][2]=='X' and b[2][2]=='X':
                xw+=1
            if b[i][0]=='O' and b[i][1]=='O' and b[i][2]=="O":
                ow+=1
            if b[i][0]=='X' and b[i][1]=='X' and b[i][2]=="X":
                xw+=1
        else:
            if b[i][0]=='O' and b[i][1]=='O' and b[i][2]=="O":
                ow+=1
            if b[i][0]=='X' and b[i][1]=='X' and b[i][2]=="X":
                xw+=1
    if ow>0 and xw>0:
        return 0
    elif ow>0 and xw==0:
        if on==xn+1:
            return 1
        else:
            return 0
    elif xw>0 and ow==0:
        if on==xn:
            return 1
        else:
            return 0
    elif ow==0 and xw==0:
        return 1
    return answer