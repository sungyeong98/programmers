import re
from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    banned_id=[i.replace('*','.') for i in banned_id]
    for i in permutations(user_id,len(banned_id)):
        chk=True
        for j in range(len(banned_id)):
            if len(banned_id[j])!=len(i[j]) or not re.match(banned_id[j],i[j]):
                chk=False
                break
        if chk:
            answer.append(i)
    return len({tuple(sorted(i)) for i in answer})