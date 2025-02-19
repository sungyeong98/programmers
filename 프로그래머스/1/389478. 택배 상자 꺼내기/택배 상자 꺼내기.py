from collections import deque
def solution(n, w, num):
    box = deque([])
    idx = 0
    target_idx = 0
    for i in range(1, n+1, w):
        if idx % 2 == 0:
            temp = [j for j in range(i, i+w)]
            box.appendleft(temp)
            if i<= num <i+w:    target_idx = temp.index(num)
        else:
            temp = [j for j in range(i+w-1, i-1, -1)]
            box.appendleft(temp)
            if i<= num <i+w:    target_idx = temp.index(num)
        idx+=1
    answer = 0
    for i in box:
        if i[target_idx] > n:
            continue
        answer+=1
        if i[target_idx] == num:
            break
    return answer