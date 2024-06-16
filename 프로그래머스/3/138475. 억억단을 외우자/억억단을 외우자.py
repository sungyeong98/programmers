def solution(e, starts):
    num=0
    temp=[0 for i in range(e+1)]
    tmp=[0 for i in range(e+1)]
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            temp[i*j]+=2
    for i in range(1,int(e**(1/2))+1):
        temp[i**2]+=1
    for i in range(e,0,-1):
        if num<=temp[i]:
            num=temp[i]
            tmp[i]=i
        else:
            tmp[i]=tmp[i+1]
    return [tmp[i] for i in starts]