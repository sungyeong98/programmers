import math
def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        if i==1:answer.append(0)
        else:
            chk=prime(i)
            if chk==True:
                answer.append(1)
            else:
                num=divisor(i)
                num.pop()
                while num[-1]>10**7:
                    num.pop()
                answer.append(num[-1])
    return answer
def divisor(n):
    temp=[]
    for i in range(1,int(n**(1/2))+1):
        if (n%i)==0:
            temp.append(i)
            if i**2!=n:
                temp.append(n//i)
    temp.sort()
    return temp
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True