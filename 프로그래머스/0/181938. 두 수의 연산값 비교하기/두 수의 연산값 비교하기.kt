class Solution {
    fun solution(a: Int, b: Int): Int {
        val temp1: Int = (a.toString() + b.toString()).toInt()
        val temp2: Int = 2 * a * b
        val result = if (temp1 > temp2) temp1 else temp2
        
        return result
    }
}