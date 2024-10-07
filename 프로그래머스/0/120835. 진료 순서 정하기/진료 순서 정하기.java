import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        
        Integer[] t = Arrays.stream(emergency).boxed().toArray(Integer[]::new);
        Arrays.sort(t, Collections.reverseOrder());
        
        int[] temp = Arrays.stream(t).mapToInt(Integer::intValue).toArray();
        
        for(int i=0; i<emergency.length; i++){
            for(int j=0; j<emergency.length; j++){
                if(temp[j]==emergency[i]){
                    answer[i]=j+1;
                    break;
                }
            }
        }
        
        return answer;
    }
}