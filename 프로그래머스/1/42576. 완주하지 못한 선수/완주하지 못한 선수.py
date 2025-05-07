from collections import Counter
def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    for i in p_counter.keys():
        if i not in c_counter:
            return i
        if p_counter[i]!=c_counter[i]:
            return i