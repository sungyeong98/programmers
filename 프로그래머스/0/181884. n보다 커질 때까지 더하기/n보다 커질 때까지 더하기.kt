class Solution {
    fun solution(numbers: IntArray, n: Int): Int {
        var result = 0
        for (i in numbers) {
            if (result > n) return result
            result += i
        }
        return result
    }
}