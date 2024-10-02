import java.util.Set;
import java.util.HashSet;
class Solution {
    public String solution(String my_string, int[] indices) {
        StringBuilder result = new StringBuilder();
        
        Set<Integer> idx = new HashSet<>();
        for(int i : indices){
            idx.add(i);
        }
        
        for(int i=0; i<my_string.length(); i++){
            if(!idx.contains(i)){
                result.append(my_string.charAt(i));
            }
        }
        return result.toString();
    }
}