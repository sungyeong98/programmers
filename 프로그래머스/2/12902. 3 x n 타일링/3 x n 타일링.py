def solution(n):
    temp=(3,11)
    if n==2:
        return temp[0]
    if n==4:
        return temp[1]
    n/=2
    n-=2
    while n>0:
        temp=(temp[1],temp[1]*4-temp[0])
        n-=1
    return temp[1]%1000000007