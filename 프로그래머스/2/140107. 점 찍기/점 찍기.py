import math
def solution(k, d):
    temp=0
    for i in range(0,d+1,k):
        x=d**2-i**2
        count=math.sqrt(x)//k+1
        temp+=count
    return temp