import java.util.Arrays;
class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] temp1 = Arrays.copyOfRange(num_list, n, num_list.length);
        int[] temp2 = Arrays.copyOfRange(num_list, 0, n);
        
        int[] result = new int[num_list.length];
        System.arraycopy(temp1, 0, result, 0, temp1.length);
        System.arraycopy(temp2, 0, result, temp1.length, temp2.length);
        return result;
    }
}