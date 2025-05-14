from collections import Counter
def solution(citations):
    counter = Counter(citations)
    temp = sorted(set(citations))
    cnt, result = 0, 0
    
    for i in temp[::-1]:
        cnt+=counter[i]
        result = max(result, min(cnt, i))
    
    return result