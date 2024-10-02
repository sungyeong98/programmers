class Solution {
    public int solution(String number) {
        int answer = 0;
        for(char i : number.toCharArray()){
            answer += Integer.valueOf(i-'0');
        }
        return answer%9;
    }
}