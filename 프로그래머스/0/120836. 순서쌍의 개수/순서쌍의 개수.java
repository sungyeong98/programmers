class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<=(int)Math.sqrt(n); i++){
            if(n%i==0){
                answer+=1;
            }
        }
        return Math.pow((int)Math.sqrt(n),2)==n?answer*2-1:answer*2;
    }
}