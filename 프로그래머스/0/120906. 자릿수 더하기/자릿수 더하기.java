class Solution {
    public int solution(int n) {
        int answer = 0;
        for(char i:Integer.toString(n).toCharArray()){
            answer+=i-'0';
        }
        return answer;
    }
}