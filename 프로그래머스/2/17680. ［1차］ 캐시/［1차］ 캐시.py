from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:  return len(cities) * 5
    cities = map(lambda x:x.lower(), cities)

    temp = deque([])
    result = 0
    
    for city in cities:
        if city in temp:
            temp.remove(city)
            temp.append(city)
            result += 1
        else:
            if len(temp) == cacheSize:
                temp.popleft()
            temp.append(city)
            result += 5
            
    return result