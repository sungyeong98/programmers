function solution(my_string) {
    var answer = my_string.split(' ').filter(word=>word!='');
    return answer;
}