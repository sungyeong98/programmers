class Solution {
    public int solution(String myString, String pat) {
        String temp = "";
        for(char c:myString.toCharArray()){
            if(c=='A'){
                temp+='B';
            }
            else{
                temp+='A';
            }
        }
        
        return temp.contains(pat)?1:0;
    }
}