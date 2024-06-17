from collections import deque
import sys
INF=sys.maxsize
def solution(stones, k):
    answer = INF
    temp=deque()
    for i in range(len(stones)):
        while len(temp)>0 and temp[-1][0]<stones[i]:
            temp.pop()
        temp.append([stones[i],i])
        while temp[0][1]<i-k+1:
            temp.popleft()
        if i+1>=k:
            answer=min(answer,temp[0][0])
    return answer