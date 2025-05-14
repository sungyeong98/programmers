from collections import deque
def solution(prices):
    result, queue = [], deque(prices)
    
    while(queue):
        cur_price, cnt = queue.popleft(), 0       
        for next_price in queue:
            cnt+=1
            if cur_price > next_price:    break
        result.append(cnt)
        
    return result
# result = 결과 정보를 담고 있는 리스트
# queue = deque에 prices 리스트 넣은 것

# queue에 값이 존재하지 않을 때까지,
# queue에서 값 추출 -> cur_price = 현재 가격, cnt = 가격이 오른 시간
# queue를 for문으로 순회, cnt에 +1
# 만약 현재가격이 다음 가격보다 크다면 종료
# cnt를 result에 추가