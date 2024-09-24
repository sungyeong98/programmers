function solution(myString) {
    var answer = '';
    for(let i of myString){
        if(i==='a' || i==='A'){
            answer+='A'
        }
        else{
            answer+=i.toLowerCase()
        }
    }
    return answer;
}