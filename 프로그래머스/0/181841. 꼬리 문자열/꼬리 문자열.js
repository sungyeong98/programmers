function solution(str_list, ex) {
    var answer = '';
    for(let i of str_list){
        if(!i.includes(ex)){
            answer+=i
        }
    }
    return answer;
}