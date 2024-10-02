class Solution {
    public String solution(int age) {
        String answer = "";
        String str_age = Integer.toString(age);
        for(char i : str_age.toCharArray()){
            answer += (char)(i-'0'+'a');
        }
        return answer;
    }
}