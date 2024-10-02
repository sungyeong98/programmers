class Solution {
    public int[] solution(int[] arr) {
        int n = arr.length;
        int add = 0;
        for(int i=1; i<=1024; i*=2){
            if(n<=i){
                add=(i-n);
                break;
            }
        }
        
        int[] result = new int[n+add];
        for(int i=0; i<n; i++){
            result[i] = arr[i];
        }
        return result;
    }
}