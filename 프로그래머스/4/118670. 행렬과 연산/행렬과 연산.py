from collections import deque
def solution(rc, operations):
    answer = []
    temp_in=deque(deque(i[1:-1]) for i in rc)
    temp_out=[deque(rc[i][0] for i in range(len(rc))),deque(rc[i][len(rc[0])-1] for i in range(len(rc)))]
    for i in operations:
        if i=='ShiftRow':
            temp_in.appendleft(temp_in.pop())
            temp_out[0].appendleft(temp_out[0].pop())
            temp_out[1].appendleft(temp_out[1].pop())
        else:
            temp_in[len(rc)-1].append(temp_out[1].pop())
            temp_out[0].append(temp_in[len(rc)-1].popleft())
            temp_in[0].appendleft(temp_out[0].popleft())
            temp_out[1].appendleft(temp_in[0].pop())
    for i in range(len(rc)):
        answer.append([])
        answer[i].append(temp_out[0][i])
        answer[i].extend(temp_in[i])
        answer[i].append(temp_out[1][i])
    return answer