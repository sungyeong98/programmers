def solution(matrix_sizes):
    dp=[[0 for i in range(len(matrix_sizes))] for j in range(len(matrix_sizes))]
    for i in range(1,len(matrix_sizes)):
        for j in range(len(matrix_sizes)-i):
            num=i+j
            temp=[]
            for k in range(j,num):
                temp.append(dp[j][k]+dp[k+1][num]+matrix_sizes[j][0]*matrix_sizes[k][1]*matrix_sizes[num][1])
            dp[j][num]=min(temp)
    return dp[0][-1]