import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayList<Integer> temp = new ArrayList<>();
        for(int i=0; i<flag.length; i++){
            if(flag[i]){
                for(int cnt=0; cnt<arr[i]*2; cnt++){
                    temp.add(arr[i]);
                }
            }
            else{
                for(int cnt=0; cnt<arr[i]; cnt++){
                    temp.remove(temp.size()-1);
                }
            }
        }
        
        int[] result = new int[temp.size()];
        for(int i=0; i<temp.size(); i++){
            result[i] = temp.get(i);
        }
        return result;
    }
}