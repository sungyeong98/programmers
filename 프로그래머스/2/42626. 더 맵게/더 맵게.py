from heapq import heapify, heappush, heappop
def solution(scoville, K):
    result = 0
    heapify(scoville)   # scoville 리스트를 heap 형태로 가공

    # scoville 리스트의 길이가 1 이하로 떨어질 때까지 반복
    while len(scoville) > 1:
        current1 = heappop(scoville)    # 가장 작은 값 추출
        if current1 >= K:   # 추출한 값이 K 이상이면 종료
            return result

        current2 = heappop(scoville)    # 2번 째로 작은 값 추출
        
        heappush(scoville, current1 + (current2 * 2))   # scoville에 계산한 값 추가
        result += 1     # 횟수 + 1
    
    if scoville[0] >= K:    # scoville 리스트의 길이가 1인 경우를 여기서 체크
        return result
    
    return -1