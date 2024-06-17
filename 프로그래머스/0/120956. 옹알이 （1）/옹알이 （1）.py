from itertools import permutations
def solution(babbling):
    answer = 0
    term=["aya", "ye", "woo", "ma"]
    temp=[]
    for i in range(1,5):
        a=list(permutations(term,i))
        for j in a:
            b=''
            for k in j:
                b+=k
            temp.append(b)
    for i in temp:
        for j in babbling:
            if i==j:
                answer+=1
    return answer