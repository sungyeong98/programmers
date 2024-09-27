class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        for(char i:my_string.toCharArray()){
            if(i==alp.charAt(0)){
                answer+=Character.toUpperCase(i);
            }
            else{
                answer+=i;
            }
        }
        return answer;
    }
}