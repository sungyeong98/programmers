import java.util.*;
class Solution {
    public String solution(String myString) {
        String answer = "";
        for(char i:myString.toCharArray()){
            answer+=Character.toLowerCase(i);
        }
        return answer;
    }
}