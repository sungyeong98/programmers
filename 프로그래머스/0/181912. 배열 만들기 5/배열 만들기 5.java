import java.util.ArrayList;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> temp = new ArrayList<>();
        for(int i=0; i<intStrs.length; i++){
            String sub = intStrs[i].substring(s,s+l);
            int num = Integer.valueOf(sub);
            if(num>k){
                temp.add(num);
            }
        }
        
        int[] result = new int[temp.size()];
        for(int i=0; i<temp.size(); i++){
            result[i] = temp.get(i);
        }
        return result;
    }
}