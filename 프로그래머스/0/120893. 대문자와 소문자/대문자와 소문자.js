function solution(my_string) {
    var result = '';
    for(let i=0; i<my_string.length; i++){
        if(my_string[i]===my_string[i].toUpperCase()){
            result+=my_string[i].toLowerCase()
        }
        else{
            result+=my_string[i].toUpperCase()
        }
    }
    return result
}