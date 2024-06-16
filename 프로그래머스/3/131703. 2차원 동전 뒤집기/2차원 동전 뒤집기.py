import copy
def solution(beginning, target):
    temp1=copy.deepcopy(beginning)
    temp2=copy.deepcopy(beginning)
    temp3=copy.deepcopy(beginning)
    temp4=copy.deepcopy(beginning)
    cnt1=convert_1(temp1,target)
    cnt2=convert_2(temp2,target)
    cnt3=convert_3(temp3,target)
    cnt4=convert_4(temp4,target)
    if cnt1==-1 or cnt2==-1 or cnt3==-1 or cnt4==-1:
        return -1
    return min(cnt1,cnt2,cnt3,cnt4)
def list_check(board,target):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]!=target[i][j]:
                return False
    return True
def convert_1(board,target):
    cnt=0
    for i in range(len(board)):
        if board[i][0]!=target[i][0]:
            cnt+=1
            for j in range(len(board[0])):
                if board[i][j]==0:
                    board[i][j]=1
                else:
                    board[i][j]=0
    for i in range(len(board[0])):
        if board[0][i]!=target[0][i]:
            cnt+=1
            for j in range(len(board)):
                if board[j][i]==0:
                    board[j][i]=1
                else:
                    board[j][i]=0
    if list_check(board,target)==False:
        return -1
    return cnt
def convert_2(board,target):
    cnt=0
    for i in range(len(board)):
        if board[i][0]==target[i][0]:
            cnt+=1
            for j in range(len(board[0])):
                if board[i][j]==0:
                    board[i][j]=1
                else:
                    board[i][j]=0
    for i in range(len(board[0])):
        if board[0][i]!=target[0][i]:
            cnt+=1
            for j in range(len(board)):
                if board[j][i]==0:
                    board[j][i]=1
                else:
                    board[j][i]=0
    if list_check(board,target)==False:
        return -1
    return cnt
def convert_3(board,target):
    cnt=0
    for i in range(len(board[0])):
        if board[0][i]!=target[0][i]:
            cnt+=1
            for j in range(len(board)):
                if board[j][i]==0:
                    board[j][i]=1
                else:
                    board[j][i]=0
    for i in range(len(board)):
        if board[i][0]!=target[i][0]:
            cnt+=1
            for j in range(len(board[0])):
                if board[i][j]==0:
                    board[i][j]=1
                else:
                    board[i][j]=0
    if list_check(board,target)==False:
        return -1
    return cnt
def convert_4(board,target):
    cnt=0
    for i in range(len(board[0])):
        if board[0][i]==target[0][i]:
            cnt+=1
            for j in range(len(board)):
                if board[j][i]==0:
                    board[j][i]=1
                else:
                    board[j][i]=0
    for i in range(len(board)):
        if board[i][0]!=target[i][0]:
            cnt+=1
            for j in range(len(board[0])):
                if board[i][j]==0:
                    board[i][j]=1
                else:
                    board[i][j]=0
    if list_check(board,target)==False:
        return -1
    return cnt