class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        for(char i:my_string.toCharArray()){
            if(i!=letter.toCharArray()[0]){
                answer+=i;
            }
        }
        return answer;
    }
}