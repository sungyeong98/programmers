from collections import Counter
def solution(citations):
    counter, temp = Counter(citations), sorted(set(citations))
    cnt, result = 0, 0
    
    for i in temp[::-1]:
        cnt+=counter[i]
        result = max(result, min(cnt, i))
    
    return result
# counter = 논문 인용 횟수 별 갯수
# temp = 논문 정렬 리스트
# cnt = 인용이 총 몇 번 됐는지 저장하기 위한 변수
# result = 정답 변수

# temp를 역순으로(큰 값부터) 순회

# 예시 [3, 0, 6, 1, 5]
# counter = {6: 1, 5: 1, 3: 1, 1: 1, 0: 1}
# temp = [0, 1, 3, 5, 6]
# cnt = 0, result = 0
# for i in [6, 5, 3, 1, 0]
# i = 6, cnt = 1, result = max(0, min(1, 6)) = max(0, 1) = 1
# i = 5, cnt = 2, result = max(1, min(2, 5)) = max(1, 2) = 2
# i = 3, cnt = 3, result = max(2, min(3, 3)) = max(2, 3) = 3
# i = 1, cnt = 4, result = max(3, min(4, 1)) = max(3, 1) = 3
# i = 0, cnt = 5, result = max(3, min(5, 0)) = max(3, 0) = 3