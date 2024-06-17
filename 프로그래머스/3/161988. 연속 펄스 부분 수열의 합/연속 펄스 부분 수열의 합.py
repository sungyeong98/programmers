def solution(sequence):
    if len(sequence)==1:
        return abs(sequence[0])
    answer = 0
    c1=[1,-1]
    c2=[-1,1]
    a,b=[],[]
    for i in range(0,len(sequence)):
        a.append(c1[i%2]*sequence[i])
        b.append(c2[i%2]*sequence[i])
    a1=chk(a)
    b1=chk(b)
    return max(a1,b1)

def chk(arr):
    temp=[0]*len(arr)
    temp[0]=arr[0]
    for i in range(0,len(arr)):
        temp[i]=max(0,temp[i-1])+arr[i]
    return max(temp)