import java.util.Arrays;
import java.util.stream.IntStream;
class Solution {
    public int solution(int[] num_list) {
        int v1 = IntStream.range(0,num_list.length).filter(i->i%2==0).map(i->num_list[i]).sum();
        int v2 = IntStream.range(0,num_list.length).filter(i->i%2==1).map(i->num_list[i]).sum();
        
        return (v1>v2)?v1:(v2>v1)?v2:v1;
    }
}