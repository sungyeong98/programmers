import sys
sys.setrecursionlimit(1000000)
def solution(n, count):
    temp={(1,1):1}
    def count_building(i,j):
        if i==0 or j==0:
            return 0
        if (i,j) in temp:
            return temp[(i,j)]
        a=count_building(i-1,j-1)+count_building(i-1,j)*(i-1)*2
        temp[(i,j)]=a%1000000007
        return temp[(i,j)]
    return count_building(n,count)