from string import ascii_uppercase
alp={val:idx if idx<len(list(ascii_uppercase))//2 else len(list(ascii_uppercase))-idx for idx,val in enumerate(list(ascii_uppercase))}

def solution(name):
    answer = 0
    move=len(name)-1
    for idx,val in enumerate(name):
        answer+=alp[val]
        temp=idx+1
        while temp<len(name) and name[temp]=='A':
            temp+=1
        move=min([move,2*idx+len(name)-temp,idx+2*(len(name)-temp)])
    answer+=move
    return answer