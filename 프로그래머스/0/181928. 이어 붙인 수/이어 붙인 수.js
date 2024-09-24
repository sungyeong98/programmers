function solution(num_list) {
    var odd = '';
    var even = '';
    for(let i of num_list){
        if(i%2===0){
            even+=String(i)
        }
        else{
            odd+=String(i)
        }
    }
    return Number(odd)+Number(even)
}