function solution(box, n) {
    return box.reduce((acc,curr) => acc*=Math.floor(curr/n), 1)
}