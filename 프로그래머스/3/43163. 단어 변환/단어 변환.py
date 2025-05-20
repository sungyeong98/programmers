from difflib import SequenceMatcher
from collections import deque
def solution(begin, target, words):
    result = 0
    queue, visited = deque([(begin, 0)]), set()
    
    while queue:
        current_word, cnt = queue.popleft()     # 현재 단어, 변환 횟수
        
        if current_word == target:  # 현재 단어와 타겟 단어가 같을 때
            result = cnt
            break
        
        for next_word in words:
            # 다음 단어를 방문하지 않은 상태이고,
            # 현재 단어와 다음 단어가 1글자만 차이나는 경우
            # SequenceMatcher = 문자열을 비교하여 얼마나 유사한지 값으로 보여주는 함수
            if next_word not in visited and \
            SequenceMatcher(None, current_word, next_word).ratio() == (len(begin) - 1) / len(begin):
                visited.add(next_word)
                queue.append((next_word, cnt + 1))
    
    return result