function solution(myString, pat) {
    var temp = '';
    for(let i of myString){
        if(i==='A'){
            temp+='B'
        }
        else{
            temp+='A'
        }
    }
    return temp.includes(pat)?1:0
}