class Solution {
    public int[][] solution(int[] num_list, int n) {
        int m = num_list.length/n;
        int[][] result = new int[m][n];
        int idx = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                result[i][j] = num_list[idx];
                idx++;
            }
        }
        
        return result;
    }
}