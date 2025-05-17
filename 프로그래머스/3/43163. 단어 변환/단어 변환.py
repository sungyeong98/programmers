from difflib import SequenceMatcher
from collections import deque
def solution(begin, target, words):
    result = 0
    queue, visited = deque([(begin, 0)]), set()
    
    while queue:
        current_word, cnt = queue.popleft()
        
        if current_word == target:
            result = cnt
            break
        
        for next_word in words:
            if next_word not in visited and \
            SequenceMatcher(None, current_word, next_word).ratio() == (len(begin) - 1) / len(begin):
                visited.add(next_word)
                queue.append((next_word, cnt + 1))
    
    return result