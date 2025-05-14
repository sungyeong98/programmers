from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge, trucks = deque([0] * bridge_length), deque(truck_weights)
    wei_sum, result = 0, 0

    while(bridge):
        result += 1
        wei_sum -= bridge.popleft()

        if trucks:
            if trucks[0] + wei_sum <= weight:
                temp = trucks.popleft()
                wei_sum += temp
                bridge.append(temp)
            else:
                bridge.append(0)
    
    return result