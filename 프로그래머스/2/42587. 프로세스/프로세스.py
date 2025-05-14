from collections import deque, Counter
def solution(priorities, location):
    queue = deque([(idx, val) for idx, val in enumerate(priorities)])
    p = sorted(set(priorities))
    counter = Counter(priorities)
    order = 1

    while queue:
        idx, val = queue.popleft()
        max_val = p[-1]
        
        if val == max_val:
            counter[max_val]-=1
            if counter[max_val] == 0:
                counter.pop(max_val)
                p.pop()
            if idx == location:
                return order
            order+=1
        else:
            queue.append((idx, val))

# queue = 중요도를 (인덱스, 값)의 형태로 담고 있는 deque 리스트
# p = 중요도의 순서를 나타내는 리스트
# counter = 각 중요도 별 존재 갯수를 담고 있는 딕셔너리
# order = 현재 실행 순서를 나타내는 변수

# queue에 내용물이 없을때까지 반복
# queue에서 꺼낸 값이 최상위 중요도라면, 인덱스가 locations가 동일한지 비교한다.
# 만약 최상위 중요도가 아니라면, 다시 queue에 값을 넣는다.