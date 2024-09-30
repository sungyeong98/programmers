class Solution {
    public int solution(int num, int k) {
        String num_str = String.valueOf(num);
        char target = Character.forDigit(k, 10);
        
        int index = num_str.indexOf(target);
        return (index==-1)?-1:(index+1);
    }
}