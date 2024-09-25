class Solution {
    public int solution(int[] num_list) {
        int v1 = 0, v2 = 1;
        for(int i=0; i<num_list.length; i++){
            v1+=num_list[i];
            v2*=num_list[i];
        }
        return (v2<Math.pow(v1,2))?1:0;
    }
}