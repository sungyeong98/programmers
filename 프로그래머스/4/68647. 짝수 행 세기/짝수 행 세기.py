MOD=10**7+19
def query_combination(n,r,pascal):
    if n==r or r==0:
        pascal[n][r]=1
        return 1
    if pascal[n][r]>0:
        return pascal[n][r]%MOD
    pascal[n][r]=(query_combination(n-1,r-1,pascal)+query_combination(n-1,r,pascal))%MOD
    return pascal[n][r]

def solution(a):
    row,col=len(a),len(a[0])
    pascal=[[0 for _ in range(row+1)] for _ in range(row+1)]
    for i in range(row+1):
        for j in range(i+1):
            query_combination(i,j,pascal)
    num_count_list=[]
    for j in range(col):
        num_cnt=0
        for i in range(row):
            if a[i][j]==1:
                num_cnt+=1
        num_count_list.append(num_cnt)
    dp=[[0 for _ in range(row+1)] for _ in range(col+1)]
    dp[1][row-num_count_list[0]]=pascal[row][row-num_count_list[0]]
    for j in range(1,col):
        for i in range(row+1):
            if dp[j][i]==0:
                continue
            for n in range(num_count_list[j]+1):
                next_num=(i-n)+(num_count_list[j]-n)
                if next_num>row or row<n:
                    continue
                count=(pascal[i][n]*pascal[row-i][num_count_list[j]-n])%MOD
                dp[j+1][next_num]+=(dp[j][i]*count)%MOD
    return dp[col][row]