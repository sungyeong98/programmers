class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for(char i:my_string.toCharArray()){
            for(int j=0; j<n; j++){
                answer+=i;
            }
        }
        return answer;
    }
}