def make_tree(n):
    num,cnt=bin(n)[2:],1
    while 2**cnt-1<len(num):
        cnt+=1
    temp=''
    for _ in range(abs((2**cnt-1)-len(num))):
        temp+='0'
    return temp+num
def check_tree(temp):
    if len(temp)<2:
        return True
    if temp[len(temp)//2]=='0':
        return all(val == '0' for val in temp)
    left=check_tree(temp[:len(temp)//2])
    right=check_tree(temp[len(temp)//2+1:])
    return left and right
def solution(numbers):
    answer = []
    for i in numbers:
        temp=list(make_tree(i))
        if check_tree(temp):
            answer.append(1)
        else:
            answer.append(0)
    return answer