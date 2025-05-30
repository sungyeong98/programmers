from heapq import heappush, heappop
def solution(operations):
    temp1, temp2 = [], []   # temp1 = 최소힙, temp2 = 최대힙
    
    for op in operations:
        word, num = op.split(" ")   # 명령어, 숫자
        
        if word == "I":     # 숫자 삽입
            heappush(temp1, int(num))   # 최소힙에 숫자 삽입
            heappush(temp2, -int(num))  # 최대힙에 숫자 삽입
        elif word == "D" and num == "1" and temp1:  # 최댓값 삭제 명령어
            target = heappop(temp2) # 최대힙에서 최대값 추출
            temp1.remove(-target)   # 최소힙에서 -target값 추출
        elif word == "D" and num == "-1" and temp1: # 최솟값 삭제 명령어
            target = heappop(temp1) # 최소힙에서 최솟값 추출
            temp2.remove(-target)   # 최대힙에서 -target 추출
            
    return [max(temp1), min(temp1)] if temp1 else [0, 0]