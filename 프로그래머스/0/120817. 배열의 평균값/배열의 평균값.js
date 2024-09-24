function solution(numbers) {
    var temp = 0;
    for (let i=0; i<numbers.length ; i++){
        temp+=numbers[i]
    }
    return temp/numbers.length
}