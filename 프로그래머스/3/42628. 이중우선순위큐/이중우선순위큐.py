from heapq import heappush, heappop
def solution(operations):
    temp1, temp2 = [], []
    
    for op in operations:
        word, num = op.split(" ")
        
        if word == "I":
            heappush(temp1, int(num))
            heappush(temp2, -int(num))
        elif word == "D" and num == "1" and temp1:
            target = heappop(temp2)
            temp1.remove(-target)
        elif word == "D" and num == "-1" and temp1:
            target = heappop(temp1)
            temp2.remove(-target)
            
    return [max(temp1), min(temp1)] if temp1 else [0, 0]