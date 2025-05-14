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
# bridge = bridge_length 길이만큼의 다리 정보를 나타내고 있는 deque 리스트
# trucks = truck_weights 리스트를 deque에 담은 것
# result = 소요시간을 담고 있는 정답 변수
# wei_sum = 현재 다리에 올라가 있는 트럭 무게의 총합을 나타내는 변수

# bridge에 값이 존재하지 않을때까지 반복
# result에 1초 추가, wei_sum에서 bridge 0번째 값만큼 빼기
# 만약 trucks가 존재한다면, 내부 로직 실행
# trucks[0] 값과 wei_sum의 합이 weight 이하일 경우, bridge에 해당 트럭 정보 추가
# 아니라면 임시값(=0) 추가