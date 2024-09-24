function solution(num_list) {
    let sum = num_list.reduce((acc, curr) => acc + curr, 0) ** 2;
    let product = num_list.reduce((acc, curr) => acc * curr, 1);
    if(sum>product){
        return 1
    }
    return 0
}