def solution(triangle):
    temp = sorted(triangle, key = lambda x : len(x), reverse = True)
    n = len(temp)
    
    for i in range(1, n):
        for j in range(len(temp[i])):
            temp[i][j] = max(temp[i][j] + temp[i-1][j], temp[i][j] + temp[i-1][j+1])
    
    return temp[-1][0]