import java.util.ArrayList;
class Solution {
    public int[] solution(String myString) {
        ArrayList<Integer> temp = new ArrayList<>();
        int idx = 0;
        for(int i=0; i<myString.length(); i++){
            if(myString.charAt(i)=='x'){
                temp.add(i-idx);
                idx=i+1;
            }
        }
        temp.add(myString.length()-idx);
        int[] result = new int[temp.size()];
        for(int i=0; i<temp.size(); i++){
            result[i]=temp.get(i);
        }
        return result;
    }
}