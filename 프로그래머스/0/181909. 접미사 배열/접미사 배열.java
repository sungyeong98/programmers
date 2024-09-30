import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public String[] solution(String my_string) {
        ArrayList<String> temp = new ArrayList<>();
        for(int i=0; i<my_string.length(); i++){
            temp.add(my_string.substring(i,my_string.length()));
        }
        String[] result = new String[temp.size()];
        for(int i=0; i<temp.size(); i++){
            result[i]=temp.get(i);
        }
        Arrays.sort(result);
        return result;
    }
}