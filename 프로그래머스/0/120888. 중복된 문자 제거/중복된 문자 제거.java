class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(char i : my_string.toCharArray()){
            if(!answer.contains(String.valueOf(i))){
                answer+=i;
            }
        }
        return answer;
    }
}