import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        Set<Integer> temp = new HashSet<>();
        for(int num:delete_list){
            temp.add(num);
        }
        return Arrays.stream(arr).filter(x->!temp.contains(x)).toArray();
    }
}