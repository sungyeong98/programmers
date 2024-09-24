function solution(arr) {
    var answer = [];
    for(let i of arr){
        for(let j=0; j<i; j++){
            answer.push(i)
        }
    }
    return answer;
}