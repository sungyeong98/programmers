import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=1; i<=n; i+=2){
            result.add(i);
        }
        int[] answer = new int[result.size()];
        for(int i=0; i<result.size(); i++){
            answer[i]=result.get(i);
        }
        return answer;
    }
}