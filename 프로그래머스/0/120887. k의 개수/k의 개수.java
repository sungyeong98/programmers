class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String target = Integer.toString(k);
        for(int ii=i; ii<=j; ii++){
            String s = Integer.toString(ii);
            for(char c : s.toCharArray()){
                if(Character.toString(c).equals(target)){
                    answer++;
                } 
            }
        }
        return answer;
    }
}