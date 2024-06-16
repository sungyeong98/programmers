import re
def solution(word, pages):
    answer = 0
    temp,chk={},[]
    for i in range(len(pages)):
        words=pages[i]
        pattern0=r'[^a-zA-Z]+'
        clean=re.sub(pattern0,' ',words)
        w=clean.split()
        cnt=0
        for j in w:
            if j.lower()==word.lower():
                cnt+=1
        pattern1=r'<meta property="og:url" content="([^"]+)"/>'
        target1=re.findall(pattern1,pages[i])
        temp[target1[0]]=[i,cnt]
        pattern2=r'<a href="([^"]+)">'
        target2=re.findall(pattern2,pages[i])
        temp[target1[0]].append(target2)
    for i in temp:
        for j in temp[i][2]:
            if j in temp:
                temp[j].append(temp[i][1]/len(temp[i][2]))
    for i in temp:
        score=temp[i][1]
        for j in range(3,len(temp[i])):
            score+=temp[i][j]
        chk.append([score,temp[i][0]])
    chk.sort(key=lambda x:(-x[0],x[1]))
    return chk[0][1]