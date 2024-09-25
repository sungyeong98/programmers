class Solution {
    public String solution(String n_str) {
        int idx = 0;
        while (n_str.charAt(idx)=='0'){
            idx+=1;
        }
        return n_str.substring(idx);
    }
}