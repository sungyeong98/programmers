from collections import defaultdict
def solution(points, routes):
    load = defaultdict(lambda : defaultdict(set))
    result = 0

    for robot_id, route in enumerate(routes):
        cnt = 0
        for j in range(len(route) - 1):
            (start_x, start_y) = points[route[j] - 1]
            (end_x, end_y) = points[route[j + 1] - 1]

            load[cnt][(start_x, start_y)].add(robot_id)

            while start_x != end_x:
                start_x += 1 if start_x < end_x else -1
                cnt += 1
                load[cnt][(start_x, start_y)].add(robot_id)

            while start_y != end_y:
                start_y += 1 if start_y < end_y else -1
                cnt += 1
                load[cnt][(start_x, start_y)].add(robot_id)

    for time in load:
        for loc in load[time]:
            if len(load[time][loc]) >= 2:
                result += 1

    return result