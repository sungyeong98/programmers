import java.util.ArrayList;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> temp = new ArrayList<>();
        for (int i=1; i<=n; i++){
            if(n%i==0){
                temp.add(i);
            }
        }
        
        int[] result = new int[temp.size()];
        for(int i=0; i<temp.size(); i++){
            result[i] = temp.get(i);
        }
        return result;
    }
}