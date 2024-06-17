from difflib import SequenceMatcher
from collections import deque
def solution(begin, target, words):
    answer,q,v=0,deque(),[0]*len(words)
    q.append([begin,0])
    while q:
        word,n=q.popleft()
        if word==target:
            answer=n
            break
        for i in range(len(words)):
            if not v[i] and SequenceMatcher(None,word,words[i]).ratio()==(len(begin)-1)/len(begin):
                q.append([words[i],n+1])
                v[i]=1
    return answer