import java.util.ArrayList;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> num_list = new ArrayList<>();
        while(n>1){
            num_list.add(n);
            if(n%2==0){
                n/=2;
            }
            else{
                n=3*n+1;
            }
        }
        num_list.add(1);
        
        int[] result = new int[num_list.size()];
        for(int i=0; i<num_list.size(); i++){
            result[i] = num_list.get(i);
        }
        return result;
    }
}