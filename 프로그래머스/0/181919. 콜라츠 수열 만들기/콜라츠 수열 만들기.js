function solution(n) {
    var answer = [];
    while(n>0){
        answer.push(n)
        if(n===1){
            break
        }
        else if(n%2===0){
            n=Math.floor(n/2)
        }
        else{
            n=3*n+1
        }
    }
    return answer;
}