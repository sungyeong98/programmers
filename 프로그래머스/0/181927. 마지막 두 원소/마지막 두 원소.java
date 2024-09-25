import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;
class Solution {
    public int[] solution(int[] num_list) {
        int v1 = num_list[num_list.length-1], v2 = num_list[num_list.length-2];
        int new_val = (v1>v2)?(v1-v2):(v1*2);
        
        return IntStream.concat(Arrays.stream(num_list), IntStream.of(new_val)).toArray();
    }
}