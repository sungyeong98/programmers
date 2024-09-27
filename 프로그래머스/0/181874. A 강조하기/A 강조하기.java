class Solution {
    public String solution(String myString) {
        String answer = "";
        for(char i:myString.toCharArray()){
            if(i=='a'||i=='A'){
                answer+='A';
            }
            else{
                answer+=Character.toLowerCase(i);
            }
        }
        return answer;
    }
}