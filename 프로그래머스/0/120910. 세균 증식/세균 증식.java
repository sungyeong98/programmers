class Solution {
    public int solution(int n, int t) {
        int answer = n;
        while(t>0){
            answer*=2;
            t-=1;
        }
        return answer;
    }
}