function solution(num_list) {
    var odd = 0;
    var even = 0;
    for(let i=0; i<num_list.length; i+=2){
        even+=num_list[i]
    }
    for(let i=1; i<num_list.length; i+=2){
        odd+=num_list[i]
    }
    return even>odd?even:odd
}