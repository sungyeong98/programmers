class Solution {
    fun solution(myString: String, pat: String): Int {
        if (myString.length < pat.length) {
            return 0
        }
        
        val temp1 = myString.toLowerCase()
        val temp2 = pat.toLowerCase()
        
        return if(temp2 in temp1) 1 else 0
    }
}