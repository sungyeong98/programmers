parent={(i,j):(i,j) for j in range(1,51) for i in range(1,51)}
chart=[['' for _ in range(51)] for _ in range(51)]

def query_find_data(location):
    r,c=query_find_parent(location)
    return chart[r][c]

def query_find_parent(location):
    if location==parent[location]:
        return location
    parent[location]=query_find_parent(parent[location])
    return parent[location]

def query_update(location,value):
    r,c=query_find_parent(location)
    chart[r][c]=value

def query_update_all(value1,value2):
    if value1==value2:
        return
    for i in range(1,51):
        for j in range(1,51):
            location=(i,j)
            if query_find_data(location)==value1:
                query_update(location,value2)

def query_merge(location1,location2):
    if location1==location2:
        return
    location1=query_find_parent(location1)
    location2=query_find_parent(location2)
    if query_find_data(location1)=='':
        parent[location1]=location2
    else:
        parent[location2]=location1

def query_unmerge(location):
    parent_location=query_find_parent(location)
    value=query_find_data(location)
    stack=[]
    for i in range(1,51):
        for j in range(1,51):
            temp_location=(i,j)
            if query_find_parent(temp_location)==parent_location:
                stack.append(temp_location)
                if temp_location==location:
                    chart[i][j]=value
                else:
                    chart[i][j]=''
    for loc in stack:
        parent[loc]=loc

def query_print(location,answer):
    value=query_find_data(location)
    if value=='':
        answer.append('EMPTY')
    else:
        answer.append(value)

def solution(commands):
    answer=[]
    for i in commands:
        command,*arg=i.split(' ')
        if command=='UPDATE':
            if len(arg)==3:
                location,value=(int(arg[0]),int(arg[1])),arg[2]
                query_update(location,value)
            else:
                value1,value2=arg[0],arg[1]
                query_update_all(value1,value2)
        elif command=='MERGE':
            location1,location2=(int(arg[0]),int(arg[1])),(int(arg[2]),int(arg[3]))
            query_merge(location1,location2)
        elif command=='UNMERGE':
            location=(int(arg[0]),int(arg[1]))
            query_unmerge(location)
        else:
            location=(int(arg[0]),int(arg[1]))
            query_print(location,answer)
    return answer