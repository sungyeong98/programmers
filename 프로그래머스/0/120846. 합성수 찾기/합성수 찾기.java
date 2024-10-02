class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int i=4; i<=n; i++){
            if(isComposite(i)){
                answer++;
            }
        }
        return answer;
    }
    private boolean isComposite(int num){
        if(num<4)   return false;
        for(int i=2; i<=Math.sqrt(num); i++){
            if(num%i==0){
                return true;
            }
        }
        return false;
    }
}