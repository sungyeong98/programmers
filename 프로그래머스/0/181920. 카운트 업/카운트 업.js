function solution(start_num, end_num) {
    var answer = [];
    while(start_num<=end_num){
        answer.push(start_num)
        start_num+=1
    }
    return answer;
}