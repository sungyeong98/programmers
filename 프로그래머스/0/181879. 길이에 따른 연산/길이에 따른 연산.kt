class Solution {
    fun solution(num_list: IntArray): Int {
        val temp1 = num_list.sum()
        val temp2 = num_list.reduce {x, y -> x * y}
        
        return if (num_list.size >= 11) temp1 else temp2
    }
}