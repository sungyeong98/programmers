def solution(s):
    answer = 0
    if len(s)==1:
        return s[0]
    c1,c2=[0],[0]
    for i in range(0,len(s)-1):
        c1.append(s[i])
    for i in range(1,len(s)):
        c2.append(s[i])
    for i in range(2,len(c1)):
        c1[i]=max(c1[i-1],c1[i]+c1[i-2])
        c2[i]=max(c2[i-1],c2[i]+c2[i-2])
    answer=max(c1[-1],c2[-1])
    return answer