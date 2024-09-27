class Solution {
    public String solution(String rsp) {
        String answer = "";
        for(char i:rsp.toCharArray()){
            if(i=='0'){
                answer+='5';
            }
            else if (i=='2'){
                answer+='0';
            }
            else{
                answer+='2';
            }
        }
        return answer;
    }
}