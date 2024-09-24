function solution(array) {
    var max_val = Math.max(...array);
    var max_idx = array.indexOf(max_val);
    return [max_val, max_idx]
}