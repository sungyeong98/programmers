def solution(a):
    temp=[False for _ in a]
    ml,mr=int(1e9),int(1e9)
    for i in range(len(a)):
        if a[i]<ml:
            ml=a[i]
            temp[i]=True
        if a[-1-i]<mr:
            mr=a[-1-i]
            temp[-1-i]=True
    return temp.count(True)