import kotlin.math.*
class Solution {
    fun solution(a: Int, b: Int): Int {
        return max((a.toString() + b.toString()).toInt(), 2*a*b)
    }
}