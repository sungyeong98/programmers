from itertools import combinations
def solution(n, q, ans):
    answer = 0
    for i in list(combinations(range(1,n+1), 5)):
        flag = True
        for idx, j in enumerate(q):
            if ans[idx] != len(set(i) & set(j)):
                flag = False
                break
        if flag: answer+=1
    
    return answer