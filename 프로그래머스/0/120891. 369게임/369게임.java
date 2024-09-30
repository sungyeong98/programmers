class Solution {
    public int solution(int order) {
        int answer = 0;
        for(char i:Integer.toString(order).toCharArray()){
            if(i-'0'==3 || i-'0'==6 || i-'0'==9){
                answer+=1;
            }
        }
        return answer;
    }
}