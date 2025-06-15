class Solution {
    fun solution(number: Int, n: Int, m: Int): Int {
        if ((number % n == 0) and (number % m == 0)) {
            return 1
        } else {
            return 0
        }
    }
}