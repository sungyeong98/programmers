import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(String my_string) {
        ArrayList<Integer> temp = new ArrayList<>();
        for(char i : my_string.toCharArray()){
            if(Character.isDigit(i)){
                temp.add(i-'0');   
            }
        }
        
        int[] result = new int[temp.size()];
        for(int i=0; i<temp.size(); i++){
            result[i] = temp.get(i);
        }
        Arrays.sort(result);
        return result;
    }
}