function solution(myString) {
    var answer = '';
    for(let i of myString){
        if(i<'l'){
            answer+='l'
        }
        else{
            answer+=i
        }
    }
    return answer;
}