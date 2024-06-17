def find_queen(queen,n,row):
    cnt=0
    if n==row:
        return 1
    for i in range(n):
        queen[row]=i
        for j in range(row):
            if queen[j]==queen[row]:
                break
            if abs(queen[j]-queen[row])==(row-j):
                break
        else:
            cnt+=find_queen(queen,n,row+1)
    return cnt
def solution(n):
    queen=[0]*n
    return find_queen(queen,n,0)