import java.util.Arrays;
class Solution {
    public int[] solution(String my_string) {
        int[] result = new int[52];
        Arrays.fill(result, 0);
        
        for(char c : my_string.toCharArray()){
            if(Character.isLowerCase(c)){
                result[c-'a'+26]+=1;
            }
            else{
                result[c-'A']+=1;
            }
        }
        return result;
    }
}