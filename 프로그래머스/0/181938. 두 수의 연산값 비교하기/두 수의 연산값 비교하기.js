function solution(a, b) {
    var temp1 = Number(String(a)+String(b));
    var temp2 = 2*a*b;
    return temp1>temp2 ? temp1 : temp2
}