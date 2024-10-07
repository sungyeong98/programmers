class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for(int i : num_list){
            int target = i;
            int cnt = 0;
            while(true){
                if(target==1)   break;
                else if(target%2==0){
                    target/=2;
                }
                else{
                    target=(target-1)/2;
                }
                cnt++;
            }
            answer+=cnt;
        }
        return answer;
    }
}