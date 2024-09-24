function solution(n_str) {
    var idx = 0;
    while(n_str[idx]==='0'){
        idx+=1
    }
    return n_str.slice(idx)
}